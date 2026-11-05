from flask import Flask, render_template
import os, sqlite3

current_folder = os.getcwd() # current working directory

app = Flask(__name__, template_folder=current_folder, static_folder=current_folder)

@app.route("/")
def default():
    return render_template("default.html")

@app.route("/about-us")
def about_us():
    return render_template("about_us.html")

@app.route("/menu")
def menu():
    db = sqlite3.connect("food.db")
    cursor = db.cursor()

    query = """SELECT category FROM category"""
    category_list = cursor.execute(query).fetchall()

    query = """SELECT * FROM menu"""
    menu = cursor.execute(query).fetchall()

    return render_template("menu.html", categories=category_list, menu=menu)



@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/finalize")
def finalize():
    return render_template("finalize.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
