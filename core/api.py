
from ninja import NinjaAPI
from typing import List
from uuid import UUID

from core.schemas import StatusNichoOutput
from core.utils import buscar_status_nicho_banco

api = NinjaAPI(
    title="Key_track API",
    version="1.0.0",
    description="API de gerenciamento do sistema Key_track"
)


@api.get("/status/", tags=["Sistema"])
def status(request):
    return {
        "mensagem": "Key_track API funcionando!",
        "status": True
    }


@api.get(
    "/status-nichos/",
    response=List[StatusNichoOutput],
    tags=["Nichos"]
)
def listar_status_nichos(request):
    return buscar_status_nicho_banco()


@api.get("/consulta-uuid/{uuid}", tags=["Consultas"])
def consulta_uuid(request, uuid: UUID):
    return {
        "mensagem": "UUID recebido com sucesso",
        "uuid": str(uuid)
    }
