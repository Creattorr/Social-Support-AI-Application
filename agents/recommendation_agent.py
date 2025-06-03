def run(state):
    if state["eligibility"] == "Approve":
        state["recommendation"] = "Provide financial support"
    else:
        state["recommendation"] = "Suggest upskilling programs"
    return state
