from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Enable CORS for Flutter Web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load('student_model.pkl')

class StudentData(BaseModel):
    hours_studied: float
    previous_scores: float
    sleep_hours: float
    sample_papers: float

@app.post("/predict")
def predict_score(data: StudentData):
    features = np.array([[
        data.hours_studied,
        data.previous_scores,
        data.sleep_hours,
        data.sample_papers
    ]])
    
    predicted_score = model.predict(features)[0]
    bounded_score = max(0.0, min(100.0, float(predicted_score)))
    
    return {"predicted_score": round(bounded_score, 2)}