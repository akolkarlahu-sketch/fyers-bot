import pandas as pd
from ta.trend import EMAIndicator, MACD, ADXIndicator
from ta.momentum import RSIIndicator
from ta.volume import VolumeWeightedAveragePrice


def titan_signal(candles):

    df = pd.DataFrame(candles)

    # Indicators

    df["ema20"] = EMAIndicator(df["close"], window=20).ema_indicator()
    df["ema50"] = EMAIndicator(df["close"], window=50).ema_indicator()
    df["ema200"] = EMAIndicator(df["close"], window=200).ema_indicator()

    df["rsi"] = RSIIndicator(df["close"], window=14).rsi()

    macd = MACD(df["close"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()

    adx = ADXIndicator(
        df["high"],
        df["low"],
        df["close"],
        window=14
    )

    df["adx"] = adx.adx()
    df["di_plus"] = adx.adx_pos()
    df["di_minus"] = adx.adx_neg()


    vwap = VolumeWeightedAveragePrice(
        df["high"],
        df["low"],
        df["close"],
        df["volume"]
    )

    df["vwap"] = vwap.volume_weighted_average_price()


    last = df.iloc[-1]


    # CALL OPTION BUY

    call_condition = (

        last.close > last.ema20
        and last.ema20 > last.ema50
        and last.ema50 > last.ema200

        and last.close > last.vwap

        and 60 < last.rsi < 70

        and last.adx > 25

        and last.di_plus > last.di_minus

        and last.macd > last.macd_signal

        and last.volume >
        df["volume"].rolling(20).mean().iloc[-1] * 2
    )


    # PUT OPTION BUY

    put_condition = (

        last.close < last.ema20
        and last.ema20 < last.ema50
        and last.ema50 < last.ema200

        and last.close < last.vwap

        and 30 < last.rsi < 40

        and last.adx > 25

        and last.di_minus > last.di_plus

        and last.macd < last.macd_signal

        and last.volume >
        df["volume"].rolling(20).mean().iloc[-1] * 2
    )


    if call_condition:
        return "BUY NIFTY/SENSEX CE"


    if put_condition:
        return "BUY NIFTY/SENSEX PE"


    return "NO SIGNAL"
