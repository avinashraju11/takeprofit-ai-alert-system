from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TradeData(BaseModel):
    entry: float
    price: float
    profit: float
    momentum: float
    atr: float
    volume_change: float
    time_in_trade: float

@app.post("/api/predict")
async def predict(data: TradeData):
    score = (
        data.profit * 0.4 +
        (1 - data.momentum) * 0.2 +
        (1 - data.atr / 100) * 0.1 +
        data.volume_change * 0.15 +
        (1 - data.time_in_trade / 20) * 0.15
    )

    exit_signal = score > 0.75
    return {
        "exit": exit_signal,
        "confidence": round(score, 2)
    }
