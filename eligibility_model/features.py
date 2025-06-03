def extract_features(row):
    return [
        row["Age"],
        row["Dependents"],
        row["Monthly Income"],
        row["Credit Score"]
    ]
