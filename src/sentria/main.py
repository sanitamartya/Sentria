from fastapi import FastAPI

from sentria.config import settings


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)


@app.get("/")
def root():
    return {"message": "Sentria is running"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": settings.app_name,
        "environment": settings.environment,
    }
