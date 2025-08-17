from fastapi import FastAPI
from services.data_loader.DAL import DataLoader

app = FastAPI()
dl = DataLoader()
dl.startup()

@app.get("/data")
def get_data():
    return dl.fetch_all()
