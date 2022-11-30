import streamlit as st

st.write("""
# Maximum Number Finder App
This app finds the maximum number from the given input
""")
#Get Input

st.header('User Input Parameters')

firstNumber = st.number_input("First No")
secondNumber = st.number_input("Second No")
thirdNumber = st.number_input("Third No")

st.subheader('Result')
res = max(firstNumber,secondNumber,thirdNumber)
st.write(res)
