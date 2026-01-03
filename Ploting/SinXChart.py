import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('Content\BikeIndia.csv')
print(df.columns)
x=np.linspace(0,10,100)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.title('Sin X Values')
plt.show()

