from fastapi import APIRouter, HTTPException
import os
import httpx

router = APIRouter()

@router.get("/")
def list_stocks():
    return ["AAPL","MSFT","TSLA","NVDA","GOOG","AMZN","META","NFLX","AMD","INTC"]

@router.get("/{symbol}")
async def get_stock(symbol: str):
    # load the API key inside the function
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv("TWELVE_DATA_API_KEY")
    if not API_KEY:
        raise RuntimeError("TWELVE_DATA_API_KEY not found in environment")

    url = (
        f"https://api.twelvedata.com/time_series"
        f"?symbol={symbol}"
        f"&interval=1day"
        f"&outputsize=90"
        f"&apikey={API_KEY}"
    )

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            res = await client.get(url)
            res.raise_for_status()
            data = res.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Request error: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"HTTP error: {e}")

    if "values" not in data:
        raise HTTPException(status_code=400, detail=data)

    return [
        {
            "Date": row["datetime"],
            "Open": float(row["open"]),
            "High": float(row["high"]),
            "Low": float(row["low"]),
            "Close": float(row["close"]),
        }
        for row in reversed(data["values"])
    ]
