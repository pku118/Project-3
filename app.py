import json
import numpy as np
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def chart():
    labels = ["January", "February", "March", "April", "May", "June", "July"]
    stock_data = {
        "label": "Stock Data",
        "data": [],
        "fill": False,
        "borderColor": "rgb(255, 99, 132)",
        "lineTension": 0.1
    }
    sp500_data = {
        "label": "S&P 500 Data",
        "data": [],
        "fill": False,
        "borderColor": "rgb(75, 192, 192)",
        "lineTension": 0.1
    }

    for i in range(len(labels)):
        stock_data["data"].append(np.random.rand())
        sp500_data["data"].append(np.random.rand())

    chart_data = json.dumps({
        "labels": labels,
        "datasets": [stock_data, sp500_data]
    })

    return render_template_string("""
    <html>
        <head>
            <title>Stock Data and S&P 500 Data</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        </head>
        <body>
            <canvas id="myChart"></canvas>
            <script>
                var ctx = document.getElementById('myChart').getContext('2d');
                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {{ chart_data }}
                });
            </script>
        </body>
    </html>
    """, chart_data=chart_data)

if __name__ == "__main__":
    app.run(debug=True)