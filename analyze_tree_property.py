# File: analyze_tree_property.py

import json
import csv
from pathlib import Path
from statistics import mean
from typing import Dict, List, Tuple, Optional


class TreePropertyAnalyzer:
    def __init__(self, json_path: str, csv_path: str):
        self.json_path = Path(json_path)
        self.csv_path = Path(csv_path)

    def load_tree_data(self) -> Tuple[List[str], List[str]]:
        """Parse the JSON and extract lists of short and tall streets."""
        if not self.json_path.exists():
            raise FileNotFoundError(f"Tree data file not found: {self.json_path}")

        with open(self.json_path, 'r') as f:
            data = json.load(f)

        def extract_street_names(tree: Dict) -> List[str]:
            """Recursively extract street names."""
            streets = []
            for key, value in tree.items():
                if isinstance(value, dict):
                    streets.extend(extract_street_names(value))
                else:
                    streets.append(key)
            return streets

        return (
            extract_street_names(data.get("short", {})),
            extract_street_names(data.get("tall", {}))
        )

    def load_property_data(self) -> List[Dict]:
        """Load property data from a CSV file."""
        if not self.csv_path.exists():
            raise FileNotFoundError(f"Property data file not found: {self.csv_path}")

        with open(self.csv_path, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def categorize_properties(self, properties: List[Dict], short_streets: List[str], tall_streets: List[str]) -> Tuple[List[float], List[float]]:
        """Categorize property prices by street type."""
        short_prices = []
        tall_prices = []
        for property in properties:
            street_name = property.get("Street Name", "").strip()
            try:
                price = float(property.get("Price (Euro)", "0").replace(",", "").strip())
                if street_name in short_streets:
                    short_prices.append(price)
                elif street_name in tall_streets:
                    tall_prices.append(price)
            except ValueError:
                continue  # Skip malformed prices
        return short_prices, tall_prices

    def calculate_average(self, prices: List[float]) -> Optional[float]:
        """Calculate the average price."""
        return mean(prices) if prices else None

    def analyze(self):
        """Main analysis function."""
        short_streets, tall_streets = self.load_tree_data()
        properties = self.load_property_data()
        short_prices, tall_prices = self.categorize_properties(properties, short_streets, tall_streets)

        short_avg = self.calculate_average(short_prices)
        tall_avg = self.calculate_average(tall_prices)

        return {
            "short_tree_avg": short_avg,
            "tall_tree_avg": tall_avg,
        }


if __name__ == "__main__":
    analyzer = TreePropertyAnalyzer("dublin-trees.json", "dublin-property.csv")
    results = analyzer.analyze()
    print(f"Average property price on streets with short trees: €{results['short_tree_avg']:.2f}")
    print(f"Average property price on streets with tall trees: €{results['tall_tree_avg']:.2f}")
