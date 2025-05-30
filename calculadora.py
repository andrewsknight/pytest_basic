# calculadora.py - Funciones simples para testear
"""
Calculadora básica para aprender pytest.
"""

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def es_par(numero):
    """Verifica si un número es par."""
    return numero % 2 == 0

def saludar(nombre):
    """Saluda a una persona."""
    if not nombre:
        return "¡Hola, desconocido!"
    return f"¡Hola, {nombre}!"

def contar_vocales(texto):
    """Cuenta las vocales en un texto."""
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador