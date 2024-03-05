# S&P 500 Dashboard

This is a simple Dash app that allows you to compare the cumulative percent change of a stock against the S&P 500 index over a specified time period.

### Installation

1. Clone the repository:

git clone https://github.com/pku118/Project-3


2. Navigate to the project directory:

cd stock-cumulative-percent-change


3. Install the required dependencies:


pip install -r requirements.txt


# Usage
1. Run the Dash app:

python app.py & app2.py


2. Open your web browser and go to http://localhost:8050/ to access the app.

3. Enter the stock symbol, start date, end date, and select a time frame (1 Month, 6 Months, 1 Year, 3 Years, 5 Years) to visualize the cumulative percent change of the stock compared to the S&P 500.

# Features
    - Input fields for stock symbol, start date, end date, and time frame selection.
    - Interactive plot using Plotly to display the cumulative percent change.
    - Data is fetched from an SQLite database (data/sp500_data.db).

Dependencies
    - Dash: https://dash.plotly.com
    - Plotly: https://plotly.com/python
    - Pandas: https://pandas.pydata.org
    - SQLite3: https://docs.python.org/3/library/sqlite3.html
