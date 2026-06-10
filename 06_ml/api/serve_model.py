from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="ML Model API")

MODEL_PATH = Path(__file__).resolve().parent.parent / "best_model.pkl"

model = joblib.load(MODEL_PATH)
feature_names = list(model.feature_names_in_)


class PredictionInput(BaseModel):
    num__total_orders: float
    num__total_spent: float
    num__average_order_amount: float
    num__successful_payments: float
    cat__city_Abu_Dhabi: int
    cat__city_Ajman: int
    cat__city_Dubai: int
    cat__city_Sharjah: int


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is running",
        "model_loaded": True,
        "model_type": str(type(model)),
        "features": feature_names
    }


@app.post("/predict")
def predict(data: PredictionInput):
    input_data = data.dict()

    input_df = pd.DataFrame([{
        "num__total_orders": input_data["num__total_orders"],
        "num__total_spent": input_data["num__total_spent"],
        "num__average_order_amount": input_data["num__average_order_amount"],
        "num__successful_payments": input_data["num__successful_payments"],
        "cat__city_Abu Dhabi": input_data["cat__city_Abu_Dhabi"],
        "cat__city_Ajman": input_data["cat__city_Ajman"],
        "cat__city_Dubai": input_data["cat__city_Dubai"],
        "cat__city_Sharjah": input_data["cat__city_Sharjah"],
    }])

    input_df = input_df[feature_names]

    prediction = model.predict(input_df)

    prediction_value = int(prediction[0])

    return {
        "prediction": prediction_value,
        "message": "Prediction completed successfully"
    }
