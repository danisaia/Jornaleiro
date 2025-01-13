from fastapi import APIRouter

router = APIRouter()

@router.get("/analysis/keywords")
async def get_keywords():
    # Lógica para retornar palavras-chave
    return {"keywords": ["exemplo", "notícia", "análise"]}

@router.get("/analysis/entities")
async def get_entities():
    # Lógica para retornar entidades
    return {"entities": ["Organização A", "Local B"]}
