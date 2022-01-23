from flask import Flask, render_template, request

app = Flask(__name__)

user = {"username": "jamesbond", "password": "superpass123"}


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        username = data.get('username')
        password = data.get("password")

        if username == user['username'] and password == user["password"]:
            return "Jesteś ty i ty w sytemie. Wiadomość ulegnie samozniszczeniu... "

    return render_template("form_example.html")


if __name__ == "__main__":
    app.run(debug=True)