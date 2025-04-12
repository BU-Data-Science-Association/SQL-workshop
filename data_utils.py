import pandas as pd
from sqlalchemy import create_engine

warren = pd.read_csv("/workspace/Warren.csv")
warren_calories = pd.read_csv("/workspace/Warren_calories.csv")
west = pd.read_csv("/workspace/West.csv")
west_calories = pd.read_csv("/workspace/West_calories.csv")
marciano= pd.read_csv("/workspace/Marciano.csv")
marciano_calories = pd.read_csv("/workspace/Marciano_calories.csv")
granby = pd.read_csv("/workspace/Granby.csv")
granby_calories = pd.read_csv("/workspace/Granby_calories.csv")


engine = create_engine("postgresql://app_user:app_password@localhost:5432/app")  # adjust accordingly
warren.to_sql("Warren", engine, if_exists="replace", index=False)
warren_calories.to_sql("Warren_Calories", engine, if_exists="replace", index=False)
west.to_sql("West", engine, if_exists="replace", index=False)
west_calories.to_sql("West_Calories", engine, if_exists="replace", index=False)
marciano.to_sql("Marciano", engine, if_exists="replace", index=False)
marciano_calories.to_sql("Marciano_Calories", engine, if_exists="replace", index=False)
granby.to_sql("Granby", engine, if_exists="replace", index=False)
granby_calories.to_sql("Granby_Common", engine, if_exists="replace", index=False)

print("Data should be loaded into Postgres")