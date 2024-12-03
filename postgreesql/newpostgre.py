import sqlalchemy
from urllib.parse import quote_plus
from sqlalchemy import create_engine , text
from flask import Flask ,jsonify

app = Flask(__name__)

import pandas as pd

# PostgreSQL connection details
PUBLIC_IP = "18.132.73.146"  # Replace with your PostgreSQL server IP
USERNAME = "consultants"
PASSWORD = "WelcomeItc@2022"
DB_NAME = "testdb"
PORT = "5432"  # Default PostgreSQL port
ENCODED_PASSWORD = quote_plus(PASSWORD)

db_url = f"postgresql+psycopg2://{USERNAME}:{ENCODED_PASSWORD}@{PUBLIC_IP}:{PORT}/{DB_NAME}"

engine = create_engine(db_url)

try:
    with engine.connect() as connection:
        print("connection successful")
except Exception as e: 
    print("connection failed")

database1 = pd.read_sql("employee", con= engine)
print(database1)

df =database1.to_dict(orient='records')

@app.route('/', methods=['GET'])
def get_data():
    data = df
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "Unable to fetch data from database"}), 500

if __name__ == '__main__':
    # Run the app
  app.run(host='0.0.0.0', port=5310, debug=True)


  # its working
