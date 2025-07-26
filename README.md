# Take Profit AI Alert System

Simple FastAPI service that gives an AI-style prediction on whether to exit a trade based on profit, momentum, ATR, and other features.

## Endpoint
POST /api/predict

### JSON Input Example
```json
{
  "entry": 15800,
  "price": 16012,
  "profit": 1.34,
  "momentum": 0.0045,
  "atr": 45.6,
  "volume_change": 0.12,
  "time_in_trade": 5
}
