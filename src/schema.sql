CREATE TABLE IF NOT EXISTS assets (
    id TEXT PRIMARY KEY,
    symbol TEXT NOT NULL,
    asset_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS market_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id TEXT NOT NULL,
    current_price REAL,
    market_cap INTEGER,
    trading_volume_24h INTEGER,
    captured_at TEXT,
    FOREIGN KEY (asset_id) REFERENCES assets(id) 
);