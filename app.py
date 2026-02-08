from prime import prime
import streamlit as st

st.title("Prime Number Checker")

st.write("Enter an number and check whether it is Prime or Not Prime")
num = st.text_input("Pls enter a number greater than or equal to 2:")

if st.button("Check"):
    try:
        num = int(num)
        output = prime(num)
        st.success(output)
    except ValueError:
        st.error("Please enter a valid Intput")