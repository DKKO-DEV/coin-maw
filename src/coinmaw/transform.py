from typing import List, Dict, Any, Tuple

def transform_data(raw_data: List[Dict[str, Any]]) -> Tuple[List[Tuple], List[Tuple]]:
    """
    Separates raw API data into two lists of tuples for the database
    Returns: (assets_data, market_data)
    """
    assets_data = [] 
    market_data = []

    for coin in raw_data:

        # Extract for assets table
        coin_id = coin.get("id")
        symbol = coin.get("symbol")
        asset_name = coin.get("name")

        if not coin_id or not symbol or not asset_name: # is NOT NULL on the schema
            print(f"Skipping coin due to incomplete data: {coin}") 
            continue

        # Extract for market_data table
        current_price = coin.get("current_price")
        market_cap = coin.get("market_cap")
        trading_volume_24h = coin.get("total_volume")
        captured_at = coin.get("captured_at")

        # Append to the corresponding tuples in onder
        assets_data.append((coin_id, symbol, asset_name))
        market_data.append((coin_id, current_price, market_cap, trading_volume_24h, captured_at))

    return assets_data, market_data


if __name__ == "__main__":
    # Test Transformation logic
    from coinmaw.extract import fetch_market_data
    try:
        raw_data = fetch_market_data()
    except Exception as e:
        print(f"There was an Error: {e}")

    assets, markets = transform_data(raw_data)

    print(f"Prepared {len(assets)} assets and {len(markets)} market records.")
    print(f"Sample asset: {assets[0]}")
    print(f"Sample asset: {markets[0]}") 
