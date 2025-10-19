import datetime as dt
import pandas as pd
from pathlib import Path


dTime=dt.datetime(2025,10,5);

print(dt.datetime.now())
print(dt.datetime.now().strftime('%d-%m-%y'))

#changed_tz=dt.datetime.now().astimezone(tz='US/Arizona')
file_path=Path("../Content")/"BikeIndia.csv"
df=pd.read_csv(file_path)

print(df.describe())
print(df.head())
