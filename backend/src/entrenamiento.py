import os
import joblib  # type: ignore

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from limpieza import cargar_y_preparar_datos
from evaluacion import evaluar_modelo


def entrenar_modelo():

    X, y = cargar_y_preparar_datos()

    columnas_categoricas = X.select_dtypes(include=["object"]).columns
    columnas_numericas = X.select_dtypes(exclude=["object"]).columns

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Datos divididos correctamente")
    print("Train:", X_train.shape)
    print("Test:", X_test.shape)

    preprocesador = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), columnas_numericas),
            ("cat", OneHotEncoder(handle_unknown="ignore"), columnas_categoricas),
        ]
    )

    modelo = Pipeline([
        ("preprocessor", preprocesador),
        ("logistic", LogisticRegression(
            max_iter=5000,
            class_weight="balanced"
        ))
    ])

    modelo.fit(X_train, y_train)

    evaluar_modelo(modelo, X_test, y_test)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_models = os.path.join(base_dir, "..", "models")
    os.makedirs(ruta_models, exist_ok=True)

    ruta_modelo = os.path.join(ruta_models, "modelo_churn.pkl")

    joblib.dump(modelo, ruta_modelo)

    print("Modelo guardado en:", ruta_modelo)

    return modelo


if __name__ == "__main__":
    entrenar_modelo()