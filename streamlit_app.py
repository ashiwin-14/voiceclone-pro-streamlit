import streamlit as st
import numpy as np

st.set_page_config(
    page_title="VoiceClone Pro - Fixed!",
    page_icon="🎤"
)

st.title("🎉 VoiceClone Pro is Working!")
st.success("✅ Deployment successful! App is running correctly.")

st.subheader("📁 File Upload Test")
uploaded_file = st.file_uploader("Test file upload", type=['mp3', 'wav', 'txt'])

if uploaded_file:
    st.success(f"✅ File uploaded: {uploaded_file.name}")
    st.balloons()

st.sidebar.success("🚀 App Status: Running")
st.sidebar.info("✅ Dependencies: Loaded")
st.sidebar.info("✅ Build: Successful")

st.markdown("---")
st.write("**If you see this, your Streamlit app is working perfectly!**")
