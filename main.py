from fastapi import FastAPI


app = FastAPI()

@app.get("/health")
async def checkHealth():
    return {"message": "healthy"}