from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="uber"
)

cursor = db.cursor()

# HOME + READ
@app.route('/')
def index():
    cursor.execute("SELECT * FROM customer")
    data = cursor.fetchall()
    return render_template('index.html', customers=data)

# CREATE (INSERT)
@app.route('/insert', methods=['POST'])
def insert():
    name = request.form['name']
    mobile = request.form['mobile']
    amount = request.form['amount']
    location = request.form['location']

    sql = "INSERT INTO customer (name, mobile, amount, location) VALUES (%s, %s, %s, %s)"
    values = (name, mobile, amount, location)

    cursor.execute(sql, values)
    db.commit()

    return redirect('/')

# DELETE
@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM customer WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

# UPDATE
@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    name = request.form['name']
    mobile = request.form['mobile']
    amount = request.form['amount']
    location = request.form['location']

    sql = "UPDATE customer SET name=%s, mobile=%s, amount=%s, location=%s WHERE id=%s"
    values = (name, mobile, amount, location, id)

    cursor.execute(sql, values)
    db.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)