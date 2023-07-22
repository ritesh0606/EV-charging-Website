from flask import Flask, render_template, request

app = Flask(__name__)

# Sample EV charging stations data (you can replace this with a real data source)
charging_stations = [
    {"name": "Charging Station 1", "location": "Location 1"},
    {"name": "Charging Station 2", "location": "Location 2"},
    # Add more charging station data as needed
]

@app.route('/')
def index():
    return render_template('index.html', charging_stations=charging_stations)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    answer = request.form['answer']
    # Process the answer or do whatever you want with it
    return f"Your answer: {answer}"

if __name__ == '__main__':
    app.run(debug=True)
