from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re

app = FastAPI()

# Request Model
class RequestModel(BaseModel):
    data: List[str]

# Helper function to separate numbers and alphabets
def process_data(data: List[str]):
    numbers = [item for item in data if re.fullmatch(r'\d+', item)]
    alphabets = [item for item in data if re.fullmatch(r'[a-zA-Z]', item)]

    highest_alphabet = max(alphabets, key=lambda c: c.lower()) if alphabets else None
    return numbers, alphabets, [highest_alphabet] if highest_alphabet else []

# POST Endpoint
@app.post("/bfhl")
def process_request(request: RequestModel):
    numbers, alphabets, highest_alphabet = process_data(request.data)

    response = {
        "is_success": True,
        "user_id": "puneet_thapliyal_27022005",  # Replace with your format
        "email": "22BCS13944@cuchd.in",
        "roll_number": "22BCS13944",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
    return response

# GET Endpoint
@app.get("/bfhl")
def get_operation_code():
    return {"operation_code": 1}




