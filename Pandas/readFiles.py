import pandas as pd

#pd.options.display.max_columns=999
df=pd.read_csv('C:\Learning\Logicmojo-AI-ML-Sept25-mail4mukund\Content\BikeIndia.csv')
#print(df['temp'])
#df.fillna({'dteday':'25/10/1984'},inplace=True) #If we do inplace=true then orginal dataframe got changed
#print(df.describe(include='all'))
#print(df)
#print(df['dteday'].mode(dropna=False))

print(df.head())
# print(df.info())
#print(type(df.head()))
#print(df.info())
#print(type(df.columns))
#print(df[df["windspeed"]>10])

# dfPivot=df.pivot_table(values='temp', columns='season', aggfunc='mean')
# print(dfPivot)
# dfUnique= df['temp'].unique();
# print(dfUnique)

# print(df.describe())
# print(df.info())
print(df.shape)
print(df.loc[1,"temp, hum"])