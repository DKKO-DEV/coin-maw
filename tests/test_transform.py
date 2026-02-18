"""Tests for transform.py file."""

import unittest
from src.coinmaw.transform import transform_data

class TestJsonTransformer(unittest.TestCase):
    """
    Test that the transformer works as intended.
    Specially on data that can't be NULL.
    """
    def test_valid_data(self):
        data = [{
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 69476,
            "market_cap": 1384647777590,
            "total_volume": 45010501462,
            "captured_at": "2026-02-14T01:16:36.211777+00:00"
        }]

        assets, markets = transform_data(data)

        self.assertEqual(len(assets), 1)
        self.assertEqual(len(markets), 1)


if __name__ == "__main__":
    unittest.main()