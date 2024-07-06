#RICHIESTA 1

#importo pandas,numpy os e math
import pandas as pd,numpy,os,math
from matplotlib import pyplot as plt
import copy

#importo le prime 700 righe dal csv
#1.0 per importare le 700 righe, trasformo il csv in un dataframe
x1=pd.read_csv(filepath_or_buffer="TSLA.CSV",nrows=700)
df1=pd.DataFrame(x1)
#print(df1)

# #1.2 uso la funzione display per mostrare il nuovo data frame che contiene solo le 700 righe.
# #display ???__??? -> funziona sola nel notebook non nello script pyton 


#2.0 faccio il sommario del data frame di 700 righe, tramite la funzione describe.(accennata da luca, me la sono andata a vedere)
#esempio: sommario=df.describe() -> print(sommario)
sommario=df1.describe()
sommario2=df1.info()
#print(sommario)
#print(sommario2)

# #3.0 uso la funzione isna() sul dataframe per vedere se ci sono nan -> restituisce true 
# #esempio: check_nan=df.isna() -> print(check_nan)
n_a_n=df1.isna()
#print(n_a_n)

# #3.1 uso la funzione sum() per sommare tutti i nan del dataframe \\\\[[[sum se fatta una sola volta somma i nan delle colonne,fatta due volte ci da i totali dei nan]]]
# #esempio: somma_nan=df.isna().sum().sum()
somma_nan=df1.isna().sum().sum()
# #print(somma_nan) ### -> ci da zero perchè gia sapevamo che il csv non aveva nan

# #4.0 Verificare se il valore "high" è maggiore o uguale al valore di apertura e di chiusura
check_high=df1["High"]>=df1["Open"] 
check_close=df1["High"]>=df1["Close"]
# print(check_high)
# print(check_close)

# #4.1 Verificare se il valore "low" è inferiore o uguale al valore di apertura e di chiusura
check_low=df1["Low"]<=df1["Open"]
check_low2=df1["Low"]<=df1["Close"]
# #print(check_low)
# #print(check_low2)

# #4.2 Verificare se il valore "adj close" è inferiore o uguale al valore close
check_adjclose=df1["Adj Close"]<=df1["Close"]
# #print(check_adjclose)

# #5.0 faccio il plot con mathplotlib tutto su un grafico
df1[['High','Open','Low','Close', 'Adj Close']].plot()
plt.title('TSLA Stock Trend')
plt.xlabel('Data')
plt.ylabel('Prezzo')
plt.show()

# #RICHIESTA 2
# #1.0 Creo un funzione per calcolare la formula -> ADTV[i] = (Volume[i] + Volume[i-1] + Volume[i-2] + Volume[i-3] + Volume[i-4])/5
# def calcola_adtv():
#     adtv=[]
#     for i in range(len(df1)):
#         adtv_value = (df1['Volume'].iloc[i] + df1['Volume'].iloc[i-1] + df1['Volume'].iloc[i-2] + df1['Volume'].iloc[i-3] + df1['Volume'].iloc[i-4]) / 5
#         #qui in teoria faccio il punto in cui converto in intero direttamente nella funzione
#         adtv_int=int(adtv_value)
#         adtv.append(adtv_int)
#     df1["ADTV"]= adtv
    
# calcola_adtv()
# print(df1)

# #2.0 Creo una funzione per calcolare la deviazione standard ->ADTV_std[i] = ((Volume[i]-ADTV[i])**2 + (Volume[i-1]-ADTV[i])**2 + (Volume[i-1]-ADTV[i])**2 +
# #                                                                           + (Volume[i-1]-ADTV[i])**2 + Volume[i-1]-ADTV[i])**2)/5

# def deviazione_adtv():
#     dev_adtv=[0 for x in range(5)]
#     for i in range(5,len(df1)):
#         dev_value_adtv = math.sqrt((df1['Volume'].iloc[i] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-1] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-2] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-3] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-4] - df1['ADTV'].iloc[i])**2)/5
#         dev_value_adtv_int=int(dev_value_adtv)
#         dev_adtv.append(dev_value_adtv_int)
#     df1["ADTV std"] = pd.Series(dev_adtv)

# deviazione_adtv()
# # print(df1)

# df1[['ADTV','ADTV std']].plot()
# plt.title('ADTV + ADTV std')
# plt.xlabel('Non lo so')
# plt.ylabel('Prezzo')
# plt.show()

# #REQUEST 3    
# #creo un nuovo dataframe con le colonne data e volume
# x1=pd.read_csv(filepath_or_buffer="TSLA.CSV",nrows=700)
# df2=pd.DataFrame(x1,columns=["Date","Volume"]).tail(5)
# #print(df2)
# #aggiungo le colonne adtv std per 2,5,10,20,20 giorni 

# def deviazione_adtv_giorni():
#     dev_adtv2=[]
#     for i in range(len(df1)):
#         dev_value_adtv5 = math.sqrt((df1['Volume'].iloc[i] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-1] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-2] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-3] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-4] - df1['ADTV'].iloc[i])**2)/5
#         dev_value_adtv2 = math.sqrt((df1['Volume'].iloc[i] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-1] - df1['ADTV'].iloc[i])**2)/5
#         dev_value_adtv10 = math.sqrt((df1['Volume'].iloc[i] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-1] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-2] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-3] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-4] - df1['ADTV'].iloc[i])**2)/5
#         dev_value_adtv20 = math.sqrt((df1['Volume'].iloc[i] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-1] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-2] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-3] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-4] - df1['ADTV'].iloc[i])**2)/5
#         dev_value_adtv50 = math.sqrt((df1['Volume'].iloc[i] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-1] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-2] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-3] - df1['ADTV'].iloc[i])**2 + (df1['Volume'].iloc[i-4] - df1['ADTV'].iloc[i])**2)/5
        
#         dev_value_adtv_int_2=int(dev_value_adtv2)
#         dev_value_adtv_int_5=int(dev_value_adtv5)
#         dev_value_adtv_int_10=int(dev_value_adtv10)
#         dev_value_adtv_int_20=int(dev_value_adtv20)
#         dev_value_adtv_int_50=int(dev_value_adtv50)
        
#         dev_adtv2.append((dev_value_adtv_int_2)*2)
#         dev_adtv3.append((dev_value_adtv_int_5)*5)
#         dev_adtv4.append((dev_value_adtv_int_10)*10)
#         dev_adtv5.append((dev_value_adtv_int_20)*20)
#         dev_adtv6.append((dev_value_adtv_int_50)*50)
        
#     #print(dev_adtv2) 
#     df2["ADTV std 2 Giorni"] = pd.Series(dev_adtv2)
#     df2["ADTV std 5 Giorni"] = pd.Series(dev_adtv3)
#     df2["ADTV std 10 Giorni"] = pd.Series(dev_adtv2)
#     df2["ADTV std 20 Giorni"] = pd.Series(dev_adtv2)
#     df2["ADTV std 50 Giorni"] = pd.Series(dev_adtv2)

# deviazione_adtv_giorni()
# print(df2)

# df2[['ADTV std 2 Giorni','ADTV std 5 Giorni','ADTV std 10 Giorni','ADTV std 20 Giorni','ADTV std 50 Giorni']].plot()
# plt.title('ADTV for different days')
# plt.xlabel('Date')
# plt.ylabel('ADTV')
# plt.show()

def calcola_adtv(df, nGiorni: int = 5):
    # Volume[i] + Volume[i-1] + Volume[i-2] + Volume[i-3] + Volume[i-4]
    adtv:float = 0
    adtv_column = [0 for x in range(nGiorni)]
 
    for i in range(nGiorni,df.shape[0]):
        for k in range(nGiorni):
            adtv += df.loc[i-k, "Volume"]
 
        adtv /= nGiorni
       
        adtv_column.append(int(adtv))  
 
    df[f'ADTV {nGiorni}'] = pd.Series(adtv_column)  
 
    return df

def calcola_adtv_std(df, nGiorni: int = 5):
    # sqrt((Volume[i]-ADTV[i])**2 + (Volume[i-1]-ADTV[i])**2 + (Volume[i-2]-ADTV[i])**2 +
    #              + (Volume[i-3]-ADTV[i])**2 + Volume[i-4]-ADTV[i])**2)/5)
    # sommaCumilativa += (volume[i] + adtv[i-k])**2 con k da 0 a nGiorni - 1
    adtv_std = 0
    adtv_std_column = [0 for x in range(nGiorni)]
    for i in range(nGiorni,df.shape[0]):
        for k in range(nGiorni):
            adtv_std += df.loc[i, "Volume"] + df.loc[i-k, f"ADTV {nGiorni}"]
 
        adtv_std /= nGiorni
        adtv_std = int(math.sqrt(adtv_std))
       
        adtv_std_column.append(adtv_std)  
 
    df[f'ADTV Std {nGiorni}'] = pd.Series(adtv_std_column)
 
    return df
 
df1 = calcola_adtv(df1,nGiorni = 2)
df1 = calcola_adtv_std(df1,nGiorni = 2)

df1 = calcola_adtv(df1,nGiorni = 5)
df1 = calcola_adtv_std(df1,nGiorni = 5)

df1 = calcola_adtv(df1,nGiorni = 10)
df1 = calcola_adtv_std(df1,nGiorni = 10)

df1 = calcola_adtv(df1,nGiorni = 20)
df1 = calcola_adtv_std(df1,nGiorni = 20)

df1 = calcola_adtv(df1,nGiorni = 50)
df1 = calcola_adtv_std(df1,nGiorni = 50)
print(df1)

plt.plot(df1['ADTV 2'],label="ADTV 2 GIORNI")
plt.plot(df1['ADTV Std 2'],label="ADTV STD 2 GIORNI")

plt.plot(df1['ADTV 5'],label="ADTV 5 GIORNI")
plt.plot(df1['ADTV Std 5'],label="ADTV STD 5 GIORNI")

plt.plot(df1['ADTV 10'],label="ADTV 10 GIORNI")
plt.plot(df1['ADTV Std 10'],label="ADTV STD 10 GIORNI")

plt.plot(df1['ADTV 20'],label="ADTV 20 GIORNI")
plt.plot(df1['ADTV Std 20'],label="ADTV STD 20 GIORNI")

plt.plot(df1['ADTV 50'],label="ADTV 50 GIORNI")
plt.plot(df1['ADTV Std 50'],label="ADTV STD 50 GIORNI")

plt.title('ADTV for different days')
plt.legend()
plt.xlabel('Date')
plt.ylabel('ADTV')
plt.show()
