import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train():
    df = pd.read_csv("data/application_form.csv")
    X = df[["Age", "Dependents", "Monthly Income", "Credit Score"]]
    y = df["Support Type"].apply(lambda x: 1 if x == "Financial" else 0)
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, "eligibility_model/model.pkl")

