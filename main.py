from fastapi import FastAPI

from src.apps.project.api import router as project_router

app = FastAPI()

app.include_router(project_router, prefix="/api/v1/users", tags=["users"])
