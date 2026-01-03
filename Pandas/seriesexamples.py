import pandas as pd

ar=['Mukund', 'Chandan', 'Ritesh','Prahlad']
sr=pd.Series(ar)
sr=pd.Series(ar,index=[1,2,3,4])
print(sr)

print(pd.Series([2,'Mukund','kumar']))