from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from routes.timebooking_routes import router as timebooking_router
#from models.timebooking import Base as TimebookingBase
from backend.config.database import engine
from fastapi.staticfiles import StaticFiles
import sys
import os

# Voeg de backend-map toe aan het Python-pad
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Create tables
#TimebookingBase.metadata.create_all(bind=engine)

app = FastAPI(title="Timebooking", version="1.0.0")

# CORS middleware for Vue frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://localhost:8080'],
    allow_credentials=True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

# Include routers
#app.include_router(timebooking_router)

@app.get("/")
async def root():
    return {"message": "Timebooking API is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)