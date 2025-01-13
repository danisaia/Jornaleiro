from fastapi import APIRouter

router = APIRouter()

@router.get("/stats/topics")
async def get_topics():
    # Lógica para consultar tópicos
    return {"topics": ["Política", "Tecnologia"]}

@router.get("/stats/entities")
async def get_stats_entities():
    # Lógica para consultar entidades mais citadas
    return {"entities": ["Pessoa X", "Organização Y"]}
