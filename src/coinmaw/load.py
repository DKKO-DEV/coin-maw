import sqlite3
from typing import List, Tuple, Any

def load_data(
        market_data: List[Tuple[Any, Any, Any, Any, Any]],
        assets_data: List[Tuple[Any, Any, Any]],
        db_name: str = "crypto_pipeline.db"
) -> None:
    """Method to upload the market's data into the database using SQLite"""
    INSERT_ASSETS_SQL = """INSERT INTO assets(id, symbol, asset_name)
    VALUES(?,?,?) ON CONFLICT(id) DO NOTHING"""

    INSERT_MARKET_DATA_SQL = """INSERT INTO market_data(asset_id, current_price, market_cap, trading_volume_24h, captured_at)
    VALUES(?,?,?,?,?)"""

    try:
        with sqlite3.connect(db_name) as conn:
            
            cursor = conn.cursor()

            cursor.executemany(INSERT_ASSETS_SQL, assets_data)
            cursor.executemany(INSERT_MARKET_DATA_SQL, market_data)

            conn.commit()
    except sqlite3.Error as e:
        print(f"Error in database: {e}")
    else:
        print("Data loading successful.")

if __name__ == "__main__":
    # small upload test
    from .extract import fetch_market_data
    from .transform import transform_data

    raw = fetch_market_data()

    assets, market = transform_data(raw)
    db = "crypto_pipeline.db"
    # load_data(market_data=market, assets_data=assets, db_name= db)

    # fetch a row.
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT asset_id, current_price, captured_at FROM market_data")

            test_row = cursor.fetchone()
            print(test_row)

    except sqlite3.Error as e:
        print(e)