import os
from fyers_apiv3 import fyersModel


client_id = os.getenv("FYERS_APP_ID")
access_token = os.getenv("FYERS_ACCESS_TOKEN")


fyers = fyersModel.FyersModel(
    client_id=client_id,
    token=access_token,
    log_path=""
)


def get_candles(symbol):

    data = {
        "symbol": symbol,
        "resolution": "15",
        "date_format": "1",
        "range_from": "2026-06-20",
        "range_to": "2026-06-27",
        "cont_flag": "1"
    }

    response = fyers.history(data=data)

    return response
