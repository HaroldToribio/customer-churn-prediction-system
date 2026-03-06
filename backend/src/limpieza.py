import os
import pandas as pd
import numpy as np

# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false

def cargar_y_preparar_datos():
    # Ruta absoluta al dataset
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_data = os.path.join(base_dir, "..", "data", "WA_Fn-UseC_-Telco-Customer-Churn.csv")

    df = pd.read_csv(ruta_data)

    print("Dimensiones iniciales:", df.shape)

    # Eliminar columna irrelevante
    df.drop("customerID", axis=1, inplace=True)

    # Convertir TotalCharges a numérico
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Eliminar nulos
    df.dropna(inplace=True)

    # Convertir variable objetivo
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Refactor numero 3: Agregar mas variables de prediccion
    np.random.seed(42)

    # Número de llamadas a soporte técnico
    df["CustomerSupportCalls"] = np.random.randint(0, 6, size=len(df))

    # Número de quejas registradas
    df["ComplaintCount"] = np.random.randint(0, 4, size=len(df))

    # Si recibió una oferta de un competidor
    df["CompetitorOffer"] = np.random.choice(
        ["Yes", "No"],
        size=len(df),
        p=[0.3, 0.7]
    )

    # Score de satisfacción del cliente (1 a 10)
    df["CustomerSatisfactionScore"] = np.random.randint(1, 11, size=len(df))

    # Número de pagos tardíos
    df["LatePayments"] = np.random.randint(0, 5, size=len(df))

    print("Variables agregadas:")
    print([
        "CustomerSupportCalls",
        "ComplaintCount",
        "CompetitorOffer",
        "CustomerSatisfactionScore",
        "LatePayments"
    ])

    print("Dimensiones después limpieza:", df.shape)

    # Separar variables
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    print("Dimensiones después de encoding:", X.shape)

    return X, y