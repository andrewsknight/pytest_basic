# test_calculadora.py - Tests simples para aprender
"""
Tests súper simples para entender pytest paso a paso.
"""

import pytest
from calculadora import sumar, restar, multiplicar, dividir, es_par, saludar, contar_vocales

# ===== TESTS BÁSICOS =====
# Los tests son funciones que empiezan con "test_"

def test_sumar_numeros_positivos():
    """Test: sumar números positivos."""
    # Ejecutamos la función
    resultado = sumar(2, 3)
    
    # Verificamos que el resultado sea correcto
    assert resultado == 6

def test_sumar_numeros_negativos():
    """Test: sumar números negativos."""
    resultado = sumar(-2, -3)
    assert resultado == -5

def test_restar():
    """Test: restar números."""
    resultado = restar(10, 3)
    assert resultado == 7

def test_multiplicar():
    """Test: multiplicar números."""
    resultado = multiplicar(4, 5)
    assert resultado == 20

# ===== TEST QUE VERIFICA ERRORES =====
def test_dividir_por_cero():
    """Test: dividir por cero debe dar error."""
    # Verificamos que se produce un error específico
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_dividir_normal():
    """Test: división normal."""
    resultado = dividir(10, 2)
    assert resultado == 5.0

# ===== TESTS CON DIFERENTES TIPOS DE DATOS =====
def test_es_par_con_numero_par():
    """Test: número par devuelve True."""
    resultado = es_par(4)
    assert resultado is True

def test_es_par_con_numero_impar():
    """Test: número impar devuelve False."""
    resultado = es_par(5)
    assert resultado is False

def test_saludar_con_nombre():
    """Test: saludar con un nombre."""
    resultado = saludar("Ana")
    assert resultado == "¡Hola, Ana!"

def test_saludar_sin_nombre():
    """Test: saludar sin nombre."""
    resultado = saludar("")
    assert resultado == "¡Hola, desconocido!"

def test_contar_vocales():
    """Test: contar vocales en texto."""
    resultado = contar_vocales("Hola mundo")
    assert resultado == 4  # o, a, u, o

# ===== TESTS MÁS AVANZADOS (PERO SIMPLES) =====

def test_multiple_asserts():
    """Test: múltiples verificaciones en un test."""
    # Podemos hacer varias verificaciones en un test
    assert sumar(1, 1) == 2
    assert sumar(0, 5) == 5
    assert sumar(-1, 1) == 0

def test_con_variables():
    """Test: usando variables para mayor claridad."""
    # Usar variables hace el test más claro
    primer_numero = 15
    segundo_numero = 5
    resultado_esperado = 3
    
    resultado_real = dividir(primer_numero, segundo_numero)
    assert resultado_real == resultado_esperado

# ===== TESTS PARAMETRIZADOS (SIMPLES) =====
@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),      # 2 + 3 = 5
    (0, 0, 0),      # 0 + 0 = 0
    (-1, 1, 0),     # -1 + 1 = 0
    (10, -5, 5),    # 10 + (-5) = 5
])
def test_sumar_varios_casos(a, b, esperado):
    """Test: probar varios casos de suma."""
    resultado = sumar(a, b)
    assert resultado == esperado

@pytest.mark.parametrize("numero, es_par_esperado", [
    (2, True),      # 2 es par
    (3, False),     # 3 es impar
    (0, True),      # 0 es par
    (-2, True),     # -2 es par
    (-3, False),    # -3 es impar
])
def test_es_par_varios_casos(numero, es_par_esperado):
    """Test: probar si varios números son pares."""
    resultado = es_par(numero)
    assert resultado == es_par_esperado

# ===== EJEMPLO DE FIXTURE (MUY SIMPLE) =====
@pytest.fixture
def numeros_para_test():
    """Fixture: números que usaremos en varios tests."""
    return {"pequeño": 5, "mediano": 50, "grande": 500}

def test_usando_fixture(numeros_para_test):
    """Test: usando una fixture."""
    # Podemos usar los datos de la fixture
    assert sumar(numeros_para_test["pequeño"], 5) == 10
    assert multiplicar(numeros_para_test["mediano"], 2) == 100