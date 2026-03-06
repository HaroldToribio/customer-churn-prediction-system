import os
import joblib # type: ignore
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Churn Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar modelo
base_dir = os.path.dirname(os.path.abspath(__file__))
ruta_modelo = os.path.join(base_dir, "..", "models", "modelo_churn.pkl")

modelo = joblib.load(ruta_modelo)
print("Modelo cargado correctamente")


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
    CustomerSupportCalls: int
    ComplaintCount: int
    CompetitorOffer: str
    CustomerSatisfactionScore: int
    LatePayments: int


@app.get("/")
def root():
    return {"mensaje": "API de predicción de churn activa"}


@app.post("/predecir")
def predecir(cliente: Cliente) -> dict[str, int | float]:

    # Convertir a DataFrame
    datos = pd.DataFrame([cliente.model_dump()])

    prediccion = modelo.predict(datos)[0]
    probabilidad = modelo.predict_proba(datos)[0][1]

    return {
        "prediccion": int(prediccion),
        "probabilidad_churn": round(float(probabilidad), 4)
    }