"""Coinmaw's core logic"""
import sys
from pathlib import Path
from requests.exceptions import HTTPError, RequestException 

from src.coinmaw.database import initialize_db
from src.coinmaw.extract import fetch_market_data
from src.coinmaw.transform import transform_data
from src.coinmaw.load import load_data


def main_loop():
    # extract the data
    try:
        coingecko_raw_data = fetch_market_data()
    except HTTPError as e:
        print(f"HTTP error from Coingecko API: {e.response.status_code} - {e.response.text}")
        sys.exit(1)
    except RequestException as e:
        print(f"Error in fetching data from Coingecko API: {e}")
        sys.exit(1)
    else: 
        if not coingecko_raw_data:
            print("There's no data to process. Quitting..")
            sys.exit(1)

    # transform the data
    assets_data, market_data = transform_data(coingecko_raw_data)
    
    # upload data to the database
    load_data(assets_data= assets_data, market_data=market_data)


if __name__ == "__main__":
    # If there's no database, initialize it.
    db_default_path = Path("crypto_pipeline.db")
    if not db_default_path.exists():
        initialize_db()

    # Upload data to the database
    main_loop()
    