from fastapi import FastAPI
from app.routers import monitoring, analysis, stats

app = FastAPI()

# Registrar os routers
app.include_router(monitoring.router, prefix="/api/v1", tags=["Monitoring"])
app.include_router(analysis.router, prefix="/api/v1", tags=["Analysis"])
app.include_router(stats.router, prefix="/api/v1", tags=["Stats"])

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao backend do Jornaleiro!"}
