#RICHIESTA 1

#importo pandas, os 
import pandas as pd,os
from matplotlib import pyplot as plt
import function
import numpy as np

#importo le prime 700 righe dal csv
#1.0 per importare le 700 righe, trasformo il csv in un dataframe
x1=pd.read_csv(filepath_or_buffer="TSLA.CSV",nrows=700)
df1=pd.DataFrame(x1)

fig, ax = plt.subplots(figsize = (9, 7))
ax.plot(df1["Date"],df1["Open"], linewidth = 1, label = 'Open')
ax.plot(df1["Date"],df1["High"], linewidth = 1, label = 'Open')
ax.plot(df1["Date"],df1["Low"], linewidth = 1, label = 'Open')
ax.plot(df1["Date"],df1["Close"], linewidth = 1, label = 'Open')
ax.plot(df1["Date"],df1["Adj Close"], linewidth = 1, label = 'Open')

ax.set_title('TSLA stock trend')
ax.set_xlabel('Date')
ax.set_xlim(0, 700) 
ax.set_ylabel('Price')

start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 100))
ax.set_xticklabels(df1.iloc[function.build_xticklabels(df1['Date'],0,700,100) , 0], rotation = 45)
ax.legend()
plt.show()