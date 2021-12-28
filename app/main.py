from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def competition_view():
    return render_template("competition.html")