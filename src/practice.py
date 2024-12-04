import sqlalchemy
from sqlalchemy import create_engine, text
from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Configure database
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://consultants:WelcomeItc%402022@18.132.73.146:5432/testdb"
)
engine = create_engine(DATABASE_URL)

# Fetch data
def fetch_data():
    try:
        database1 = pd.read_sql("SELECT * FROM employee", con=engine)
        return database1.to_dict(orient="records")
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

@app.route('/get_data', methods=['GET'])
def get_data():
    # Call fetch_data dynamically
    data = fetch_data()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Unable to fetch data from database"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5232, debug=True)
