import json
import pandas as pd
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from typing import Dict
from pydantic import BaseModel
from orch import orchestrator

app = FastAPI()
security = HTTPBasic()

#Fake Database
user_db : Dict[str, Dict[str,str]] = {
    "Tony": {
        "password": "password123",
        "role": "engineering",
        "employee_id": "FINEMP1012"
    },
    "Bruce": {
        "password": "securepass",
        "role": "marketing",
        "employee_id": "FINEMP1000"
    },
    "Sam": {
        "password": "financepass",
        "role": "finance",
        "employee_id": "FINEMP1010"
    },
    "Peter": {
        "password": "pete123",
        "role": "engineering",
        "employee_id": "FINEMP1011"
    },
    "Sid": {
        "password": "sidpass123",
        "role": "marketing",
        "employee_id": "FINEMP1001"
    },
    "Natasha": {
        "password": "hrpass123",
        "role": "hr",
        "employee_id": "FINEMP1002"
    }
}

class ChatRequest(BaseModel):
    message: str

def authentication (credentials :HTTPBasicCredentials = Depends(security) ):
    username = credentials.username
    password = credentials.password
    user = user_db.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "username": username,
        "role": user["role"],
        "employee_id": user["employee_id"]
    }

@app.get("/login")
def login(user = Depends(authentication)):
    return {
        "message": f"Welcome {user['username']}!",
        "role": user["role"],
        "employee_id": user["employee_id"]
    }

@app.post("/chat")
def chat(request: ChatRequest, user = Depends(authentication)):
    answer = orchestrator(
        query=request.message,
        employee_id=user["employee_id"],
        role = user["role"]
    )
    return {"bot_response": answer}