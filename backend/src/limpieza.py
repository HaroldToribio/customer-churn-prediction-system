import pandas as pd

'''
Primera limpieza

def cargar_y_limpiar_datos():

    # Ruta del dataset
    ruta = "../data/WA_Fn-UseC_-Telco-Customer-Churn.csv"

    # Cargar dataset
    df = pd.read_csv(ruta)

    print("Dataset cargado correctamente")
    print("Dimensiones iniciales:", df.shape)

    # Eliminar columna irrelevante
    df.drop("customerID", axis=1, inplace=True)

    # Convertir TotalCharges a numérico
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Eliminar valores nulos
    df.dropna(inplace=True)

    # Convertir Churn a binaria
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    print("Limpieza completada")
    print("Dimensiones finales:", df.shape)

    return df


if __name__ == "__main__":
    df_limpio = cargar_y_limpiar_datos()
    print(df_limpio.head()) 
    '''

def cargar_y_preparar_datos():

    ruta = "../data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    df = pd.read_csv(ruta)

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
    x = df.drop("Churn", axis=1)
    y = df["Churn"]

    # One Hot Encoding
    x = pd.get_dummies(x, drop_first=True)

    print("Dimensiones después de encoding:", x.shape)

    return x, y


if __name__ == "__main__":
    x, y = cargar_y_preparar_datos()
    print("x shape:", x.shape)
    print("y shape:", y.shape)