import streamlit as st
import numpy as np

st.title("Hybrid Electric Vehicle RL Dashboard")

speed = st.slider("Speed",0,120,50)
battery = st.slider("Battery",0,100,80)
temp = st.slider("Temperature",0,100,30)

efficiency = battery/100 - temp/200

st.metric("Estimated Efficiency",round(efficiency,3))

noise = speed/2

st.metric("Estimated Noise",round(noise,2))
