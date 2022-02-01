import os
from flask import Flask, render_template, request

UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

user = {"username": "jamesbond", "password": "superpass123"}


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        username = data.get('username')
        password = data.get("password")

        if username == user['username'] and password == user["password"]:
            return "Jesteś w systemie. Wiadomość ulegnie samozniszczeniu... "

    return render_template("login.html")


@app.route("/images/", methods=["GET", "POST"])
def form_view():
    if request.method == "POST":
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return "File is uploaded"
    return render_template('form_with_image_example.html')


if __name__ == "__main__":
    app.run(debug=True)
