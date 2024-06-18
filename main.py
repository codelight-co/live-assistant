from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas.models import HealthResponse
from routes.admin import router as admin_router
from routes.auth import router as auth_router
from routes.posts import router as posts_router
from routes.company import router as company_router
from routes.rag import router as rag_router
from routes.ai_agent import router as ai_agent_router
from ai_models.app import router as ai_model

app = FastAPI()

# Enable CORS (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=auth_router, prefix="/auth")
app.include_router(router=ai_model, prefix="/ai")
app.include_router(router=admin_router, prefix="/admin")
app.include_router(router=company_router, prefix="/companies")
app.include_router(router=rag_router, prefix="/rag")
app.include_router(router=ai_agent_router, prefix="/ai-agent")



@app.get("/", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")