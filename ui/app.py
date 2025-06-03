import streamlit as st
import pandas as pd
from agents.master_orchestrator import run_full_pipeline

st.set_page_config(page_title="Social Support AI - LangGraph", layout="centered")
st.title("Social Support AI - LangGraph Edition")

uploaded_file = st.file_uploader("Upload Application Form CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df)

    if st.button("Run AI Assessment"):
        results = []

        st.write("### Processing Applications...")
        for index, row in df.iterrows():
            input_data = {
                "Age": row["Age"],
                "Dependents": row["Dependents"],
                "Monthly Income": row["Monthly Income"],
                "Credit Score": row["Credit Score"]
            }
            output = run_full_pipeline(input_data)
            results.append({
                "Name": row["Name"],
                "Eligibility": output.get("eligibility"),
                "Recommendation": output.get("recommendation")
            })

        result_df = pd.DataFrame(results)
        st.write("### AI Assessment Results", result_df)
