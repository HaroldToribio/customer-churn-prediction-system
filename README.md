# Customer Churn Prediction System

Sistema Predictivo de Abandono de Clientes

<img width="945" height="716" alt="image" src="https://github.com/user-attachments/assets/a055adc3-1c20-469c-8e43-a42f29e39800" />

---

## 📌 Descripción

Este proyecto implementa un Sistema de Predicción de Abandono de Clientes (Customer Churn) utilizando un modelo de Regresión Logística.

El sistema permite analizar el perfil de un cliente y estimar la probabilidad de que abandone el servicio, presentando los resultados en un Dashboard Ejecutivo interactivo.

El proyecto incluye:

Modelo de Machine Learning entrenado
API REST desarrollada con FastAPI
Frontend interactivo en HTML + JavaScript
Visualización de KPIs y probabilidad
Contenerización con Docker
Arquitectura separada Backend / Frontend

---

## 🧠 Modelo de Machine Learning

Se implementó un modelo de:

Regresión Logística

Variables principales consideradas:

Tipo de contrato
Antigüedad (tenure)
Cargos mensuales
Cargos totales
Servicio de internet
Soporte técnico
Servicios adicionales

El modelo devuelve:

Probabilidad de abandono (0–1)
Clasificación final (ALTO / BAJO riesgo)

---

## 🏗 Arquitectura del Sistema

Usuario → Frontend (HTML + Chart.js) → FastAPI → Modelo → Respuesta JSON → Visualización

---

## 📂 Estructura del Proyecto

customer-churn-prediction-system.git/
│
├── backend/
│   ├── entrenamiento.py
│   ├── main.py
│   └── modelo.pkl
│
├── frontend/
│   └── index.html
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

---

## 🚀 Instalación

1. Clonar el repositorio:
git clone https://github.com/HaroldToribio/customer-churn-prediction-system.git
cd customer-churn-prediction-system.git

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

Proyecto desarrollado como sistema académico y pieza de portafolio profesional orientada a Data Science y Backend Development.
