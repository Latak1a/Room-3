import pandas as pd,math,numpy as np,os


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
            adtv_std += df.loc[i, "Volume"] + df.loc[i-k, f"ADTV {nGiorni}"]
 
        adtv_std /= nGiorni
        adtv_std = int(math.sqrt(adtv_std))**2
       
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