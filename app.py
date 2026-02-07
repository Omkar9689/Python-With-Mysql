from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # add your mysql password if set
    database="customer_db"
)

cursor = db.cursor(dictionary=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        sql = "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, phone))
        db.commit()

        return redirect("/")

    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    return render_template("index.html", customers=customers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
