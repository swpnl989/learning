import numpy as np
import pandas as pd



def check_www(column_list,df):  # check and drop rows 
    drop_index= []
    for i,j in enumerate(column_list): 
        if j[0:4].lower()=='www.':
            pass
        else:
            drop_index.append(i)
    df = df.drop(drop_index)
    df = df.reset_index(drop=True)
    return df



def data_cleaning_scorecard(df):
    df['ADM_RATE'].replace(to_replace = '', value = '0.0', inplace=True)
    df['CCSIZSET'].replace(to_replace = '', value = '0.0', inplace=True)
    df.dropna(axis = 0,subset="NPCURL",inplace=True)
    df = df.reset_index(drop=True)
    df['sch_deg'].replace(to_replace = '', value = 'Null', inplace=True)
    df_1=df[df["AccredAgency"] == "Accreditation Commission for Acupuncture and Oriental Medicine"]
    df_2=df[df["AccredAgency"] == "Western Association of Schools and Colleges Senior College and University Commission"]
    df_3=df[df["AccredAgency"] == "Southern Association of Colleges and Schools Commission on Colleges | Council on Occupational Education"]
    df_4=df[df["AccredAgency"] == "National Association of Schools of Dance Commission on Accreditation"]
    df_5=df[df["AccredAgency"] == "National Association of Schools of Dance Commission on Accreditation"]
    df_6=df[df["AccredAgency"] == "Oklahoma Board of Career and Technology Education"]
    df_7=df[df["AccredAgency"] == "Puerto Rico State Agency for the Approval of Public Postsecondary Vocational Technical Institutions and Programs"]

    df_1.to_csv("cleaned_csv/ACAO_uni.csv",index=False)
    df_2.to_csv("cleaned_csv/WASC_uni.csv",index=False)
    df_3.to_csv("cleaned_csv/SACSC_uni.csv",index=False)
    df_4.to_csv("cleaned_csv/NAS_uni.csv",index=False)
    df_5.to_csv("cleaned_csv/NNA_uni.csv",index=False)
    df_6.to_csv("cleaned_csv/OBC_uni.csv",index=False)
    df_7.to_csv("cleaned_csv/PRAA_uni.csv",index=False)

df = pd.read_csv("CollegeScorecard.csv", keep_default_na=False)
df = check_www(list(df["INSTURL"]),df)
df = check_www(list(df["NPCURL"]),df)
data_cleaning_scorecard(df)    