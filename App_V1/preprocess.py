

import urduhack
#urduhack.download()

import pandas as pd
from urduhack.preprocessing import *
from urduhack.normalization import normalize
import json
import re

def text_preprocessing(text):
    """
    This Functions takes a string as input and returns preprocessed form of it in urdu language.
    """
    # removing digits and english letters
    Text=re.sub(r"[a-zA-z0-9]+", "", text)
    
    #removing \n (new line tag)
    Text=Text.replace("\n","") 
    
    #using urduhack's functions for data preprocessing 
    Text=normalize_whitespace(Text)
    Text=remove_punctuation(Text)
    Text=remove_accents(Text)
    Text=replace_urls(Text)
    Text=replace_emails(Text)
    Text=replace_phone_numbers(Text)
    Text=replace_numbers(Text)
    return Text

def normalization(text):
    """
    This Functions takes a string as input and returns normalized, consistent and cleaned form of it in urdu language.
    """
    
    #using urduhack's functions to normalize text. 
    #refer to docs here: https://docs.urduhack.com/en/stable/reference/normalization.html
    Text=normalize(text)
    
    #removing irregular whitescapes/empty srings/larger strings and imputing them with NaN
    Text=Text.strip()
    if len(Text)==0 :
        Text=Text.replace("", "NaN")
        
        return float(Text)
    else:
        return Text
    

sw=pd.read_json("Data/stopwords-ur.json.txt")[0].tolist()
def remove_stopwords(tokenized_text):
    Text=[w for w in tokenized_text if w not in sw]
    return Text



def clean_it(df):
    df["cleaned"]=df["tweets"].apply(lambda x: text_preprocessing(x))
    df["cleaned"]=df["cleaned"].apply(lambda x : normalization(x))
    df.dropna(inplace=True,axis=0)
    df.reset_index(inplace=True,drop=True)
    return df


