from datetime import date
from typing import Annotated
from pydantic import BaseModel, Field, EmailStr, StringConstraints, field_validator
from enum import Enum

class UserType(str, Enum):
    YOUNGSTER = "YOUNGSTER"
    RECRUITER = "RECRUITER"

class YoungsterInputDTO(BaseModel):
    # Campos herdados de User
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    cpf: Annotated[str, StringConstraints(min_length=11, max_length=11, pattern=r'^\d{11}$')]
    birth_date: date
    cellphone: Annotated[str, StringConstraints(pattern=r'^\+?1?\d{9,15}$')]
    password: str = Field(..., min_length=8)
    
    # Campo específico do Youngster
    rg: Annotated[str, StringConstraints(min_length=1, max_length=20)]

    @field_validator('birth_date')
    def validate_birth_date(cls, v):
        if v > date.today():
            raise ValueError('Birth date cannot be in the future')
        return v

    @field_validator('name')
    def name_must_be_stripped(cls, v):
        return v.strip()

    class Config:
        from_attributes = True