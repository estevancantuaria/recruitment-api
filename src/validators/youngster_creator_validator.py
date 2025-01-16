from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_umprocessable_entity import HttpUnprocessableEntityError

def youngster_creator_validator(request: HttpRequest) -> None:
    
    class BodyData(BaseModel):
        nome: str
        email: str
        senha: str
        cpf: str
        telefone: str
        ativo: bool
        tipo_usuario: str
        rg: str
        data_nascimento: str
        
    try:
        BodyData(**request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
