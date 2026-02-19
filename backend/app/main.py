import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import stocks

# -------------------------
# Load .env early
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

# -------------------------
# Create FastAPI app
# -------------------------
app = FastAPI(title="Stock Education API")

# -------------------------
# CORS setup (dev-safe)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only; in prod, use your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Include router
# -------------------------
app.include_router(stocks.router, prefix="/stocks")

# -------------------------
# Root endpoint
# -------------------------
@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/test_env")
def test_env():
    import os
    return {"api_key": os.getenv("TWELVE_DATA_API_KEY")}
