#importo pandas,numpy os e math
import pandas as pd,numpy,os,math
from matplotlib import pyplot as plt


#importo le prime 700 righe dal csv
#1.0 per importare le 700 righe, trasformo il csv in un dataframe
x1=pd.read_csv(filepath_or_buffer="TSLA.CSV",nrows=700)
df1=pd.DataFrame(x1)
#print(df1)

#1.2 uso la funzione display per mostrare il nuovo data frame che contiene solo le 700 righe.
#display ???__??? -> funziona sola nel notebook non nello script pyton 


#2.0 faccio il sommario del data frame di 700 righe, tramite la funzione describe.(accennata da luca, me la sono andata a vedere)
#esempio: sommario=df.describe() -> print(sommario)
sommario=df1.describe()
sommario2=df1.info()
#print(sommario)
#print(sommario2)

#3.0 uso la funzione isna() sul dataframe per vedere se ci sono nan -> restituisce true 
#esempio: check_nan=df.isna() -> print(check_nan)

n_a_n=df1.isna()
#print(n_a_n)

#3.1 uso la funzione sum() per sommare tutti i nan del dataframe \\\\[[[sum se fatta una sola volta somma i nan delle colonne,fatta due volte ci da i totali dei nan]]]
#esempio: somma_nan=df.isna().sum().sum()
somma_nan=df1.isna().sum().sum()
#print(somma_nan) ### -> ci da zero perchè gia sapevamo che il csv non aveva nan

#4.0 Verificare se il valore "high" è maggiore o uguale al valore di apertura e di chiusura
check_high=df1["High"]>=df1["Open"] 
check_close=df1["High"]>=df1["Close"]
#print(check_high)
#print(check_close)

#4.1 Verificare se il valore "low" è inferiore o uguale al valore di apertura e di chiusura
check_low=df1["Low"]<=df1["Open"]
check_low2=df1["Low"]<=df1["Close"]
#print(check_low)
#print(check_low2)
#4.2 Verificare se il valore "adj close" è inferiore o uguale al valore close
check_adjclose=df1["Adj Close"]<=df1["Close"]
#print(check_adjclose)

#5.0 faccio il plot con mathplotlib tutto su un grafico
# df1[["Open","High","Low","Close","Adj Close"]].plot()
# plt.show()

high=df1["High"]
open=df1["Open"]
low=df1["Low"]
close=["Close"]
adj=df1["Adj Close"]


plt.plot(high)
plt.show()





