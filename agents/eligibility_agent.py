import joblib
from eligibility_model.features import extract_features

model = joblib.load("eligibility_model/model.pkl")

def run(state):
    row = state["parsed_data"]
    features = extract_features(row)
    prediction = model.predict([features])[0]
    state["eligibility"] = "Approve" if prediction == 1 else "Soft Decline"
    return state
