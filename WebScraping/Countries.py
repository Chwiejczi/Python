from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from datetime import datetime  

def is_valid(text): 
    if text not in ['-', '–', '—', '']:
        return text
    return 0 


def clean_number(x):
    if x is None:
        return np.nan
    x = str(x).strip()
    x = x.replace(',', '')
    if '(' in x:
        x = x.split('(')[0].strip()
    if x in ['', '-', '–', '—', 'N/A', 'n/a', '—N/a']:
        return np.nan
    try:
        return round(float(x), 2)
    except ValueError:
        return np.nan


def extract(url, table_attribs):  
    headers = {
        "User-Agent": "MyPythonScraper/1.0 (kotprezesa2005@gmail.com)"
    }
    page=requests.get(url,headers=headers).text  
    data=BeautifulSoup(page,'html.parser')  
    table=data.find_all('tbody')   
    rows=table[2].find_all('tr')  
    data=[]  
    for row in rows: 
        cols=row.find_all('td')  
        if len(cols) >= 2: 
            txt1=cols[1].get_text(strip=True) 
            txt2=cols[2].get_text(strip=True) 
            if cols[0].find('a') is not None and is_valid(txt1) and is_valid(txt2): 
                Country=cols[0].get_text(strip=True) 
                imf=cols[1].get_text(strip=True) 
                wb=cols[2].get_text(strip=True)  
                imf=is_valid(imf) 
                wb=is_valid(wb) 
                temp=[Country,imf,wb] 
                data.append(temp) 
    
    df=pd.DataFrame(data,columns=table_attribs) 
    return df

def Transform(df): 
    #IMF_temp=df["IMF"].to_list()   

    #IMF_temp=[x.replace(',','').split('(')[0] if ',' in x  else x for x in IMF_temp] 
    #IMF_temp=[x.split('(')[0] for x in IMF_temp]
    #IMF_temp=[round(float(x),2) for x in IMF_temp] 
    df["IMF"] = [clean_number(x) for x in df["IMF"]]
    
    df["Word_Bank"] = [clean_number(x) for x in df["Word_Bank"]]

    return df


url='https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)' 
table_attribs=["Country","IMF","Word_Bank"] 
df=extract(url, table_attribs) 
df=Transform(df)
print(df) 



