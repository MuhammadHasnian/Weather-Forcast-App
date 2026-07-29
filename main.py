import streamlit as st
import plotly.express as px
from backend import get_data


#creating tite,input_text,slider widget
st.title("Weather forcast for  the next  days.")
place = st.text_input(label="Place:",placeholder="Enter the city name...")
days =  st.slider(label="Forecast days:",min_value=1,max_value=5,help="Select data to view.")
option = st.selectbox("Select data to view:",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}.")

try:
    if place:
    # calling function to get data
        data,dates= get_data(place,days,option)

    # if the option is temperature
        if option == "Temperature":
            data =  [temp/10 for temp in data]
            figure = px.line(x=dates, y=data, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)


        if option == "Sky":
            files ={"Clear":"images/clear.png","Clouds":"images/cloud.png",
                    "Rain":"images/rain.png","Snow":"images/snow.png"}
            sky = [files[condition] for  condition in data]
            print(sky)
            print(data)
            st.image(sky,width=180)

except:
    st.error("Please enter a valid city name.")




