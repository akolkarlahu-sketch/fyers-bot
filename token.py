import os
from fyers_apiv3 import fyersModel

APP_ID = os.getenv("FYERS_APP_ID")
SECRET_KEY = os.getenv("FYERS_SECRET_KEY")
REDIRECT_URI = os.getenv("FYERS_REDIRECT_URI")
AUTH_CODE = os.getenv("FYERS_AUTH_CODE")

session = fyersModel.SessionModel(
    client_id=APP_ID,
    secret_key=SECRET_KEY,
    redirect_uri=REDIRECT_URI,
    response_type="code",
    grant_type="authorization_code"
)

session.set_token(AUTH_CODE)

response = session.generate_token()

print(response)
