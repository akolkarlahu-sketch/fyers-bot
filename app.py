from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "FYERS Bot Server Running"

@app.route("/callback")
def callback():
    code = request.args.get("auth_code")
    print("AUTH CODE:", code)

    return "FYERS Login Successful. You can close this page."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

