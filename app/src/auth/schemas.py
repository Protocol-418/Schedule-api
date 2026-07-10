from typing import Annotated
from pydantic import BaseModel, Field, EmailStr, StringConstraints
from uuid import UUID


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
     