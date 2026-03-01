# Customer Churn Prediction System

Sistema completo de predicción de abandono de clientes utilizando Machine Learning, API REST y Dashboard Web.

---

## 📌 Descripción

Este proyecto implementa un sistema cliente-servidor que permite predecir la probabilidad de abandono (churn) de un cliente de telecomunicaciones.

El sistema incluye:

- Modelo de Machine Learning entrenado con datos reales.
- API REST desarrollada con FastAPI.
- Dashboard web interactivo.
- Visualización gráfica de probabilidad de churn.

---

## 🧠 Modelo de Machine Learning

- Algoritmo: Logistic Regression
- Preprocesamiento:
  - Limpieza de datos
  - Conversión de variables
  - One-Hot Encoding
  - Escalado con StandardScaler
- Serialización del modelo con Joblib

---

## 🏗 Arquitectura del Sistema

Usuario → Frontend (HTML + Chart.js) → FastAPI → Modelo → Respuesta JSON → Visualización

---

## 📂 Estructura del Proyecto
segundo_parcial/
│
├── backend/
│ ├── src/
│ │ ├── main.py
│ │ ├── limpieza.py
│ │ ├── entrenamiento.py
│ │ └── evaluacion.py
│ ├── models/
│ │ └── modelo_churn.pkl
│ └── data/
│
├── frontend/
│ └── index.html
│
├── requirements.txt
└── README.md

---

## 🚀 Instalación

1. Clonar el repositorio:
git clone <url-del-repositorio>

2. Crear entorno virtual:
python -m venv .venv


3. Activar entorno virtual:

Windows:.venv\Scripts\activate
Mac/Linux:source .venv/bin/activate

4. Instalar dependencias: pip install -r requirements.txt

---

## ▶️ Ejecución del Backend

Ubicarse en: backend/src

Ejecutar: uvicorn main:app --reload

La API estará disponible en: http://127.0.0.1:8000

Documentación interactiva: http://127.0.0.1:8000/docs

---

## 🌐 Ejecución del Frontend

Abrir el archivo:frontend/index.html

en el navegador.

---

## 📊 Funcionalidades

- Predicción binaria (Churn / No Churn)
- Probabilidad de abandono
- Visualización tipo dashboard
- Interpretación automática del riesgo

---

## 🎓 Contexto Académico

Proyecto desarrollado para la asignatura de Simulación de Sistemas.

---

## 🐳 Ejecutar con Docker

Construir y levantar el sistema:
docker-compose up --build

La API estará disponible en:
http://localhost:8000

## 👨‍💻 Autor

Harold Toribio