# Tutorial paso a paso: Pytest para principiantes

## ¿Qué es pytest?
Pytest es una herramienta que nos ayuda a **verificar que nuestro código funciona correctamente**. Es como un "revisor automático" que comprueba si nuestras funciones hacen lo que esperamos.

## Paso 1: Instalación
```bash
pip install pytest
```

## Paso 2: Crear archivos
Crea estos dos archivos en una carpeta:

1. `calculadora.py` (el código que queremos testear)
2. `test_calculadora.py` (los tests)

## Paso 3: Entender la estructura básica

### Un test simple se ve así:
```python
def test_sumar():
    # 1. Ejecutamos la función
    resultado = sumar(2, 3)
    
    # 2. Verificamos que sea correcto
    assert resultado == 5
```

### Reglas importantes:
- ✅ Los tests deben empezar con `test_`
- ✅ Usa `assert` para verificar resultados
- ✅ Un test = una cosa específica a verificar

## Paso 4: Ejecutar los tests

```bash
# Ejecutar todos los tests
pytest

# Ver más detalles
pytest -v

# Ejecutar un test específico
pytest test_calculadora.py::test_sumar
```

## Paso 5: Interpretar los resultados

### ✅ Test exitoso:
```
test_calculadora.py::test_sumar PASSED
```

### ❌ Test fallido:
```
test_calculadora.py::test_sumar FAILED
AssertionError: assert 6 == 5
```

## Tipos de tests que puedes hacer

### 1. Verificar que algo es igual
```python
def test_sumar():
    assert sumar(2, 3) == 5
```

### 2. Verificar que algo es verdadero/falso
```python
def test_es_par():
    assert es_par(4) is True
    assert es_par(5) is False
```

### 3. Verificar que se produce un error
```python
def test_error_division_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
```

### 4. Verificar texto
```python
def test_saludar():
    assert saludar("Ana") == "¡Hola, Ana!"
```

## Tests parametrizados (probar muchos casos a la vez)

En lugar de escribir muchos tests similares:
```python
def test_sumar_caso1():
    assert sumar(2, 3) == 5

def test_sumar_caso2():
    assert sumar(0, 0) == 0
    
# ... y así muchos más
```

Puedes usar parametrización:
```python
@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_sumar_varios_casos(a, b, esperado):
    assert sumar(a, b) == esperado
```

## Fixtures (datos reutilizables)

Si necesitas los mismos datos en varios tests:
```python
@pytest.fixture
def numeros():
    return {"pequeño": 5, "grande": 100}

def test_usando_fixture(numeros):
    assert sumar(numeros["pequeño"], 5) == 10
```

## Ejercicios para practicar

### Ejercicio 1: Test básico
Crea un test para verificar que `restar(10, 3)` da `7`.

### Ejercicio 2: Test de error
Crea un test que verifique que `dividir(5, 0)` produce un error.

### Ejercicio 3: Test parametrizado
Crea un test parametrizado para verificar que estos números son pares: 2, 4, 6, 8.

### Ejercicio 4: Test de texto
Crea una función que cuente cuántas palabras hay en un texto y haz un test para ella.

## Comandos útiles para empezar

```bash
# Ver qué tests se ejecutarían (sin ejecutarlos)
pytest --collect-only

# Parar en el primer error
pytest -x

# Mostrar output de print()
pytest -s

# Ejecutar solo tests que contienen "sumar"
pytest -k "sumar"
```

## Estructura de carpetas recomendada

```
mi-proyecto/
├── calculadora.py          # Tu código
├── test_calculadora.py     # Tus tests
└── README.md              # Documentación
```

## Consejos para empezar

1. **Empieza simple**: Un test por función, casos básicos
2. **Nombres descriptivos**: `test_sumar_numeros_positivos` es mejor que `test1`
3. **Un test, una cosa**: Cada test debe verificar una cosa específica
4. **Usa assert**: Es la forma más simple de verificar resultados
5. **Ejecuta tests frecuentemente**: Después de cada cambio pequeño

## ¿Por qué hacer tests?

- 🛡️ **Seguridad**: Sabes que tu código funciona
- 🐛 **Encontrar bugs**: Los tests te dicen dónde hay problemas
- 🔄 **Cambios seguros**: Puedes modificar código sin miedo
- 📝 **Documentación**: Los tests muestran cómo usar tu código

¡Empieza con estos ejemplos simples y ve aumentando la complejidad poco a poco!