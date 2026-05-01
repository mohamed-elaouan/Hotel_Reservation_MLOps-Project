<div align="center">
  <img src="https://img.icons8.com/external-flatart-icons-flat-flatarticons/128/000000/external-hotel-hotel-services-and-facilities-flatart-icons-flat-flatarticons-1.png" alt="Hotel Logo" width="80" />
  <h1>Hotel Reservation Cancellation Predictor</h1>
  <h3>End-to-End MLOps Pipeline & Production Deployment</h3>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge&logo=mlflow&logoColor=white" alt="MLflow" />
    <img src="https://img.shields.io/badge/GCP-Cloud_Run-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="GCP" />
    <img src="https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?style=for-the-badge&logo=jenkins&logoColor=white" alt="Jenkins" />
    <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  </p>
</div>

---

## 📈 Dashboard Preview
![Application Dashboard](./docs/assets/dashboard_mockup.png)
*Professional UI for real-time reservation risk assessment.*

---

## 🏨 Business Value & Impact
Cancellations represent a major revenue leakage for the hospitality industry. This project provides a **predictive solution** to:
- **Minimize Revenue Loss**: Identify high-risk bookings early to optimize overbooking strategies.
- **Optimize Operations**: Better staff and resource allocation based on actual expected occupancy.
- **Dynamic Pricing**: Enable targeted marketing or flexible pricing for high-probability cancellations.

---

## ⚙️ MLOps Lifecycle Architecture
The system follows a robust industry-standard lifecycle from raw data to a scalable cloud endpoint:

```mermaid
graph LR
    A[(GCS Bucket)] -- Raw Data --> B[Ingestion Pipeline]
    B --> C[Preprocessing & SMOTE]
    C --> D[LightGBM Training]
    D --> E{MLflow UI}
    E -- Model Artifact --> F[Flask API]
    F -- Dockerized --> G[Jenkins CI/CD]
    G --> H[Google Cloud Run]
```

---

## 🛠️ Essential Technical Features
- **Experiment Tracking**: Full lifecycle management using **MLflow** for hyperparameter tuning (`RandomizedSearchCV`) and artifact versioning.
- **Imbalanced Data Handling**: Implementation of **SMOTE** to handle class imbalance in reservation cancellations.
- **Scalable Deployment**: Fully containerized environment with **Docker**, orchestrated by a **Jenkins** CI/CD pipeline.
- **Cloud Infrastructure**: Serverless deployment on **Google Cloud Run** for high availability and auto-scaling.

---

## 📂 Project Structure
```text
├── application.py          # Flask entry point
├── pipeline/               # Orchestration scripts
├── src/                    # Core modular logic (Ingestion, Preprocessing, Training)
├── config/                 # YAML & Python configurations
├── templates/ & static/    # Modern UI resources
└── Dockerfile & Jenkinsfile # Infrastructure as Code
```

---

## 🚀 Essential Setup

### 1. Environment Preparation
```bash
python -m venv venv
# Activate: source venv/bin/activate (Unix) or venv\Scripts\activate (Windows)
pip install -e .
```

### 2. Execution Flow
- **Train Model**: `python pipeline/training_pipeline.py`
- **Track Experiments**: `mlflow ui` (Open http://localhost:5000)
- **Local Serve**: `python application.py` (Access http://localhost:8080)

---

## 👨‍💻 Author
**Mohamed EL Aouan**  
*Data Scientist & MLOps Architect*

---
*Developed as a professional portfolio demonstration of production-grade Machine Learning Engineering.*
