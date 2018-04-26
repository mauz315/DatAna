
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()

df = web.DataReader("FCAU", "morningstar", start, end)

#print(df)
#print(df.head())

df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())   

df['Close'].plot()
plt.legend()
plt.show()