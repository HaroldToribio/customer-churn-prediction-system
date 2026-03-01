import os
import joblib
from limpieza import cargar_y_preparar_datos
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportMissingTypeStubs=false

def entrenar_modelo():

    # Cargar datos preparados
    x, y = cargar_y_preparar_datos()

    # Dividir datos
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    print("Datos divididos correctamente")
    print("Train:", x_train.shape)
    print("Test:", x_test.shape)

    # Crear modelo
    modelo = LogisticRegression(max_iter=1000)

    # Crear pipeline con escalado
    modelo = Pipeline([
        ("scaler", StandardScaler()),
        ("logistic", LogisticRegression(
            max_iter=5000,
            class_weight="balanced",
        ))
    ])

    # Entrenar
    modelo.fit(x_train, y_train)

    # Predicciones
    y_pred = modelo.predict(x_test)

    # Evaluación
    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("\nReporte de clasificación:\n")
    print(classification_report(y_test, y_pred))

    # ===== GUARDAR MODELO =====
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_models = os.path.join(base_dir, "..", "models")

    # Crear carpeta si no existe
    os.makedirs(ruta_models, exist_ok=True)

    ruta_modelo = os.path.join(ruta_models, "modelo_churn.pkl")

    print("Guardando modelo en:", ruta_modelo)

    joblib.dump(modelo, ruta_modelo)

    return modelo

if __name__ == "__main__":
    entrenar_modelo()