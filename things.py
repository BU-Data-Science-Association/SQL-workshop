import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("/workspace/Warren.csv")

engine = create_engine("postgresql://app_user:app_password@localhost:5432/app")  # adjust accordingly
df.to_sql("Warren2", engine, if_exists="append", index=False)
print(df)