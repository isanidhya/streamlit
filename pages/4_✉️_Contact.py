import streamlit as st


"""
# Contact page
"""

with st.form(key="form1"):
    user = st.text_input("Enter your Email id:",placeholder="Email id")
    password = st.text_input("Enter your Password:",placeholder="Password",type="password")
    st.form_submit_button("Submit")