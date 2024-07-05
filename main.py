#RICHIESTA 1

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
df1[['High','Open','Low','Close', 'Adj Close']].plot()
plt.title('TSLA Stock Trend')
plt.xlabel('Non lo so')
plt.ylabel('Prezzo')
plt.show()

#RICHIESTA 2
#1.0 Creo un funzione per calcolare la formula -> ADTV[i] = (Volume[i] + Volume[i-1] + Volume[i-2] + Volume[i-3] + Volume[i-4])/5
def calcola_adtv():
    adtv=[]
    for i in range(len(df1)):
        adtv_value = (df1['Volume'].iloc[i] + df1['Volume'].iloc[i-1] + df1['Volume'].iloc[i-2] + df1['Volume'].iloc[i-3] + df1['Volume'].iloc[i-4]) / 5
        #qui in teoria faccio il punto in cui converto in intero direttamente nella funzione
        adtv_int=int(adtv_value)
        adtv.append(adtv_int)
    df1["ADTV"]= adtv
    
calcola_adtv()
print(df1)

#2.0 Creo una funzione per calcolare la deviazione standard ->ADTV_std[i] = ((Volume[i]-ADTV[i])**2 + (Volume[i-1]-ADTV[i])**2 + (Volume[i-1]-ADTV[i])**2 +
#                                                                           + (Volume[i-1]-ADTV[i])**2 + Volume[i-1]-ADTV[i])**2)/5

def deviazione_adtv():
    dev_adtv=[]
    for i in range(len(df1)):
        dev_value_adtv=((df1['Volume'].iloc[i]- df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-1]- df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-2]- df1['ADTV'].iloc[i])**2+ (df1['Volume'].iloc[i-3]- df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-4]- df1['ADTV'].iloc[i])**2)/5
        dev_value_adtv_int=int(dev_value_adtv)
        dev_adtv.append(dev_value_adtv_int)
    df1["ADTV std"] = dev_adtv
    
deviazione_adtv()
print(df1)

df1[['ADTV','ADTV std']].plot()
plt.title('ADTV + ADTV std')
plt.xlabel('Non lo so')
plt.ylabel('Prezzo')
plt.show()

###perchè esce solo adtv std?????????????????????                  

