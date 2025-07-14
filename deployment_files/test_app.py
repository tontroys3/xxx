import streamlit as st

# Simple test to verify Streamlit works
st.title("🎥 StreamFlow Test")
st.write("This is a test to verify the app works on Streamlit.io")

if st.button("Click Me"):
    st.success("App is working correctly!")
    
st.write("If you see this page, the deployment is successful.")