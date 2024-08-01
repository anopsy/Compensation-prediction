import streamlit as st
import pandas as pd
from joblib import load


model = load("/app/rbf_model.joblib")

def show_predict_page():
    st.title("Engineering Compensation Prediction")

    st.write("""### We need some information to predict the compensation""")
    job_name = st.text_input("Job name", "e.g. data scientist")

    countries = (
            "United States",
            "India" ,
            "United Kingdom",
            "Other" ,
            "Canada" ,
            "Austria",
            "Brazil" ,
            "France",
            "Germany",
            "Australia",
            "South Africa",
            "Romania",
            "China",
            "Netherlands",
            "Lithuania",
            "Mexico" ,
            "Singapore",
            "Israel",
            "Spain" ,
            "Italy",
            "Japan" ,
            "New Zealand",
            "Philippines",
            "Argentina",
            "Poland",
            "Malaysia",
            "Ireland",
            "Cuba",
    )

    education = (
            "Unclear",
            "Bachelors",
            "High School",
            "Some High School",
            "Masters",
            "Doctorate",
            "Associates",
            "Vocational",
            "No Education Requirement",
    )

    hours = (
            "Full-Time",
            "Unclear",
            "Part-Time",
            "Contract",
            "Hourly",
            "Intern" ,
            "Temp",
    )
    seniorities = (
            "Unclear Seniority",
            "Senior IC",
            "Manager",
            "IC",
            "Junior IC",
            "Staff IC",
            "Intern",
            "Director",
            "Chief",
            "Contract",
            "Exec",
            "Senior Manager",
    )
    remote_opts = (
        "Unclear",
        "true",
        "false",
    )

    hour = st.selectbox("Hours", hours)
    remote = st.selectbox("Remote", remote_opts)
    education = st.selectbox("Education Level", education)
    seniority = st.selectbox("Seniority", seniorities)
    country = st.selectbox("Country", countries)

    ok = st.button("Calculate Compensation Estimation")
    if ok:

        df_predict = pd.DataFrame({
            "job_name": [job_name],
            "hours": [hour],
            "remote": [remote],
            "education": [education],
            "seniority":[seniority], 
            "country":[country],
        })

        estimation = model.predict(df_predict)
        scaler_loaded = load('/app/scaler.joblib')
        salary = scaler_loaded.inverse_transform([estimation])

        st.subheader(f"The estimated salary is ${salary[0][0]:,.0f}")

show_predict_page()

        