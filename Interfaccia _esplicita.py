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

df1 = function.calcola_adtv(df1,nGiorni = 2)
df1 = function.calcola_adtv_std(df1,nGiorni = 2)

df1 = function.calcola_adtv(df1,nGiorni = 5)
df1 = function.calcola_adtv_std(df1,nGiorni = 5)

df1 = function.calcola_adtv(df1,nGiorni = 10)
df1 = function.calcola_adtv_std(df1,nGiorni = 10)

df1 = function.calcola_adtv(df1,nGiorni = 20)
df1 = function.calcola_adtv_std(df1,nGiorni = 20)

df1 = function.calcola_adtv(df1,nGiorni = 50)
df1 = function.calcola_adtv_std(df1,nGiorni = 50)


fig, ax = plt.subplots(figsize = (9, 7))
ax.plot(df1["Date"],df1["ADTV 2"], linewidth = 1, label = 'ADTV 2 GIORNI')
ax.plot(df1["Date"],df1["ADTV Std 2"], linewidth = 1, label = 'ADTV Std 2 GIORNI')

ax.plot(df1["Date"],df1["ADTV 5"], linewidth = 1, label = 'ADTV 5 GIORNI')
ax.plot(df1["Date"],df1["ADTV Std 5"], linewidth = 1, label = 'ADTV Std 5 GIORNI')

ax.plot(df1["Date"],df1["ADTV 10"], linewidth = 1, label = 'ADTV 10 GIORNI')
ax.plot(df1["Date"],df1["ADTV Std 10"], linewidth = 1, label = 'ADTV Std 10 GIORNI')

ax.plot(df1["Date"],df1["ADTV 20"], linewidth = 1, label = 'ADTV 20 GIORNI')
ax.plot(df1["Date"],df1["ADTV Std 20"], linewidth = 1, label = 'ADTV Std 20 GIORNI')

ax.plot(df1["Date"],df1["ADTV 50"], linewidth = 1, label = 'ADTV 50 GIORNI')
ax.plot(df1["Date"],df1["ADTV Std 50"], linewidth = 1, label = 'ADTV Std 50 GIORNI')

ax.set_title('TSLA stock trend')
ax.set_xlabel('Date')
ax.set_xlim(0, 700) 
ax.set_ylabel('Price')

start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 100))
ax.set_xticklabels(df1.iloc[function.build_xticklabels(df1['Date'],0,700,100) , 0], rotation = 45)
ax.legend()
plt.show()