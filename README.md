Tree Property Price Analyzer
Overview
This project analyzes property prices on streets categorized by tree types (short or tall). Using data from JSON and CSV files, the program calculates and displays the average property prices for each category.

The repository includes:

Main code for performing the analysis.
Unit tests to validate the program's functionality.
Mock files for testing.
Instructions for setup and usage.
Features
Tree Categorization: Parses a JSON file to extract streets with short and tall trees.
Property Data Analysis: Parses a CSV file containing property price data.
Street Matching: Matches property streets with tree categories (short or tall).
Average Calculation: Calculates the average property prices for streets in both categories.
Unit Testing: Ensures program correctness with mock data.
File Structure
graphql
Copy code
.
├── analyze_tree_property.py       # Main program script
├── test_analyze_tree_property.py  # Unit test script
├── dublin-trees.json              # JSON file containing tree categorization
├── dublin-property.csv            # CSV file containing property price data
├── test-dublin-trees.json         # Mock JSON file for tests
├── test-dublin-property.csv       # Mock CSV file for tests
├── README.md                      # Project documentation
└── .gitignore                     # Files and directories to ignore in version control
Prerequisites
Python: Version 3.8 or higher.
Virtual Environment: Recommended for dependency isolation.
Setup Instructions
Clone the Repository:

bash
Copy code
git clone https://github.com/P3st83/Projecttree.git
cd Projecttree
Create and Activate a Virtual Environment:

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate  # On Linux/Mac
.venv\Scripts\activate     # On Windows
Install Dependencies: Ensure all required dependencies are installed using:

bash
Copy code
pip install -r requirements.txt
Verify Setup: Run unit tests to ensure the setup is correct:

bash
Copy code
python -m unittest test_analyze_tree_property.py
Usage Instructions
To calculate average property prices for streets with short and tall trees, run the following command:

bash
Copy code
python analyze_tree_property.py
Example Output
plaintext
Copy code
DEBUG: Loaded short streets: ['abbey drive', 'coolrua drive']
DEBUG: Loaded tall streets: ['temple gardens', 'cork street']
DEBUG: Parsed price for abbey drive: 100000.0
Matched short street: abbey drive with price: 100000.0
DEBUG: Parsed price for coolrua drive: 200000.0
Matched short street: coolrua drive with price: 200000.0
DEBUG: Parsed price for temple gardens: 300000.0
Matched tall street: temple gardens with price: 300000.0
...
Average property price on streets with short trees: €150000.00
Average property price on streets with tall trees: €350000.00
Running Unit Tests
Unit tests ensure the program behaves as expected with mock data. Run the tests using:

bash
Copy code
python -m unittest test_analyze_tree_property.py
Example Test Output
plaintext
Copy code
DEBUG: Loaded short streets: ['abbey drive', 'coolrua drive']
DEBUG: Loaded tall streets: ['temple gardens', 'cork street']
...
----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK
Known Issues and Limitations
Property prices in the CSV file must be in the format €<amount> (e.g., €100000). Invalid formats will result in skipped entries.
Ensure the JSON and CSV files are correctly structured as shown in the mock files.
Contributing
Contributions are welcome! If you have suggestions or want to contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

This version ensures clarity, provides an overview, and guides users step-by-step. Let me know if you’d like further refinements!
