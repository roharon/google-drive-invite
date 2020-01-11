from flask import Flask, render_template
from modules import share
app = Flask(__name__)


@app.route("/invite", methods=['GET'])
def invite_get():
    return render_template("invite.html")

@app.route("/invite", methods=['POST'])
def invite_post():
    return share.share_task()
