Tree Property Price Analyzer
Overview
This project analyzes property prices based on streets with short and tall trees. Using JSON and CSV files, it calculates the average property price for each street type, providing insights into whether tree density correlates with property value.

Features
Dynamic Data Analysis: Processes data from JSON and CSV files to categorize streets and calculate averages.
Customizable: Easily replace input files to analyze different datasets.
Unit-Tested: Comprehensive tests ensure reliability and accuracy.
Project Structure
python
Copy code
pythonProjectTree/
├── analyze_tree_property.py       # Main program file
├── test_analyze_tree_property.py  # Unit tests
├── dublin-trees.json              # JSON file with street data
├── dublin-property.csv            # CSV file with property prices
├── test-dublin-trees.json         # Test JSON file for unit tests
├── test-dublin-property.csv       # Test CSV file for unit tests
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
Setup Instructions
Install Python:

Ensure Python 3.8+ is installed. Verify with:
bash
Copy code
python --version
Clone the Repository:

bash
Copy code
git clone https://github.com/P3st83/Projecttree.git
cd Projecttree
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Program
Execute the Analysis:

bash
Copy code
python analyze_tree_property.py
This will calculate and display average property prices for streets with short and tall trees.

Sample Output:

vb net
Copy code
Average property price on streets with short trees: €488981.66
Average property price on streets with tall trees: €587800.39
Running Unit Tests
To validate the functionality, run the unit tests:

bash
Copy code
python -m unittest test_analyze_tree_property.py
Files
analyze_tree_property.py: The main script that analyzes property prices.
test_analyze_tree_property.py: Unit tests for the script.
dublin-trees.json: Input file containing categorized tree data.
dublin-property.csv: Input file with property prices and street names.
test-dublin-trees.json: Mock JSON data for testing.
test-dublin-property.csv: Mock CSV data for testing.
Dependencies
The project uses the following Python libraries:

json (Built-in)
csv (Built-in)
unittest (Built-in)
pathlib (Built-in)
statistics
chardet
Install them using:

bash
Copy code
pip install -r requirements.txt
Contribution Guidelines
Fork the repository.
Create a new branch for your feature:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add feature-name"
Push to your branch:
bash
Copy code
git push origin feature-name
Create a pull request.
License
This project is licensed under the MIT License. See LICENSE for more details.

This updated README ensures clarity, professionalism, and ease of use for developers and users alike. Let me know if you'd like any additional changes!