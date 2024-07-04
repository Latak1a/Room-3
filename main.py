#importo pandas,numpy os e math
import pandas as pd,numpy,os,math 

#importo le prime 700 righe dal csv
#1.0 per importare le 700 righe, trasformo il csv in un dataframe
x1=pd.read_csv(filepath_or_buffer="TSLA.CSV")
df1=pd.DataFrame(x1)
#print(df1)

#1.1 successivamente con la funzione head del dataframe di pandas, selezioni le prime 700 righe, lo ritrasformo in un nuovo data frame
df2=df1.head(700)
#print(df2)

#1.2 uso la funzione display per mostrare il nuovo data frame che contiene solo le 700 righe.
#display ???__??? -> funziona sola nel notebook non nello script pyton 


#2.0 faccio il sommario del data frame di 700 righe, tramite la funzione describe.(accennata da luca, me la sono andata a vedere)
#esempio: sommario=df.describe() -> print(sommario)
sommario=df2.describe()
#print(sommario)

#3.0 uso la funzione isna() sul dataframe per vedere se ci sono nan -> restituisce true 
#esempio: check_nan=df.isna() -> print(check_nan)

n_a_n=df2.isna()
#print(n_a_n)
#3.1 uso la funzione sum() per sommare tutti i nan del dataframe \\\\[[[sum se fatta una sola volta somma i nan delle colonne,fatta due volte ci da i totali dei nan]]]
#esempio: somma_nan=df.isna().sum().sum()
somma_nan=df2.isna().sum().sum()
print(somma_nan) ### -> ci da zero perchè gia sapevamo che il csv non aveva nan

#4.0 Verificare se il valore "high" è maggiore o uguale al valore di apertura e di chiusura
#4.1 Verificare se il valore "low" è inferiore o uguale al valore di apertura e di chiusura
#4.2 Verificare se il valore "adj close" è inferiore o uguale al valore close

#5.0 faccio il plot con mathplotlib tutto su un grafico




