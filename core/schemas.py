
from ninja import Schema
from typing import Optional
from datetime import time


class StatusNichoOutput(Schema):
    nicho_id: int
    status: bool
    nome_sala: str
    docente_nome: Optional[str] = None
    horario_retirada: Optional[time] = None
    horario_previsto: Optional[time] = None
