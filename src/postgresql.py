
from sqlalchemy import create_engine ,MetaData, Table
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

# PostgreSQL connection details
PUBLIC_IP = "18.132.73.146"  # Replace with your PostgreSQL server IP
USERNAME = "Consultants"
PASSWORD = "WelcomeItc@2022"
DB_NAME = "testdb"
PORT = "5432"  # Default PostgreSQL port
ENCODED_PASSWORD = quote_plus(PASSWORD)

database1 = f"postgresql+psycopg2://{USERNAME}:{ENCODED_PASSWORD}@{PUBLIC_IP}:{PORT}/{DB_NAME}"

engine = create_engine(database1)

import pandas as pd
df = pd.read_sql("accounts1", con= engine)
print(df)

