#RICHIESTA 1

#importo pandas, os 
import pandas as pd
from matplotlib import pyplot as plt
import function
import numpy as np
import start_logger as lg

logger=lg.percorso_log("my_logger","app.log",level=lg.logging.DEBUG)
logger.debug("Importo le prime 700 righe del csv")

#importo le prime 700 righe dal csv
#1.0 per importare le 700 righe, trasformo il csv in un dataframe  
x1=pd.read_csv(filepath_or_buffer="TSLA.CSV",nrows=700)
df1=pd.DataFrame(x1)

# # #1.2 uso la funzione display per mostrare il nuovo data frame che contiene solo le 700 righe.
# # #display ???__??? -> funziona sola nel notebook non nello script pyton 

# #2.0 faccio il sommario del data frame di 700 righe, tramite la funzione describe
sommario=df1.describe()
# sommario2=df1.info()


# # #3.0 uso la funzione isna() sul dataframe per vedere se ci sono nan -> restituisce true 
logger.debug("uso la funzione isna() sul dataframe per vedere se ci sono nan")
n_a_n=df1.isna()


# # #3.1 uso la funzione sum() per sommare tutti i nan del dataframe ->
logger.debug("uso la funzione sum() per sommare tutti i nan del dataframe")
somma_nan=df1.isna().sum().sum()


# # #4.0 Verificare se il valore "high" è maggiore o uguale al valore di apertura e di chiusura
logger.debug("Verifico se il valore di high è maggiore o uguale al valore di apertura e di chiusura ")
check_high=df1["High"]>=df1["Open"] 
check_close=df1["High"]>=df1["Close"]


# # #4.1 Verificare se il valore "low" è inferiore o uguale al valore di apertura e di chiusura
logger.debug("Verifico se il valore di low è inferiore o uguale al valore di apertura e di chiusura ")
check_low=df1["Low"]<=df1["Open"]
check_low2=df1["Low"]<=df1["Close"]


# # #4.2 Verificare se il valore "adj close" è inferiore o uguale al valore close 
logger.debug("Verifico se il valore di adj close è inferiore o uguale al valore di close ")
check_adjclose=df1["Adj Close"]<=df1["Close"]


# # #5.0 faccio il plot con mathplotlib tutto su un grafico
# plt.plot(df1["Date"],df1['High'])
# plt.plot(df1["Date"],df1['Open'])
# plt.plot(df1["Date"],df1['Low'])
# plt.plot(df1["Date"],df1['Close'])
# plt.plot(df1["Date"],df1['Adj Close'])
plt.plot(df1["Date"],df1["High"],df1["Date"],df1["Open"],df1["Date"],df1["Low"],df1["Date"],df1["Close"],df1["Date"],df1["Adj Close"])
plt.title('TSLA Stock Trend')
plt.xticks(np.arange(0, 699, 50),rotation=45)
plt.xlabel('Data')
plt.ylabel('Prezzo')
plt.legend(["High","Open","Low","Close","Adj Close"])
plt.show()

# # #RICHIESTA 2 + RICHIESTA 3 

# # #1.0 Creata una libreria con tutte le funzioni chiamata function.py
logger.debug("Creo una libreria per tutte le funzioni ")
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

#print(df1)

plt.plot(df1['Date'],df1['ADTV 2'],label="ADTV 2 GIORNI")
plt.plot(df1['Date'],df1['ADTV Std 2'],label="ADTV STD 2 GIORNI")

plt.plot(df1['Date'],df1['ADTV 5'],label="ADTV 5 GIORNI")
plt.plot(df1['Date'],df1['ADTV Std 5'],label="ADTV STD 5 GIORNI")

plt.plot(df1['Date'],df1['ADTV 10'],label="ADTV 10 GIORNI")
plt.plot(df1['Date'],df1['ADTV Std 10'],label="ADTV STD 10 GIORNI")

plt.plot(df1['Date'],df1['ADTV 20'],label="ADTV 20 GIORNI")
plt.plot(df1['Date'],df1['ADTV Std 20'],label="ADTV STD 20 GIORNI")

plt.plot(df1['Date'],df1['ADTV 50'],label="ADTV 50 GIORNI")
plt.plot(df1['Date'],df1['ADTV Std 50'],label="ADTV STD 50 GIORNI")

plt.title('ADTV for different days')
plt.xticks(np.arange(0, 699, 100),rotation=45)
plt.legend()
plt.xlabel('Date')
plt.ylabel('ADTV')
plt.show()

#Implemento la funzione fill_between()
logger.debug("implemento la funzione fill_between()")
x=df1["Date"]
y=df1["ADTV 2"]
delta=df1["ADTV Std 2"]

plt.plot(df1["Date"],df1["ADTV 5"])
plt.fill_between(x,y-delta,y+delta,facecolor="C0",alpha=0.4)
plt.xlim(0,700)
plt.xticks(np.arange(0,700,200))
plt.show()

#Istogramma
logger.debug("Aggiungo l'istogramma")
fig, ax = plt.subplots(figsize=(9, 7))
ax.hist(df1["ADTV 5"],color='C0', bins = 50)
ax.hist(df1["ADTV Std 5"],color='C1', bins = 50)
ax.set_title('Istogramma')
ax.set_xlabel('ADTV 5')
ax.set_ylabel('ADTV Std 5')
ax.grid()
fig.tight_layout()
plt.show()

#RICHIESTA 4
#1.0 droppo tutte le colonne "ADTV" e "ADTV std"
logger.debug("droppo tutte le colonne ADTV e ADTV std")
df1=df1.drop(columns=["ADTV 2","ADTV Std 2",
                      "ADTV 5","ADTV Std 5",
                      "ADTV 10","ADTV Std 10",
                      "ADTV 20","ADTV Std 20",
                      "ADTV 50","ADTV Std 50"],axis="columns")

#2.0 aggiungo "ADTV" e "ADTV std" per la media di 10 giorni
logger.debug("aggiungo ADTV e ADTV Std per la media di 10 giorni")
df2=function.calcola_media_10_giorni(df1,nGiorni=10)
df2=pd.DataFrame(df1)
#print(df2)

# #RICHIESTA 5
logger.debug("creata la funzione per salvare il csv")
# #Creo la directory "Output_data" nel percorso di dove si trova il progetto e
# #salvo il data frame aggiornato sottoforma di csv chiamato 'Modified_TSLA.csv'
# #quindi sarebbe il data frame ultimo di richiesta 4.(volevo si possono salvare anche gli altri)

function.save_csv(df2)

df1=df1.drop(columns=["ADTV 10","ADTV Std 10","Date"])

function.correlazioni('Open',df1)

