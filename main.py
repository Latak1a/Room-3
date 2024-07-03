#importo pandas,numpy os e math
import pandas as pd,numpy,os,math

#importo le prime 700 righe dal csv
#1.0 per importare le 700 righe, trasformo il csv in un dataframe
#1.1 successivamente con la funzione head del dataframe di pandas, selezioni le prime 700 righe, lo ritrasformo in un nuovo data frame
#1.2 uso la funzione display per mostrare il nuovo data frame che contiene solo le 700 righe.


#2.0 faccio il sommario del data frame di 700 righe, tramite la funzione describe.(accennata da luca, me la sono andata a vedere)
#esempio: sommario=df.describe() -> print(sommario)

#3.0 uso la funzione isna() sul dataframe per vedere se ci sono nan -> restituisce true 
#esempio: check_nan=df.isna() -> print(check_nan)
#3.1 uso la funzione sum() per sommare tutti i nan del dataframe \\\\[[[sum se fatta una sola volta somma i nan delle colonne,fatta due volte ci da i totali dei nan]]]
#esempio: somma_nan=df.isna().sum().sum()

#4.0 questo lo faccio domani sera, è l'una di notte la sveglia suona tra 4 ore :O




