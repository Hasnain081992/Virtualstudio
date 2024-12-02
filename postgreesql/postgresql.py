
from urllib.parse import quote_plus
from sqlalchemy import create_engine , text

import pandas as pd

# PostgreSQL connection details
PUBLIC_IP = "18.132.73.146"  # Replace with your PostgreSQL server IP
USERNAME = "Consultants"
PASSWORD = "WelcomeItc@2022"
DB_NAME = "testdb"
PORT = "5432"  # Default PostgreSQL port
ENCODED_PASSWORD = quote_plus(PASSWORD)

db_url = f"postgresql+psycopg2://{USERNAME}:{ENCODED_PASSWORD}@{PUBLIC_IP}:{PORT}/{DB_NAME}"

engine = create_engine(db_url)

database1 = pd.read_sql("employee", con= engine)
print(database1)