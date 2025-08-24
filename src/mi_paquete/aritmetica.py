from __future__ import annotations

def suma(a: float, b: float) -> float:
    """Retorna la suma de dos números."""
    return a + b

def division_segura(a: float, b: float) -> float:
    """Retorna a/b verificando división por cero."""
    if b == 0:
        raise ZeroDivisionError("b no puede ser 0")
    return a / b
