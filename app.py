from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def show_books():
    return render_template("items.html")


if __name__ == "__main__":
    app.run(debug=True)