import os
from flask import Flask, render_template, request, Response, redirect
from modules.share import share_task

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/invite", methods=['GET'])
def invite_result():
    return render_template("invite.html", file_id=os.environ['file_id'])

@app.route("/error", methods=['GET'])
def error():
    return render_template("error.html")

@app.route("/invite", methods=['POST'])
def invite_post():
    response = share_task(email_address=request.json['email'], verify_code=request.json['verify_code'])

    if (int(response)/100 == 4) or (int(response)/100==5):
        return redirect('/error')
    else:
        return redirect('/invite')

if __name__ == "__main__":
    app.run("0.0.0.0", "80")