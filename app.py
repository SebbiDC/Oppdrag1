from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title = "Home")

@app.route("/om")
def om():
    return render_template("om.html", title = "Noe")

@app.route("/registrering")
def registrering():
    return render_template("registrering.html", title = "registrering")


if __name__ == "__main__":
    app.run(debug=True)