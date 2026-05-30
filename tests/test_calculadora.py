import pytest
from src.calculadora import dividir

# === 1. PRUEBAS DE CAMINO FELIZ (HAPPY PATH) ===
def test_dividir_enteros_positivos():
    assert dividir(10, 2) == 5.0

def test_dividir_resultado_decimal():
    assert dividir(5, 2) == 2.5

def test_dividir_numeros_negativos():
    assert dividir(-6, 3) == -2.0
    assert dividir(6, -3) == -2.0
    assert dividir(-6, -3) == 2.0
