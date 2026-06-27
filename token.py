import os
from fyers_apiv3 import fyersModel


client_id = os.getenv("FYERS_APP_ID")
secret_key = os.getenv("FYERS_SECRET_KEY")
redirect_uri = os.getenv("FYERS_REDIRECT_URI")


auth_code = "PASTE_NEW_AUTH_CODE_HERE"


session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type="code",
    grant_type="authorization_code"
)


session.set_token(auth_code)

response = session.generate_token()

print(response)
