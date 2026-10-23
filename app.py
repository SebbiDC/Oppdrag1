from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title = "Home")

@app.route("/om")
def om():
    return render_template("om.html", title = "Noe")

@app.route("/registrering", methods = ["GET", "POST"])
def registrering():

    if request.method == "POST":
        navn = request.form["navn"]
        fag = request.form["fag"]
        email = request.form["email"]
        alder = request.form["alder"]
        kurs = request.form["kurs"]

        return render_template(
            "resultat.html",
            navn = navn,
            fag = fag,
            email = email,
            alder = alder
            )
    return render_template("registrering.html", title = "registrering")




if __name__ == "__main__":
    app.run(debug=True)