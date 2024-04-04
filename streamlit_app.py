import streamlit as st
import requests


def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][to_currency]


st.title("Currency Converter")

from_currency = st.selectbox(
    "From Currency", ["USD", "EUR", "JPY", "GBP", "AUD", "CAD"]
)
to_currency = st.selectbox("To Currency", ["USD", "EUR", "JPY", "GBP", "AUD", "CAD"])
amount = st.number_input("Amount", min_value=0.0, max_value=1000000.0)

if st.button("Convert"):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    st.write(
        f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}."
    )
