from flask import Flask, render_template, request, Response
from modules.share import share_task
app = Flask(__name__)


@app.route("/invite", methods=['GET'])
@app.route("/", methods=['GET'])
def invite_get():
    return render_template("invite.html")

@app.route("/invite", methods=['POST'])
def invite_post():
    response = share_task(email_address=request.json['email'], verify_code=request.json['verify_code'])

    if response == "400":
        return Response("not found", status=400)
    
    elif response == "500":
        return Response("env error", status=500)

    else:
        return response