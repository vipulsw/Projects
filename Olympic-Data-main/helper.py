import numpy as np
import pandas as pd
import plotly.express as px
def medal_tally(df):
    medal_tally =df.drop_duplicates(subset=["Team","NOC","Games","Year","Season","City","Sport","Event","Medal"])
    # i hockey if 1 gold is wone 11 golds are being added because it has 11 players we did this to avoid that mistake.
    medal_tally=medal_tally.groupby("region").sum()[["Gold","Bronze","Silver"]].sort_values("Gold",ascending=False)
    medal_tally["Total"]=medal_tally["Gold"]+medal_tally["Silver"]+medal_tally["Bronze"]
    medal_tally["Gold"]=medal_tally["Gold"].astype(int)
    medal_tally["Silver"]=medal_tally["Silver"].astype(int)
    medal_tally["Bronze"]=medal_tally["Bronze"].astype(int)
    medal_tally["Total"]=medal_tally["Total"].astype(int)
    medal_tally["region"]=medal_tally.index
    medal_tally.index=np.arange(0,205)
    return medal_tally

def country_year_list(df):
    year=df["Year"].unique().tolist()
    year.sort()
    year.insert(0,"Overall")
    county=np.unique(df['region'].dropna().values).tolist()
    county.sort()
    county.insert(0,"Overall")
    return year,county
def fetch_medall_tally(df,year,country):
    medal_df = df.drop_duplicates(subset=["Team","NOC","Games","Year","Season","City","Sport","Event","Medal"])
    flag=0
    if year=="Overall" and country=="Overall":
        temp_df=medal_df
    elif year=="Overall" and country!="Overall":
        flag=1
        temp_df=medal_df[medal_df["region"]==country]
    elif year!="Overall" and country=="Overall":
        temp_df=medal_df[medal_df["Year"]==year]
    elif year!="Overall" and country!="Overall":
        temp_df=medal_df[(medal_df["Year"]==year)&(medal_df["region"]==country)]
    if flag==1:    
        x=temp_df.groupby("Year").sum()[["Gold","Bronze","Silver"]].sort_values("Gold",ascending=False)
    else:
        x=temp_df.groupby("region").sum()[["Gold","Bronze","Silver"]].sort_values("Gold",ascending=False)
    x["Total"]=x["Gold"]+x["Silver"]+x["Bronze"]
    x["Gold"]=x["Gold"].astype(int)
    x["Silver"]=x["Silver"].astype(int)
    x["Bronze"]=x["Bronze"].astype(int)
    x["Total"]=x["Total"].astype(int)
    return x
def Data_over_time(df,col):
    nations_over_time=df.drop_duplicates(["Year",col])["Year"].value_counts().reset_index().sort_values("index")
    nations_over_time.rename(columns={"index":"Edition","Year":col},inplace=True)
    return nations_over_time
def most_succesfull(df,sport):
    temp_df = df[df["Medal"]!=0]
    if sport!="Overall":
        temp_df=temp_df[temp_df["Sport"]==sport]
    x=temp_df["Name"].value_counts().reset_index().merge(df,left_on="index",right_on="Name")[["index","Name_x","Sport","region"]].drop_duplicates()
    x.rename(columns={"index":"Name","Name_x":"Medals"},inplace=True)
    return x
def year_wise_medal(df,country):
    temp_df=df.dropna(subset=["Medal"])
    temp_df.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event","Medal"],inplace=True)
    new_df=temp_df[temp_df["region"]==country]
    final_df=new_df.groupby("Year").count()["Medal"].reset_index()
    final_df1=temp_df[temp_df["region"]==country]
    return final_df,final_df1
def weight_v_height(df,sport):
    athlete_df = df.drop_duplicates(subset=["Name","region"])
    athlete_df["Medal"].fillna("No Medal",inplace=True)
    if sport!="Overall":
        temp_df=athlete_df[(athlete_df["Sport"]==sport)]
        return temp_df
    else:
        return athlete_df 
def males_v_females(df):
    athlete_df = df.drop_duplicates(subset=["Name","region"])
    men=athlete_df[athlete_df["Sex"]=="M"].groupby("Year").count()["Name"].reset_index()
    women=athlete_df[athlete_df["Sex"]=="F"].groupby("Year").count()["Name"].reset_index()
    final= men.merge(women,on="Year")
    final.rename(columns={"Name_x":"Male","Name_y":"female"},inplace=True)
    final.fillna(0,inplace=True)
    return final
    