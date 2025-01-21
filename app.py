from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd

def train_model(data_path):
    # Load dataset
    data = pd.read_csv(data_path)
    X = data[['Temperature', 'Run_Time']]
    y = data['Downtime_Flag']

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return model, {"accuracy": accuracy, "f1_score": f1}

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()
model = None  # Global model variable

# Endpoint to upload data
@app.post("/upload")
async def upload_data(file: UploadFile = File(...)):
    data = pd.read_csv(file.file)
    data.to_csv("uploaded_data.csv", index=False)
    return {"message": "Data uploaded successfully."}

# Endpoint to train the model
@app.post("/train")
def train():
    global model
    model, metrics = train_model("uploaded_data.csv")
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    return {"message": "Model trained successfully.", "metrics": metrics}

# Endpoint to make predictions
class PredictionInput(BaseModel):
    Temperature: float
    Run_Time: float

@app.post("/predict")
def predict(input_data: PredictionInput):
    global model
    if not model:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
    input_df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(input_df)[0]
    confidence = max(model.predict_proba(input_df)[0])
    return {"Downtime": "Yes" if prediction == 1 else "No", "Confidence": confidence}

