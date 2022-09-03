import os
from flask import Flask, render_template, request, Response, redirect
from modules.share import share_task

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    data = dict(title=os.environ['title'], subtitle=os.environ['subtitle'])
    return render_template("home.html", data=data)


@app.route("/invite", methods=['GET'])
def invite_result():
    return render_template("invite.html", file_id=os.environ['file_id'])


@app.route("/invite", methods=['POST'])
def invite_post():
    response = share_task(email_address=request.json['email'], verify_code=request.json['verify_code'])

    if type(response) == str:
        # if status code return
        return redirect('/error')
    else:
        return redirect('/invite')


@app.route("/error", methods=['GET'])
def error():
    return render_template("error.html")


if __name__ == "__main__":
    app.run("0.0.0.0", "80")
