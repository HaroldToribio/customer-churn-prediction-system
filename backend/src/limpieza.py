import os
import pandas as pd

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

    print("Dimensiones después limpieza:", df.shape)

    # Separar variables
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    print("Dimensiones después de encoding:", X.shape)

    return X, y