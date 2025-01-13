from fastapi import APIRouter

router = APIRouter()

@router.post("/monitoring/register")
async def register_site(site_url: str):
    # Lógica para cadastrar um site
    return {"message": f"Site {site_url} cadastrado com sucesso!"}

@router.get("/monitoring/status")
async def get_status():
    # Lógica para verificar status
    return {"status": "Monitoramento em execução"}
