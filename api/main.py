from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Social Support AI API",
    description="AI-powered eligibility assessment with LangGraph",
    version="1.0"
)

app.include_router(router)
