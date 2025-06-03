#Social Support AI with LangGraph Agents

This project automates eligibility assessments for government social support applications using Machine Learning and agent-based orchestration with **LangGraph**.


## Features

- Ingests applicant data from CSV
- Validates application consistency
- Uses a trained ML model to predict eligibility
- Provides intelligent support recommendations
- LangGraph agent orchestration
- Interactive UI using Streamlit



## Tech Stack

- Python
- scikit-learn, pandas, joblib
- LangGraph + LangChain (agent orchestration)
- Streamlit (user interface)
- FastAPI (optional API layer)


## 📁 Folder Structure

social_support_ai/
├── data/ # CSV data files
├── eligibility_model/ # ML model training and features
├── agents/ # LangGraph agents and orchestrator
├── ui/ # Streamlit interface
├── api/ # FastAPI endpoints (optional)
├── requirements.txt
├── README.md



---

## Setup Instructions

```bash
git clone https://github.com/Creattorr/Social-Support-AI-Application-.git
cd social_support_ai
pip install -r requirements.txt
```
##Train the model:
```bash
python eligibility_model/train_model.py
```

## Run Instructions

### 1. Start API
```bash
uvicorn api.main:app --reload
```

### 2. Start UI
```bash
streamlit run ui/app.py
```
Then visit http://localhost:8501


## Future Enhancements


- Integrate OCR & document parsing
- Use local LLMs via Ollama for response generation
- Add LangSmith observability for agent monitoring








