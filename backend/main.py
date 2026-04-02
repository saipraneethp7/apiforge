import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from generator import generate_api
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="APIForge", description="Generate production-ready APIs from plain English")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    description: str
    language: str
    framework: str

class GenerateResponse(BaseModel):
    title: str
    description: str
    routes: list
    code: str
    setup: str
    dependencies: list

@app.get("/")
def root():
    return {"message": "APIForge is running", "version": "1.0.0"}

@app.get("/frameworks")
def get_frameworks():
    return {
        "python": ["fastapi", "flask", "django"],
        "javascript": ["express", "fastify"],
        "go": ["gin", "echo"]
    }

@app.post("/generate")
def generate(request: GenerateRequest):
    if not request.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty")
    if len(request.description) < 10:
        raise HTTPException(status_code=400, detail="Please provide a more detailed description")
    if len(request.description) > 500:
        raise HTTPException(status_code=400, detail="Description too long, keep it under 500 characters")

    try:
        result = generate_api(
            description=request.description,
            language=request.language,
            framework=request.framework
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Generation failed. Please try again.")