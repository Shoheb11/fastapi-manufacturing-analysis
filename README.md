# Predictive Analysis for Manufacturing Operations

## **Project Overview**
This project implements a **RESTful API** to predict **machine downtime** in manufacturing operations. The API is built using **FastAPI**, a high-performance Python framework, and leverages **machine learning models** to make predictions. Users can:
- Upload manufacturing data.
- Train a predictive model.
- Get predictions on new data.

---

## **Features**
1. **Upload Dataset**: Accepts manufacturing data in CSV format.
2. **Train Model**: Trains a machine learning model using the uploaded dataset.
3. **Make Predictions**: Provides predictions for machine downtime based on user-provided input.
4. **Metrics Reporting**: Outputs performance metrics (accuracy, F1-score) after training.

---

## **Technologies Used**
- **Backend Framework**: FastAPI
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas
- **Server**: Uvicorn

---

## **Endpoints**

### 1. **Upload Dataset**
- **URL**: `/upload`
- **Method**: `POST`
- **Description**: Uploads a CSV file with manufacturing data.
- **Request**:
  - Body: Form-data with the file.
- **Example** (Using `curl`):
  ```bash
  curl -X POST "http://127.0.0.1:8000/upload" -F "file=@path/to/dataset.csv"
  ```
- **Response**:
  ```json
  {
    "message": "File uploaded successfully.",
    "file_location": "uploaded_data.csv"
  }
  ```

---

### 2. **Train Model**
- **URL**: `/train`
- **Method**: `POST`
- **Description**: Trains a logistic regression model using the uploaded dataset and returns model performance metrics.
- **Request**: No parameters required.
- **Example** (Using `curl`):
  ```bash
  curl -X POST "http://127.0.0.1:8000/train"
  ```
- **Response**:
  ```json
  {
    "message": "Model trained successfully.",
    "metrics": {
      "accuracy": 0.85,
      "f1_score": 0.88
    }
  }
  ```

---

### 3. **Predict**
- **URL**: `/predict`
- **Method**: `POST`
- **Description**: Accepts input features and returns a prediction with confidence.
- **Request**:
  - Body: JSON with features.
  - Example Input:
    ```json
    {
      "Temperature": 80,
      "Run_Time": 120
    }
    ```
- **Example** (Using `curl`):
  ```bash
  curl -X POST "http://127.0.0.1:8000/predict" \
       -H "Content-Type: application/json" \
       -d '{"Temperature": 80, "Run_Time": 120}'
  ```
- **Response**:
  ```json
  {
    "Downtime": "Yes",
    "Confidence": 0.92
  }
  ```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/predictive-analysis-api.git
cd predictive-analysis-api
```

### **2. Create and Activate a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
Start the server with Uvicorn:
```bash
uvicorn app:app --reload
```
- The API will be accessible at `http://127.0.0.1:8000`.

---

## **Project Workflow**
1. Upload a manufacturing dataset via the `/upload` endpoint.
2. Train the predictive model using the `/train` endpoint.
3. Use the `/predict` endpoint to get machine downtime predictions.

---

## **Sample Dataset**
A sample dataset (`sample_data.csv`) is included in the repository with the following structure:
| Machine_ID | Temperature | Run_Time | Downtime_Flag |
|------------|-------------|----------|---------------|
| 1          | 85          | 200      | 1             |
| 2          | 70          | 150      | 0             |

---

## **Requirements**
- Python 3.8+
- Libraries:
  - FastAPI
  - Uvicorn
  - Pandas
  - Scikit-learn
  - Python-multipart

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

## **Testing**
Test the API using tools like:
1. **Postman**: Create requests for `/upload`, `/train`, and `/predict`.
2. **Curl**: Run commands provided in the examples above.

Swagger UI is available at:
- **Interactive Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Docs**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## **Future Enhancements**
- Add support for multiple models (e.g., Decision Tree, Random Forest).
- Extend the API to handle real-time data streams.
- Build a simple dashboard to visualize model metrics and predictions.

---



