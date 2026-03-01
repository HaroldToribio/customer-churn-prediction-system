import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from limpieza import cargar_y_preparar_datos
from fastapi.middleware.cors import CORSMiddleware

# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportMissingTypeStubs=false

# ===== CREAR APP =====
app = FastAPI(title="Churn Prediction API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "modelo_churn.pkl")

modelo = joblib.load(MODEL_PATH)

x_train, y_train = cargar_y_preparar_datos()
columnas_modelo = x_train.columns

class Cliente(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.post("/predict")
def predecir(cliente: Cliente) -> dict[str, float | int]:

    cliente_df = pd.DataFrame([cliente.model_dump()])
    cliente_df = pd.get_dummies(cliente_df, drop_first=True)
    cliente_df = cliente_df.reindex(columns=columnas_modelo, fill_value=0)

    pred = modelo.predict(cliente_df)[0]
    proba = modelo.predict_proba(cliente_df)[0][1]

    return {
        "prediction": int(pred),
        "probability": round(float(proba), 4)
    }