from fastapi import APIRouter, UploadFile, File
import pandas as pd
from agents.master_orchestrator import run_full_pipeline

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    output = []

    for _, row in df.iterrows():
        input_data = {
            "Age": row["Age"],
            "Dependents": row["Dependents"],
            "Monthly Income": row["Monthly Income"],
            "Credit Score": row["Credit Score"]
        }
        result = run_full_pipeline(input_data)
        output.append({
            "Name": row["Name"],
            "Eligibility": result.get("eligibility"),
            "Recommendation": result.get("recommendation")
        })
    return {"results": output}
