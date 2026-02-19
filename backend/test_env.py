import os
from dotenv import load_dotenv

load_dotenv()  # loads .env in the same folder

print("API KEY:", os.getenv("TWELVE_DATA_API_KEY"))
