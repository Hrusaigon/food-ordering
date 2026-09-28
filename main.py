from flask import Flask, render_template
import os

current_folder = os.getcwd() # current working directory

app = Flask(__name__, template_folder=current_folder, static_folder=current_folder)

@app.route("/")
def default():
    return render_template("default.html")

@app.route("/about-us")
def about_us():
    return render_template("about_us.html")


@app.route("/food-category")
def food_category():
    return render_template("food_category.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/finalize")
def finalize():
    return render_template("finalize.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)