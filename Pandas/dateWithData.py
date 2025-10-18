import datetime as dt
import pandas as pd


dTime=dt.datetime(2025,10,5);

print(dt.datetime.now())
print(dt.datetime.now().strftime('%d-%m-%y'))

#changed_tz=dt.datetime.now().astimezone(tz='US/Arizona')

pd.read_csv('..\Content\BikeIndia.csv')

df=pd.DataFrame()
df.describe()