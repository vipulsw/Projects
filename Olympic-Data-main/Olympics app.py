import streamlit as st
import pandas as pd
import helper,Preprocessing
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.figure_factory as ff 
df=pd.read_csv("C:\\Users\\kvsan\\Desktop\\Ml projects\\olympics\\athlete_events.csv")
region_df=pd.read_csv("C:\\Users\\kvsan\\Desktop\\Ml projects\\olympics\\noc_regions.csv")
df=Preprocessing.preprocess(df,region_df)
st.sidebar.header("Olympic data analysis")
st.sidebar.image("https://logos-world.net/wp-content/uploads/2021/09/Olympics-Logo-1913-1986.png")
user=st.sidebar.radio("select an option",
                 ("Medal Tally","Overall Analysis","Country-wise Analysis","Athlete wise Analysis"))
if user == "Medal Tally":
    st.header("Medal Tally")
    years,country=helper.country_year_list(df)
    selected_year=st.sidebar.selectbox("Select year",years)
    selected_country=st.sidebar.selectbox("Select country",country)
    if selected_year=="Overall" and selected_country!="Overall":
        st.subheader("Overall performance of "+selected_country)
    if selected_year=="Overall" and selected_country=="Overall":
        st.subheader("Overall")
    if selected_year!="Overall" and selected_country=="Overall":
        st.subheader("Overall performance in "+str(selected_year))
    if selected_year!="Overall" and selected_country!="Overall":
        st.subheader("Overall performance of "+selected_country+" in "+str(selected_year))
    medal_tally=helper.fetch_medall_tally(df,year=selected_year,country=selected_country)
    st.table(medal_tally)
if user=="Overall Analysis":
    st.title("Top statistics")
    editions=df["Year"].nunique()-1
    cities= df["City"].nunique()
    sports=df["Sport"].nunique()
    events=df["Event"].nunique()
    athletes=df["Name"].nunique()
    nations=df["NOC"].nunique()

    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)
    col4,col5,col6=st.columns(3)
    with col4:
        st.header("Events")
        st.title(events)
    with col5:
        st.header("Athletes")
        st.title(athletes)
    with col6:
        st.header("Nations")
        st.title(nations)
    nations_over_time=helper.Data_over_time(df,"region")
    fig=px.line(nations_over_time,x="Edition",y="region")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)
    events_over_time=helper.Data_over_time(df,"Event")
    fig=px.line(events_over_time,x="Edition",y="Event")
    st.title("Events over the years")
    st.plotly_chart(fig)
    sports_over_time=helper.Data_over_time(df,"Sport")
    fig=px.line(sports_over_time,x="Edition",y="Sport")
    st.title("Sports over the years")
    st.plotly_chart(fig)
    athletes_over_time=helper.Data_over_time(df,"Name")
    fig=px.line(athletes_over_time,x="Edition",y="Name")
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig,ax=plt.subplots(figsize=(20,20))
    x=df.drop_duplicates(["Year","Sport","Event"])
    ax=sns.heatmap(x.pivot_table(index="Sport",columns="Year",values="Event",aggfunc="count").fillna(0).astype("int"),annot=True)
    st.pyplot(fig)
    st.title("Most Succesfull Athletes")
    sport_list=df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,"Overall")
    selected_sport=st.selectbox("Select a Sport",sport_list)
    x=helper.most_succesfull(df,selected_sport)
    st.table(x)
if user == "Country-wise Analysis":
    country_list=df["region"].unique()
    selected=st.sidebar.selectbox("select a country",country_list)
    final,heatmap=helper.year_wise_medal(df,selected)
    fig=px.line(final,x="Year",y="Medal")
    fig2,ax=plt.subplots(figsize=(20,20))
    ax=sns.heatmap(heatmap.pivot_table(index="Sport",columns="Year",values="Medal",aggfunc="count").fillna(0),annot=True)
    st.plotly_chart(fig)
    st.pyplot(fig2)
if user == "Athlete wise Analysis":
    st.title("Distibution of Age")
    athlete_df = df.drop_duplicates(subset=["Name","region"])
    x1=athlete_df["Age"].dropna()
    x2=athlete_df[athlete_df["Medal"]=="Gold"]["Age"].dropna()
    x3=athlete_df[athlete_df["Medal"]=="Silver"]["Age"].dropna()
    x4=athlete_df[athlete_df["Medal"]=="Bronze"]["Age"].dropna()
    fig=ff.create_distplot([x1,x2,x3,x4],["Overall","Gold","Silver","Bronze"],show_hist=False,show_rug=False)
    st.plotly_chart(fig)
    sport_list=df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,"Overall")
    selected_sport=st.selectbox("Select a Sport",sport_list)
    temp_df=helper.weight_v_height(df,selected_sport)
    st.header("Weight vs Height: "+selected_sport)
    fig,ax=plt.subplots()
    ax=sns.scatterplot(x=temp_df["Weight"],y=temp_df["Height"],hue=temp_df["Medal"],style=temp_df["Sex"],s=100)
    st.pyplot(fig)
    final=helper.males_v_females(df)
    fig=px.line(final,x="Year",y=["Male","female"])
    st.title("Participation of Male vs Female over the years")
    st.plotly_chart(fig)