"""Módulo voltado para models que serão reutilizados no projeto."""

from pydantic import BaseModel

class ErrorModel(BaseModel):
    """Model para retornar erros personalizados"""
    message: str
    execption: str
