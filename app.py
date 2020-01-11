from flask import Flask, render_template, request
from modules.share import share_task
app = Flask(__name__)


@app.route("/invite", methods=['GET'])
def invite_get():
    return render_template("invite.html")

@app.route("/invite", methods=['POST'])
def invite_post():
    return share_task(request.json['email'])