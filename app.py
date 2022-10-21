import uvicorn
from fastapi import FastAPI, Request, Body
from pydantic import BaseModel
from typing import Literal
from preprocesing.cleaning_data import preprocess
from predict.prediction import predict
import pandas as pd
from fastapi.encoders import jsonable_encoder
import os

PORT = os.environ.get('PORT', 8000)

app = FastAPI(PORT=PORT)


class Input(BaseModel):

    zip_code: int
    property_type: Literal["APARTMENT", "HOUSE"]
    rooms_number: int
    area: int
    equipped_kitchen: bool | None = None
    terrace_area: int | None = None
    land_area: int | None = None
    facades_number: int | None = None
    swimming_pool: bool | None = None
    building_state: Literal["NEW", "GOOD",
                            "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]


@app.get("/")
async def status_check():
    return "Alive"


@app.get("/predict")
async def data_format():

    return ("""Property information should be provided as following : zip_code: int, property_type:[APARTMENT,HOUSE], rooms_number: int, area: int, equipped_kitchen: Optional [bool], terrace_area: Optional [int], land_area: Optional [int], facades_number: Optional [int], swimming_pool: Optional [bool], building_state: [NEW, GOOD,TO RENOVATE,JUST RENOVATED,TO REBUILD]""")


@app.post("/predict")
async def make_prediction(data: Input = Body(embed=True)):

    json_data = jsonable_encoder(data)
    processed_json = preprocess(json_data)
    predicted_price = predict(processed_json)
    return predicted_price
