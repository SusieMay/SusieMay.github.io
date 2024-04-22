from flask import Flask, request, jsonify, render_template
import csv
from datetime import datetime
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plot', methods=['POST'])
def generate_plot():
    print("Received request:", request.json)
    market_hash_names = request.json['market_hash_names']
    num_days = request.json['num_days']
    print("Market hash names:", market_hash_names)
    print("Number of days:", num_days)

    fig = go.Figure()

    for name in market_hash_names:
        filename = f"{name.replace('%20', '_')}.csv"
        dates = []
        prices = []

        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
                prices.append(float(row[1]))

        if dates:
            start_date = min(dates)
            days = [(date - start_date).days for date in dates]

            days = days[:num_days]
            prices = prices[:num_days]

            trace = go.Scatter(x=days, y=prices, mode='lines+markers', name=name)
            fig.add_trace(trace)
        else:
            print(f"No data found for {name}")

    fig.update_layout(
        xaxis_title="Days after release",
        yaxis_title="Price",
        hovermode="closest",
        width=800,
        height=600,
        margin=dict(l=50, r=50, t=50, b=50),
    )

    print("Generated figure:", fig)
    plot_data = fig.to_json()
    plot_layout = fig.layout.to_json()
    return jsonify({'plot_data': plot_data, 'plot_layout': plot_layout})

if __name__ == '__main__':
    app.run()