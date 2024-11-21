import json
import csv
from pathlib import Path
from statistics import mean
from typing import Dict, List, Tuple


class TreePropertyAnalyzer:
    def __init__(self, json_path: Path, csv_path: Path):
        self.json_path = json_path
        self.csv_path = csv_path

    def load_tree_data(self) -> Tuple[List[str], List[str]]:
        """Parse the JSON and extract lists of short and tall streets."""
        if not self.json_path.exists():
            raise FileNotFoundError(f"Tree data file not found: {self.json_path}")

        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        def extract_street_names(tree: Dict) -> List[str]:
            """Recursively extract street names."""
            streets = []
            for key, value in tree.items():
                if isinstance(value, dict):
                    streets.extend(extract_street_names(value))
                else:
                    streets.append(key.strip().lower())  # Normalize names
            return streets

        short_streets = extract_street_names(data.get("short", {}))
        tall_streets = extract_street_names(data.get("tall", {}))
        print(f"DEBUG: Loaded short streets: {short_streets}")
        print(f"DEBUG: Loaded tall streets: {tall_streets}")
        return short_streets, tall_streets

    @staticmethod
    def detect_file_encoding(file_path: Path) -> str:
        """Detect file encoding for CSV files."""
        import chardet
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result.get('encoding', 'utf-8')
        print(f"DEBUG: Detected encoding for {file_path}: {encoding}")
        return encoding

    def load_property_data(self) -> List[Dict]:
        """Load property data from a CSV file."""
        if not self.csv_path.exists():
            raise FileNotFoundError(f"Property data file not found: {self.csv_path}")

        encoding = self.detect_file_encoding(self.csv_path)

        with open(self.csv_path, 'r', encoding=encoding) as f:
            reader = csv.DictReader(f)
            properties = list(reader)
            for prop in properties:
                print(f"DEBUG: Raw property data: {prop}")
            return properties

    @staticmethod
    def categorize_properties(properties: List[Dict], short_streets: List[str], tall_streets: List[str]) -> Tuple[List[float], List[float]]:
        """Categorize property prices by street type."""
        short_prices = []
        tall_prices = []

        for prop in properties:
            street_name = prop.get("Street Name", "").strip().lower()
            price_raw = prop.get("Price", "0")  # Extract raw price
            try:
                # Normalize price: replace malformed symbol and clean up
                normalized_price = price_raw.replace("", "").replace("€", "").replace(",", "").strip()
                price = float(normalized_price)

                if price <= 0:
                    print(f"DEBUG: Skipping property with invalid or zero price: {price_raw}")
                    continue

                print(f"DEBUG: Parsed price for {street_name}: {price} (raw: {price_raw})")

                if street_name in short_streets:
                    print(f"Matched short street: {street_name} with price: {price}")
                    short_prices.append(price)
                elif street_name in tall_streets:
                    print(f"Matched tall street: {street_name} with price: {price}")
                    tall_prices.append(price)
                else:
                    print(f"Street not matched: {street_name}")
            except ValueError:
                print(f"ERROR: Could not parse price for {street_name}: {price_raw}")
                continue

        return short_prices, tall_prices

    @staticmethod
    def calculate_average(prices: List[float]) -> float:
        """Calculate the average price."""
        if not prices:  # Handle empty lists explicitly
            print("DEBUG: No prices available for this category.")
            return 0.0
        avg = mean(prices)
        print(f"DEBUG: Calculated average: {avg}")
        return avg

    def analyze(self) -> Dict[str, float]:
        """Run the full analysis."""
        short_streets, tall_streets = self.load_tree_data()
        properties = self.load_property_data()
        short_prices, tall_prices = self.categorize_properties(properties, short_streets, tall_streets)
        short_tree_avg = self.calculate_average(short_prices)
        tall_tree_avg = self.calculate_average(tall_prices)
        return {
            "short_tree_avg": short_tree_avg,
            "tall_tree_avg": tall_tree_avg
        }


if __name__ == "__main__":
    # Define paths to JSON and CSV files
    json_file_path = Path("dublin-trees.json")
    csv_file_path = Path("dublin-property.csv")

    # Create an instance of TreePropertyAnalyzer
    analyzer = TreePropertyAnalyzer(json_path=json_file_path, csv_path=csv_file_path)

    # Run the analysis
    try:
        results = analyzer.analyze()
        print(f"Average property price on streets with short trees: €{results['short_tree_avg']:.2f}")
        print(f"Average property price on streets with tall trees: €{results['tall_tree_avg']:.2f}")
    except Exception as e:
        print(f"Error during analysis: {e}")
