from fastapi import FastAPI, Response, Request
from typing import List,Dict
from datetime import datetime
import hashlib

app = FastAPI()

# Simulate DB
tours : List[Dict] = [
    {
        "id": 1,
        "name": "Skiing in the Alps",
        "customers": []
    },
    {
        "id": 2,
        "name": "Hiking in the Andes",
        "customers": []
    },
    {
        "id": 3,
        "name": "Surfing in Hawaii",
        "customers": []
    }
]

# Simulate DB modification Time
last_modified = datetime.now()

def generate_strong_etag(tours):
    data = "".join([f'{tour["id"]}{tour["name"]}{tour["customers"]}' for tour in tours])
    return hashlib.md5(data.encode()).hexdigest()

def generate_weak_etag(tours):
    data = "".join([f'{tour["id"]}{tour["name"]}' for tour in tours])
    return f'W/"{hashlib.md5(data.encode()).hexdigest()}"' # W/ to symbolize weak etag

@app.get("/tours")
async def get_tours(request: Request, response: Response):
    # Check if the If-Modified-Since header is present
    if_modified_since = request.headers.get("If-Modified-Since")
    if if_modified_since:
        print(if_modified_since)
        request_time = datetime.strptime(if_modified_since, "%a, %d %b %Y %H:%M:%S %Z")
        if request_time >= last_modified:
            response.status_code = 304
            return

    if_none_match = request.headers.get("If-None-Match")
    if if_none_match:
        weak_etag = generate_weak_etag(tours)
        strong_etag = generate_strong_etag(tours)
        print(f'if_none_match: {if_none_match}')
        print(f'weak_etag: {weak_etag}')
        print(f'strong_etag: {strong_etag}')
        if if_none_match in (weak_etag, strong_etag):
            response.status_code = 304
            return
    
    response.headers["Last-Modified"] = last_modified.strftime("%A, %d %B %Y %H:%M:%S")
    response.headers["ETag"] = generate_strong_etag(tours)
    return tours