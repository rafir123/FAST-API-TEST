from fastapi import FastAPI
from app.routers.endpoints.endpoints import router

app = FastAPI(debug=True)

app.include_router(router)