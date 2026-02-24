"""Tests for transform.py file."""

import unittest 
from coinmaw.transform import transform_data 

class TestJsonTransformer(unittest.TestCase):
    """
    Test that the transformer works as intended.
    Specially on data that can't be NULL.
    """
    def test_valid_data(self):
        """In this case, the coin data should be ADDED, and the lists would have length 1."""
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

    def test_invalid_data_missing_id(self):
        """In this case, the coin data should be SKIPPED, and the lists would be empty."""
        data = [{
            "id": None,
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 69476,
            "market_cap": 1384647777590,
            "total_volume": 45010501462,
            "captured_at": "2026-02-14T01:16:36.211777+00:00"
        }]

        assets, markets = transform_data(data)

        self.assertEqual(len(assets), 0)
        self.assertEqual(len(markets), 0)
        

    def test_invalid_data_missing_price(self):
        """In this case, the coin data should be ADDED, and price would be NULL/NONE."""
        data = [{
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": None,
            "market_cap": 1384647777590,
            "total_volume": 45010501462,
            "captured_at": "2026-02-14T01:16:36.211777+00:00"
        }]

        assets, markets = transform_data(data)

        self.assertIsNone(markets[0][1], None)

if __name__ == "__main__":
    unittest.main()