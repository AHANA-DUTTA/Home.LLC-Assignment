import pandas as pd
from sqlalchemy import create_engine


# MySQL credentials and engine setup
MYSQL_USER = 'db_user'
MYSQL_PASS = '6equj5_db_user'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DB   = 'home_db'

engine = create_engine(f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}")
print("Connection Established...")

properties_df = pd.read_sql_query("""SELECT * FROM properties""", con=engine)
valuation_df = pd.read_sql_query("""SELECT * FROM valuations""", con=engine)
hoa_df = pd.read_sql_query("""SELECT * FROM hoa""", con=engine)
rehab_df = pd.read_sql_query("""SELECT * FROM rehab""", con=engine)

properties_df.drop('id',axis=1, inplace=True)
valuation_df.drop('id',axis=1, inplace=True)
hoa_df.drop('id',axis=1, inplace=True)
rehab_df.drop('id',axis=1, inplace=True)

df1 = pd.merge(properties_df, valuation_df, on='property_title', how='inner')
df2 = pd.merge(df1, hoa_df, on='property_title', how='inner')
joined_df = pd.merge(df2, rehab_df, on='property_title', how='inner')

# Set custom ID
joined_df['id'] = joined_df.index + 1

# Reorder columns to match DB schema
joined_df.set_index('id', inplace=True)

joined_df.to_sql(
    name='final_properties',         # Target table name
    con=engine,           # SQLAlchemy engine
    if_exists='append',   
    index=False          
)

print("Data is loaded to Target table")
