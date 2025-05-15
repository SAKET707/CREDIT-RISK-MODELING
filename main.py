import streamlit as st
from prediction_helper import predict

st.title("CREDIT RISK MODELING")

row1 = st.column(3)
row2 = st.column(3)
row3 = st.column(3)
row4 = st.column(3)

with row1[0]:
    age = st.number_input('Age',min_value=18,max_value=100,step=1,value=18)
with row1[1]:
    income = st.number_input('Income',min_value=0,value=0)
with row1[2]:
    loan_amount = st.number_input('Loan Amount',min_value=1,value=1)



loan_to_income_ratio = loan_amount/income if income>0 else 0
with row2[0]:
    st.text('Loan to Income Ratio :')
    st.text(f"{loan_to_income_ratio : .2f}")
with row2[1]:
    delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=0) 
with row3[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=0)

with row3[0]:
    loan_tenure_months = st.number_input('Loan Tenure (Months)',min_value=1,step=1,value=1)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=0)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=1)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

if st.button('Calculate Risk'):
    probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)
    
    st.write(f"Deafult Probability: {probability:.2%}")
    st.write(f"Credit Score: {credit_score}")
    st.write(f"Rating: {rating}")