from sklearn.metrics import accuracy_score, classification_report


def evaluar_modelo(modelo, X_test, y_test):
    """
    Evalúa el modelo entrenado mostrando métricas básicas.
    """

    y_pred = modelo.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))