from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<name>")
def homepage(name):
    students = {"Naeemah": 25, "godwin": 26, "Thapelo": 47, "Jason": 23}
    return render_template("homepage.html", name=name)


@app.route("/loopy/<int:number>")
def loopy(number):
    return render_template("numbers_page.html", number=number)


if __name__ == '__main__':
    app.debug = True
    app.run()
