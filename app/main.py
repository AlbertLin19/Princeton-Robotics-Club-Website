from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_view():
    return render_template("home.html")

@app.route("/2020-virtual-micromouse-competition/")
def competition_view():
    return render_template("competition.html")

@app.route("/projects/")
def projects_view():
    return render_template("projects.html")

@app.route("/supporters/")
def supporters_view():
    return render_template("supporters.html")

@app.route("/join/")
def join_view():
    return render_template("join.html")

@app.route("/members/")
def members_view():
    return render_template("members.html")

@app.route("/leadership/")
def leadership_view():
    return render_template("leadership.html")

    