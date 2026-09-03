from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

books = [
    {"title": "Kobzar", "author": "Taras Shevchenko", "category": "poetry"},
    {"title": "Forest song", "author": "Lesya Ukrainka", "category": "drama-extravaganza"}
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def show_books():
    return render_template("items.html", books=books)


@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    category = request.form.get("category", "Загальне")

    if title and author:
        books.append({"title": title, "author": author, "category": category})

    return redirect(url_for("show_books"))


if __name__ == "__main__":
    app.run(debug=True)