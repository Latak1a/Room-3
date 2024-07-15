import pandas as pd,math,numpy as np,os
from matplotlib import pyplot as plt
import copy

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
    # sommaCumulativa += (volume[i] + adtv[i-k])**2 con k da 0 a nGiorni - 1
    adtv_std = 0
    adtv_std_column = [0 for x in range(nGiorni)]
    for i in range(nGiorni,df.shape[0]):
        for k in range(nGiorni):
            adtv_std += (df.loc[i-k, "Volume"] - df.loc[i, f"ADTV {nGiorni}"])**2
 
        adtv_std /= nGiorni
        adtv_std = int(math.sqrt(adtv_std))
       
        adtv_std_column.append(adtv_std)  
 
    df[f'ADTV Std {nGiorni}'] = pd.Series(adtv_std_column)
 
    return df

def calcola_media_10_giorni(df, nGiorni=10):
    df = calcola_adtv(df, nGiorni)
    df = calcola_adtv_std(df, nGiorni)
    adtv_10 = df[f'ADTV {nGiorni}'].mean()
    adtv_std_10 = df[f'ADTV Std {nGiorni}'].mean()
    return df, adtv_10, adtv_std_10

def save_csv(df):
    output_dir = "Output_data"
    file_name = "Modified_TSLA.csv"
    
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir) 
        os.chdir(output_dir)
        if os.path.exists(file_name):
            df.to_csv(file_name, mode="w+", index=False)
        else:
            df.to_csv(file_name, index=False)  
    elif os.path.isdir(output_dir):
        os.chdir(output_dir)
        if os.path.exists(file_name):
            df.to_csv(file_name, mode="w+", index=False)
        else:
            df.to_csv(file_name, index=False)
            
def build_xticklabels(column, start, end, frequency):
    xticklabels = []
    for idx in range(int(start), int(end)):
        if idx % frequency == 0:
            xticklabels.append(idx)
    return xticklabels
    
def correlazioni(nomeColonnaPrincipale: str, df: pd.DataFrame):
    nRighe = 3; nColonne = 2
    dimensioneFigura = (8 , 8)
    fig, axs = plt.subplots(nRighe, nColonne, figsize = dimensioneFigura)
    
    
 # 1 Individuare le colonne da plottare
    listaColonne = list(df.columns)
    listaColonne.remove(nomeColonnaPrincipale)
    df_adtv5=calcola_adtv(df,5)
    df.insert(column=7,value=df_adtv5,loc=5)#########################verificare funzione insert
    #print(listaColonne)
    # 2. Produrre la griglia di grafici 3x2
    
    def daPosizioneAIndici() -> list:
    # da listaColonne a [[0,0], [0,1], [1,0], [1,1], [2,0], [2,1]]
        listaIndici = []
        for i in range(nRighe):
            for j in range(nColonne):
                listaIndici.append([i, j])
                #print(listaIndici)
        return listaIndici

    listaIndici = daPosizioneAIndici()
    
    for index, colonna in enumerate(listaColonne):
        riga, col = listaIndici[index]        
        #parti del grafico
        axs[riga][col].scatter(df[nomeColonnaPrincipale]/df[nomeColonnaPrincipale].max(), df[colonna])
        axs[riga][col].set_title(f"{nomeColonnaPrincipale} vs {colonna}")
        axs[riga][col].set_xlabel(nomeColonnaPrincipale)
        axs[riga][col].set_ylabel(colonna)
    
    fig.tight_layout()
    plt.show()