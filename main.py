from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(
    title="My AI API",
    description="A starter AI API built with Python and FastAPI.",
    version="0.1.0",
)

@app.get("/", tags=["Health"])
def home():
    return {
        "status": "online",
        "message": "Welcome to My AI API",
        "docs": "/docs",
    }

app.include_router(chat_router, prefix="/api", tags=["Chat"])
