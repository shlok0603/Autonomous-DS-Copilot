from fastapi import FastAPI

app = FastAPI(
    title="Autonomous Data Science Co-Pilot",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "Running",
        "message": "Autonomous Data Science Co-Pilot API"
    }