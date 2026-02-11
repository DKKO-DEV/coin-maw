import os
import requests
from datetime import datetime, timezone
from typing import Dict, List, Any
from dotenv import load_dotenv

load_dotenv()

COINGECKO_API_MARKET_URL = "https://api.coingecko.com/api/v3/coins/markets"
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")

def fetch_market_data() -> List[Dict[str, Any]]:
    """Fetch top 50 coins by market cap from Coingecko."""

    headers = {"x-cg-demo-api-key": COINGECKO_API_KEY} if COINGECKO_API_KEY else {}
    query ={
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }

    try:
        api_response = requests.get(
            COINGECKO_API_MARKET_URL,
            params= query,
            headers= headers,
            timeout= 10
        )

        api_response.raise_for_status()

        api_data_list = api_response.json()

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
        raise   
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        raise

    # Validate List
    if not isinstance(api_data_list, list):
        raise ValueError(f"Expected a List of coins, got {type(api_data_list)}")

    # Add timestamp to each dictionary fetched.
    current_time = datetime.now(timezone.utc).isoformat()
    for coin in api_data_list:
        coin["captured_at"] = current_time
    
    return api_data_list

if __name__ == "__main__":
    try:
        coin_data = fetch_market_data()
        print(f"Successfully fetched {len(coin_data)} coins.")
    except Exception as e:
        print(f"Failed: {e}")