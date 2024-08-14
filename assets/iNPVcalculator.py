import streamlit as st
import numpy as np

# Title of the app
st.title("NPV Calculator")

# User inputs
initial_investment = st.number_input("Initial Investment", value=0.0)
discount_rate = st.number_input("Discount Rate (%)", value=0.0) / 100
cash_flows = st.text_area("Cash Flows (comma-separated)", "1000, 2000, 3000")

# Convert cash flows to a list of floats
cash_flows = [float(x) for x in cash_flows.split(",")]

# Calculate NPV
npv = np.npv(discount_rate, [-initial_investment] + cash_flows)

# Display the result
st.write(f"Net Present Value (NPV): ${npv:.2f}")
