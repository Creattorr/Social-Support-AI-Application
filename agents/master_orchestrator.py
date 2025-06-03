from langgraph.graph import StateGraph, END
from agents.data_agent import run as data_step
from agents.validation_agent import run as validation_step
from agents.eligibility_agent import run as eligibility_step
from agents.recommendation_agent import run as recommendation_step

workflow = StateGraph()

workflow.add_node("DataAgent", data_step)
workflow.add_node("ValidationAgent", validation_step)
workflow.add_node("EligibilityAgent", eligibility_step)
workflow.add_node("RecommendationAgent", recommendation_step)

workflow.set_entry_point("DataAgent")
workflow.add_edge("DataAgent", "ValidationAgent")
workflow.add_edge("ValidationAgent", "EligibilityAgent")
workflow.add_edge("EligibilityAgent", "RecommendationAgent")
workflow.add_edge("RecommendationAgent", END)

app = workflow.compile()

def run_full_pipeline(input_dict):
    return app.invoke(input_dict)
