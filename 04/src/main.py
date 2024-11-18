from fastapi import FastAPI, HTTPException, BackgroundTasks
from typing import List, Dict
import time

app = FastAPI()

# Fake database
tours : Dict[int, Dict] = {
    1: {
        "name": "Skiing in the Alps",
        "available": 10,
        "price": 1000,
        "location": "France"
    },
    2: {
        "name": "Hiking in the Andes",
        "available": 5,
        "price": 500,
        "location": "Peru"
    },
    3: {
        "name": "Surfing in Hawaii",
        "available": 3,
        "price": 1500,
        "location": "USA"
    }
}


def delete_tour_task(id: int):
    time.sleep(10)
    if id in tours:
        del tours[id]
    else:
        print(f"Tour with id {id} not found (maybe already deleted)")

@app.delete("/tour/{id}")
async def delete_tour(id: int, background_tasks: BackgroundTasks):
    if id not in tours:
        raise HTTPException(status_code=404, detail="Tour not found")
    background_tasks.add_task(delete_tour_task, id)
    return {"message": "Tour deletion has been scheduled"}

@app.get("/tours")
async def get_tours():
    return tours