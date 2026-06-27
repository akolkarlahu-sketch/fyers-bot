from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Titan AI Signal Bot Running"


@app.route("/callback")
def callback():

    print("FULL CALLBACK URL:", request.url)
    print("ARGS:", request.args)

    return f"""
    <h2>FYERS Callback Received</h2>

    Full URL:
    <br>
    {request.url}

    <br><br>

    Parameters:
    <br>
    {request.args}
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
