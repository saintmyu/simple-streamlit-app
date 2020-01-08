# simple_app.py

import streamlit as st

x = st.slider('Select a value: ')
st.write(x, 'x + 2', x+2)
