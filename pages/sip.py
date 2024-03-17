import time
import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd

data = pd.read_csv("pages/data/income.csv")
max_investment_value = int(data["invest_amt"])

# st.subheader('Supp! Ever wondered how to make your money work for you while you sip on your coffee? ')

# st.write('this tool helps you keep trackof your sip monthly investment amount and how your interest grows with time :sunglasses:')

st.image("assets/sip-header.png")

_LOREM_IPSUM = "Supp! Ever wondered how to make your money work for you while you sip on your coffee? \n this tool helps you keep trackof your sip monthly investment amount and how your interest grows with time :sunglasses:"


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("SiP SiP :coffee:"):
    st.write_stream(stream_data)

monthly_investment = st.slider(
    "monthly investment", min_value=500, max_value=max_investment_value, step=500
)


return_rate = st.slider(
    "expected annual return rate", min_value=1, max_value=30, step=1
)


time_period = st.slider("time period", min_value=1, max_value=30, step=1)


# if st.button("enter customised data"):
# monthly_investment = st.number_input("monthly investment")
# return_rate = st.number_input("expected return rate")
# time_period = st.number_input("time period")

number_of_months = time_period * 12
monthly_rate = return_rate / 100 / 12
future_value = 0
for i in range(int(number_of_months)):
    future_value += monthly_investment
    future_value *= 1 + monthly_rate
# future_value = monthly_investment * ((((1 + monthly_rate)**(number_of_months))-1) * (1 + monthly_rate))/monthly_rate

st.markdown(
    f"### Amount invested per month: ₹{monthly_investment} \n ### Expected return rate: {return_rate}%\n ### Time period: {time_period} years"
)
st.markdown(f"### Future value of investment:  ₹{int(future_value)}")
st.markdown(f"### Total investment: ₹{monthly_investment * number_of_months}")

# update data['invest_amt'] to invest_amt - monthly_investment
data["invest_amt"] = int(data["invest_amt"]) - monthly_investment

st.markdown(
    f"### After investing to sip you have: ₹{int(data['invest_amt'])} left to invest"
)
