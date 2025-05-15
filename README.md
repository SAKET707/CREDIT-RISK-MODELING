
************************************************************************************************************************************************************************************************************
##Credit Risk Modeling App
************************************************************************************************************************************************************************************************************

This project is a Streamlit-based web application that predicts an individual's credit risk by estimating their default probability, credit score, and providing a rating (Poor, Average, Good, Excellent). It uses a trained machine learning model built on financial and credit data to assist financial institutions in decision-making.

************************************************************************************************************************************************************************************************************
Features

    Predict default probability of a borrower.

    Calculate an estimated credit score on a 300–900 scale.

    Classify users into credit rating categories: Poor, Average, Good, Excellent.

    Interactive UI for entering applicant details.

    Real-time model inference using pre-trained artifacts.
    
    ************************************************************************************************************************************************************************************************************
Model Overview

The backend model is a logistic regression classifier trained on credit-related features. It outputs the probability of loan default, which is then transformed into a credit score using a scoring formula.
Inputs

The model takes the following user inputs via the UI:
Field	Description
Age	Applicant's age (18–100)
Income	Monthly income in INR
Loan Amount	Loan amount requested
Loan Tenure (Months)	Duration of the loan
Delinquency Ratio (%)	% of accounts with late payments
Avg DPD	Average Days Past Due on delinquent accounts
Credit Utilization Ratio	% of credit limit currently utilized
Open Loan Accounts	Number of active loan accounts
Residence Type	Owned / Rented / Mortgage
Loan Purpose	Education / Home / Auto / Personal
Loan Type	Secured / Unsecured

Derived Input:

    Loan to Income Ratio: Calculated as loan_amount / income

Outputs

After submitting inputs, the model returns:

    Default Probability: Estimated chance (in %) that the borrower will default.

    Credit Score: Score between 300 and 900.

    Rating:

        300–499: Poor

        500–649: Average

        650–749: Good

        750–900: Excellent

************************************************************************************************************************************************************************************************************
⚙How It Works

    Input Transformation:

        Inputs are converted into model features using a feature engineering pipeline (prepare_input()).

        Dummy variables and additional placeholders are filled to match the training format.

    Scaling:

        Features are normalized using a MinMaxScaler that was saved during training.

    Prediction:

        The logistic regression model returns a default probability.

        The probability is mapped to a credit score using:

        score = base_score + non_default_prob * scale_length

************************************************************************************************************************************************************************************************************
🛠 Dependencies

    streamlit

    pandas

    numpy

    scikit-learn

    joblib

Install them via:

pip install -r requirements.txt

************************************************************************************************************************************************************************************************************
Running the App

    Make sure you have Python installed.

    Place model_data.joblib inside the ARTIFACTS/ directory.

    Run the Streamlit app:

streamlit run app.py

************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
