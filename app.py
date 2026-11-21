
import streamlit as st
from predict import predict_demand
st.title("Bike rental demand forecast")
c1, c2 = st.columns(2)
yr = c1.selectbox("Year", [2011, 2012, 2013, 2014], index=2); mnth = c1.slider("Month", 1, 12, 6)
hr = c1.slider("Hour", 0, 23, 8); weekday = c1.selectbox("Weekday (0=Sun)", list(range(7)), index=2)
holiday = c1.checkbox("Holiday"); season = c2.selectbox("Season", ["spring","summer","fall","winter"], index=1)
weather = c2.selectbox("Weather", ["Clear","Mist","Light Snow","Heavy Rain"])
temp = c2.slider("Normalised temp (0-1)", 0.0, 1.0, 0.5); hum = c2.slider("Normalised humidity (0-1)", 0.0, 1.0, 0.6)
wind = c2.slider("Normalised wind speed (0-1)", 0.0, 1.0, 0.2)
wd = "Working Day" if (weekday in range(1,6) and not holiday) else "No work"
if st.button("Predict"):
    n = predict_demand([dict(yr=yr, mnth=mnth, hr=hr, weekday=weekday, holiday="Yes" if holiday else "No", workingday=wd,
                             season=season, weathersit=weather, temp=temp, hum=hum, windspeed=wind)])[0]
    st.metric("Predicted rentals this hour", n)
