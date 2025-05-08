from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from API.v1.routes import router as api_router
from core.db import int_db

int_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods= ["*"],
    allow_headers=["*"]
)

app.include_router(api_router,prefix="/API/v1",tags=["AI study Buddy"])

@app.get("/")
async def root():
    return {"message":"welcomme to AI study Buddy API!"}