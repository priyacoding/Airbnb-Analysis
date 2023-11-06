import pandas as pd
import pymongo
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

# page configuration
page_icon_url = (r'c:\Users\Lenovo\Downloads\Airbnb_logo.png.png')
st.set_page_config(page_title='Airbnb',
                       page_icon=page_icon_url, layout="wide")

# page header transparent color
page_background_color = """
    <style>
    [data-testid="stHeader"] 
    {
    background: rgba(0,0,0,0);
    }
    </style>
    """
st.markdown(page_background_color, unsafe_allow_html=True)

    # title and position
st.markdown(f'<h1 style="text-align: center;color:blue;">Airbnb Analysis</h1>',
                unsafe_allow_html=True)

with st.sidebar:
    image_url = (r'c:\Users\Lenovo\Desktop\airbnb_banner.jpg.jpg')
    st.image(image_url, use_column_width=True)

    option = option_menu(menu_title=' ', options=['Home', 'Features Analysis'],
                         icons=['database-fill', 'list-task'])
    col1, col2 = st.columns([0.26, 0.48])

# CREATING CONNECTION WITH MONGODB ATLAS AND RETRIEVING THE DATA
client = pymongo.MongoClient("mongodb+srv://iam_priyu_s:priyadharshini@cluster0.e4tsodp.mongodb.net/?retryWrites=true&w=maj")
db = client.sample_airbnb
col = db.listingsAndReviews

# READING THE CLEANED DATAFRAME
df = pd.read_csv(r'c:\Users\Lenovo\Downloads\airbnb.csv')

if option == "Home":

 st.subheader("Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.")
 st.subheader(':violet[Skills take away From This Project]:')
 st.subheader('Python Scripting, Data Preprocessing, Visualization, EDA, Streamlit, MongoDb, PowerBI or Tableau')
 st.subheader(':violet[Domain]:')
 st.subheader('Travel Industry, Property management and Tourism')

df = pd.read_csv(r'c:\Users\Lenovo\Downloads\airbnb.csv')
country = st.sidebar.multiselect('Select a Country',sorted(df.country.unique()),sorted(df.country.unique()))
prop = st.sidebar.multiselect('Select Property_type',sorted(df.property_type.unique()),sorted(df.property_type.unique()))
room = st.sidebar.multiselect('Select Room_type',sorted(df.room_type.unique()),sorted(df.room_type.unique()))
if option=="Features Analysis":
    dinesh  = pymongo.MongoClient("mongodb+srv://iam_priyu_s:priyadharshini@cluster0.e4tsodp.mongodb.net/?retryWrites=true&w=maj")
    db = dinesh['sample_airbnb']
    col = db['listingsAndReviews']


    query = f'country in {country} & room_type in {room} & property_type in {prop}'

    col1,col2=st.columns([1,1],gap='small')

    with col1:
        df1 = df.query(query).groupby(["property_type"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                         title='Top 10 Property Types With Count',
                         x='property_type',
                         y='count',
                         orientation='v',
                         color='property_type',
                         color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True) 

        df1= df.query(query).groupby(["room_type"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.pie(df1,
                             title=' Room_Type With Count',
                             values='count',
                             names="room_type")
        fig.update_traces(textposition='inside', textinfo='value+label')
        st.plotly_chart(fig,use_container_width=True)
        df1= df.query(query).groupby(["bed_type"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.line(df1,
                             title=' Bed_Type With Count',
                             x='bed_type',
                             y='count',text='count',markers=True)
        fig.update_traces(textposition="top center")                    
        st.plotly_chart(fig,use_container_width=True)
        df1= df.query(query).groupby(["cancellation_policy"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.line(df1,
                             title=' Cancellation_Policy With Count',
                             x='cancellation_policy',
                             y='count',text='count',markers=True)

        fig.update_traces(textposition="top center")                    
        st.plotly_chart(fig,use_container_width=True)

        df1= df.query(query).groupby(["number_of_reviews"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                             title=' Number_Of_Reviews With Count',
                             x="number_of_reviews",
                             y="count",
                             text="count",
                             orientation='v',
                             color='count',
                             color_continuous_scale=px.colors.sequential.Darkmint_r)
        fig.update_traces( textposition='outside')
        st.plotly_chart(fig,use_container_width=True)
    with col2: 
        df1= df1= df.query(query).groupby('room_type',as_index=False)['minimum_nights'].sum()
        fig = px.pie(df1,
                             title='Minimum_Nights With Room_Type',
                             values="minimum_nights",
                             names="room_type")
        fig.update_traces(textposition='inside', textinfo='value+label')
        st.plotly_chart(fig,use_container_width=True) 
        df1= df1= df.query(query).groupby(["maximum_nights"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.pie(df1,
                             title='Maximum_Nights With Count',
                             values='count',
                             names="maximum_nights")
        fig.update_traces(textposition='inside')
        fig.update_layout(uniformtext_minsize=12)
        st.plotly_chart(fig,use_container_width=True)

        df1= df1= df.query(query).groupby(["accommodates"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                             title='Accommodates With Count',
                             x="accommodates",
                             y="count",
                             orientation='v',
                             color='count',
                             color_continuous_scale=px.colors.sequential.Bluered_r)
        st.plotly_chart(fig,use_container_width=True)
        df1= df1= df.query(query).groupby("property_type",as_index=False)['price'].mean().sort_values(by='price',ascending=False)[:10]
        fig = px.bar(df1,
                             title=' Property With MeanPrice ',
                             x="property_type",
                             y="price",
                             text="price",
                             orientation='v',
                             color='property_type',
                             color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True) 
        country_df = df.query(query).groupby('country',as_index=False)['price'].mean().sort_values(by='price')
        fig = px.scatter_geo(data_frame=country_df,
                                       locations='country',
                                       color= 'price', 
                                       hover_data=['price'],
                                       locationmode='country names',
                                       size='price',
                                       title= 'MeanPrice In Each Country',
                                       color_continuous_scale='agsunset'
                            )
        st.plotly_chart(fig,use_container_width=True) 



    df1= df.query(query).groupby(["host_response_time"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]               
    fig = px.bar(df1,
                             title=' Host_Response_Time With Count ',
                             x="host_response_time",
                             y="count",
                             text="count",
                             orientation='v',
                             color='host_response_time',
                             color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True) 

    fig = px.scatter(df, x="country", y="host_listings_count", facet_col="host_response_time",title="Country with host_listings_count",
                 width=800, height=400)
    st.plotly_chart(fig)
    df2= df.query(query).groupby('room_type',as_index=False)['price'].mean().sort_values(by='price')
    fig = px.bar(df2,
                             title=' Room  With MeanPrice ',
                             x="room_type",
                             y="price",
                             text="price",
                             orientation='v',
                             color='room_type',
                             color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True)

    st.header(":blue[Tableau Dashboard]")
    st.write(" ")
    st.write(":violet[Click The Link For Tableau Dashboard page]")
    st.write("https://public.tableau.com/app/profile/s.priya.dharshini2113/viz/Airbnb-Analyis/Dashboard1?publish=yes")
