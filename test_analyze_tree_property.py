import unittest
from unittest.mock import patch, mock_open
from pathlib import Path
from analyze_tree_property import TreePropertyAnalyzer

class TestTreePropertyAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.json_path = Path("test-dublin-trees.json")
        cls.csv_path = Path("test-dublin-property.csv")

    @patch("builtins.open", new_callable=mock_open, read_data="""{
        "short": {"drive": {"abbey drive": 0, "coolrua drive": 10}},
        "tall": {"gardens": {"temple gardens": 20}, "street": {"cork street": 10}}
    }""")
    @patch("pathlib.Path.exists", return_value=True)
    def test_load_tree_data(self, mock_exists, mock_file):
        analyzer = TreePropertyAnalyzer(self.json_path, self.csv_path)
        short_streets, tall_streets = analyzer.load_tree_data()
    
        self.assertEqual(short_streets, ["abbey drive", "coolrua drive"])
        self.assertEqual(tall_streets, ["temple gardens", "cork street"])

    @patch("builtins.open", new_callable=mock_open, read_data="""Street Name,Price
abbey drive,€100000
coolrua drive,€200000
temple gardens,€300000
cork street,€400000
unknown street,€500000""")
    @patch("pathlib.Path.exists", return_value=True)
    @patch("analyze_tree_property.TreePropertyAnalyzer.detect_file_encoding", return_value="utf-8")
    def test_load_property_data(self, mock_encoding, mock_exists, mock_file):
        analyzer = TreePropertyAnalyzer(self.json_path, self.csv_path)
        properties = analyzer.load_property_data()

        self.assertEqual(len(properties), 5)
        self.assertEqual(properties[0]["Street Name"], "abbey drive")
        self.assertEqual(properties[0]["Price"], "€100000")

    @patch("builtins.open", side_effect=[
        mock_open(read_data="""{
            "short": {"drive": {"abbey drive": 0, "coolrua drive": 10}},
            "tall": {"gardens": {"temple gardens": 20}, "street": {"cork street": 10}}
        }""").return_value,
        mock_open(read_data="""Street Name,Price
abbey drive,€100000
coolrua drive,€200000
temple gardens,€300000
cork street,€400000
unknown street,€500000""").return_value
    ])
    @patch("pathlib.Path.exists", return_value=True)
    @patch("analyze_tree_property.TreePropertyAnalyzer.detect_file_encoding", return_value="utf-8")
    def test_analyze(self, mock_encoding, mock_exists, mock_files):
        analyzer = TreePropertyAnalyzer(self.json_path, self.csv_path)
        results = analyzer.analyze()

        self.assertAlmostEqual(results["short_tree_avg"], 150000.0, places=2, msg="Short tree average is incorrect")
        self.assertAlmostEqual(results["tall_tree_avg"], 350000.0, places=2, msg="Tall tree average is incorrect")

if __name__ == "__main__":
    unittest.main()