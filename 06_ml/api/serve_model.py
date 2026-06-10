from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path
import logging


app = FastAPI(title="ML Model API")


LOG_PATH = Path(__file__).resolve().parent / "api_logs.txt"

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logging.error(f"Validation error: {exc.errors()}")

    return JSONResponse(
        status_code=422,
        content={
            "message": "Invalid input. Please check the required fields and data types.",
            "errors": exc.errors()
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unexpected error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "message": "An unexpected error occurred while processing the request."
        }
    )


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

    class Config:
        extra = "forbid"


class PredictionOutput(BaseModel):
    prediction: int
    message: str


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is running",
        "model_loaded": True,
        "model_type": str(type(model)),
        "features": feature_names
    }


@app.post("/predict", response_model=PredictionOutput)
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

    logging.info(
        f"Prediction completed successfully. Prediction: {prediction_value}"
    )

    return {
        "prediction": prediction_value,
        "message": "Prediction completed successfully"
    }
