from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<name>")
def five_for(name):
    return render_template("forfive.html", names=name)


@app.route("/leapyears")
def leap_year():
    return render_template("leapyears.html")


@app.route("/year", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        value_first = int(request.form["first"])
        value_second = int(request.form["second"])
        return render_template("leapyears.html", first=value_first, second=value_second)
    else:
        return render_template("year.html")


@app.route("/oneenter", methods=["GET", "POST"])
def one_enter():
    if request.method == "POST":
        value_first = int(request.form["firsts"])
        return render_template("enterleapyear.html", year=value_first)
    else:
        return render_template("oneenter.html")


if __name__ == "__main__":
    app.run(debug=True)
