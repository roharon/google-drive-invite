from flask import Flask, render_template

app = Flask(__name__)

@app.route("/invite")
def invite():
    
    return render_template("invite.html")