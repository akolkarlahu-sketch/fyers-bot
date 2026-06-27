from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Titan AI Signal Bot Running"


@app.route("/callback")
def callback():

    auth_code = request.args.get("auth_code")

    print("AUTH CODE RECEIVED:", auth_code)

    return f"""
    <h2>FYERS Login Successful</h2>
    <p>Auth Code received:</p>
    <p>{auth_code}</p>
    <p>You can close this page.</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
