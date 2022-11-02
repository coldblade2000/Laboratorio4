from fastapi import FastAPI
from typing import Optional
import pandas as pd
from DataModel import DataModel
from joblib import load

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/predict")
def make_predictions(data_model: DataModel):
    df = pd.DataFrame(data_model.dict(), columns=data_model.dict().keys(), index=[0])
    df.columns = data_model.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)[0]
    return result
