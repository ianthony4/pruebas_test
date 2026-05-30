import pytest
from src.calculadora import dividir

# === 1. PRUEBAS DE CAMINO FELIZ (HAPPY PATH) ===
def test_dividir_enteros_positivos():
    assert dividir(10, 2) == 5.0

