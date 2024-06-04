import os
from dotenv import load_dotenv
from fastapi import FastAPI


app = FastAPI()

load_dotenv()  # Load environment variables from .env file

DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']

@app.get("/health")
async def checkHealth():
    return {"message": "healthy"}


@app.get("/env")
async def env_variables():
    return {"DEBUG": DEBUG}