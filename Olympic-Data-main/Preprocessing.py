import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\kvsan\\Desktop\\Ml projects\\olympics\\athlete_events.csv")
region_df=pd.read_csv("C:\\Users\\kvsan\\Desktop\\Ml projects\\olympics\\noc_regions.csv")
def preprocess(df,region_df):
    # Filter for summer olympics
    df=df[df["Season"]=="Summer"]
    # merge with region_df
    df=df.merge(region_df,on="NOC",how="left")
    df.drop_duplicates(inplace=True)
    df=pd.concat([df,pd.get_dummies(df["Medal"])],axis=1)
    return df