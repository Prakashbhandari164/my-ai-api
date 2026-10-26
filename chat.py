from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)

class ChatResponse(BaseModel):
    reply: str

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Starter response only. Connect a real AI model in app/services/ai_service.py.
    return ChatResponse(
        reply=f"Your API received: {request.message}. Real AI integration is not configured yet."
    )
