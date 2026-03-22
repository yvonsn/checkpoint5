# 🐍 Fundamentos de Python para Principiantes

---

## 📑 Índice

- [¿Qué es un condicional?](#-qué-es-un-condicional-if--elif--else)
- [Sintaxis y ejemplos](#-sintaxis-básica)
- [¿Cuáles son los diferentes tipos de bucles en Python?](#-cuáles-son-los-diferentes-tipos-de-bucles-en-python)
- [Bucle for](#-bucle-for)
- [Bucle while](#-bucle-while)
- [¿Qué es una lista por comprensión en Python?](#-qué-es-una-lista-por-comprensión-en-python)
- [¿Qué es un argumentos en Python?](#-qué-es-un-argumento-en-python)
- [¿Qué es una función Lambda en Python?](#-qué-es-una-función-lambda-en-python)
- [¿Qué es un paquete pip?](#-qué-es-un-paquete-pip)

---

## 🔹 ¿Qué es un condicional? (`if / elif / else`)

En la vida cotidiana, una condición es una situación en la que debes tomar una decisión entre dos o más opciones.

Ejemplo:
Si vas a tomar café, debes decidir si le pones azúcar o no.

En programación ocurre lo mismo: muchas veces necesitamos que el programa tome decisiones según diferentes factores. Para eso usamos las condicionales, que permiten ejecutar distintos bloques de código según una condición.

### 💻 Sintaxis básica

![if](/documentos-markdown/images/if.png)

### 💡 Ejemplo: Máquina de café

#### if simple

```python
print("Máquina de café")
print("Quieres el café con azúcar presiona 1")

opcion = int(input())

if opcion == 1:
    print("Preparando café con azúcar...")
```

#### if/else

```python
print("Máquina de café")
print("¿Quieres el café con azúcar? 1. Sí / 2. No")

opcion = int(input())

if opcion == 1:
    print("Preparando café con azúcar...")
else:
    print("Preparando café sin azúcar...")
```

#### elif (múltiples funciones)

```python
print("Cómo quieres el café? 1. Azúcar / 2. Sacarina / 3. Solo")

opcion = int(input())

if opcion == 1:
    print("Preparando café con azúcar")
elif opcion == 2:
    print("Preparando café con sacarina")
else:
    print("Preparando café solo")
```

### Conceptos clave

- if → “si”

- elif → “si no, pero si…”

- else → “en cualquier otro caso”

- La indentación es obligatoria

---

## 🔹 ¿Cuáles son los diferentes tipos de bucles en Python?

Los bucles son importantes en cualquier lenguaje de programación, porque permiten repetir un bloque de código mientras se cumpla una condición. En Python tenemos:

## 🔹 Bucle for

Nos permite repetir un bloque. Se usa cuando sabemos cuántas veces repetir o queremos recorrer una colección.

### 💻 Sintaxis

```python
for variable in iterable:
    # código a repetir
```

![For](/documentos-markdown/images/for.png)

### 💡 Ejemplos

#### Imprimir 5 asteriscos

```python
for x in range(5):
    print("*")
```

Imprime:

\* <br>\*<br> \*<br> \*<br> \*

#### Recorrer un string

```python
for letra in "hola":
    print(letra)
```

Imprime:

h<br>o<br>l<br>a

#### Recorrer una lista

```python
dias = ["lunes", "martes", "miércoles"]
for dia in dias:
    print(dia)
```

lunes<br>martes<br>miércoles

### 🔧 break y continue

modifican el flujo normal del bucle.

- break → termina el bucle, dando paso a la instrucción que viene después.
- continue → salta a la siguiente iteración.

#### Creamos un programa que recorra un diccionario de calificaciones que al encontrar un 10 escribe: Qué máquina!, si hay menores de 5 no los lee y si hay un 2 termina el programa e imprime Caso perdido!.

```python
calificaciones = {
"Ana": 7,
"Luis": 4,
"Marta": 10,
"Carlos": 2
}
for nombre, nota in calificaciones.items():
    if nota == 2:
        print(nombre, "→ Caso perdido!")
        break
    if nota < 5:
        continue
    if nota == 10:
        print(nombre, "→ ¡Qué máquina!")
else:
    print(nombre, "→ Bien")
```

## 🔹 Bucle while

Ejecuta un bloque de código repetidas veces, mientras la condición del bucle sea verdadera. a diferencia de for, no se sabe de antemano cuántas veces se ejecutará. Cuando la condición sea falsa, el bucle termina y continúa la ejecución normal del programa.

### 💻 Sintaxis

![while](/documentos-markdown/images/while.png)

### 💡 Ejemplos

#### Imprimir 5 asteriscos

```python
x = 0
while x < 5:
    print("*")
    x += 1
```

#### Esperar condición del usuario

```python
entrada = ""
while entrada.lower() != "s":
    entrada = input("Escribe 'S' para salir: ")
```

#### Break y continue

```python
contador = 0

while True:
    contador += 1
    if contador == 3:
        continue
    if contador > 5:
        break
    print(contador)
```

---

## 🔹 ¿Qué es una lista por comprensión en Python?

Es una funcionalidad que nos permite crear listas avanzadas de una forma compacta y elegante, en una sola línea de código, a partir de un iterable (como una cadena, lista o rango) aplicando opcionalmente condiciones o transformaciones.

### 💻 Sintaxis

![Comprension](/documentos-markdown/images/comprension.png)

### 💡 Ejemplos

#### Crear una lista con las Letras de la palabra "Python"

| Método Tradicional                                                                               | Lista de comprensión                                    |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| lista = [ ]<br>for letras in "Python":<br>&nbsp;&nbsp;&nbsp;lista.append(letras)<br>print(lista) | lista = [letras for letras in "Python"]<br>print(lista) |

Resultado de ambos métodos: ['P', 'y', 't', 'h', 'o', 'n']

#### Crear una lista con el cuadrado de los número del 0 al 10

| Método Tradicional                                                                                                 | Lista de comprensión                                 |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| lista = [ ]<br>for n in range(0, 11):<br>&nbsp;&nbsp;&nbsp;lista.append(n\*\*2)<br>&nbsp;&nbsp;&nbsp;print(letras) | lista = [n**2 for n in range(0, 11)]<br>print(lista) |

Resultado de ambos métodos: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

---

## 🔹 ¿Qué es una función Lambda en Python?

Es una forma corta de declarar funciones pequeñas y anónimas (no es necesario dar un nombre para las funciones Lambda). Son ideales cuando necesitamos hacer operaciones rápidas y simples. Pueden contener solo una expresión.

### 💻 Sintaxis

![Lambda](/documentos-markdown/images/lambda.png)

### 💡 Ejemplos

| Método Tradicional                                                             | Función Lambda                                         |
| ------------------------------------------------------------------------------ | ------------------------------------------------------ |
| def cuadrado(x):<br>&nbsp;&nbsp;&nbsp;return x\*\*2<br><br>print(cuadrado(21)) | cuadrado = lambda x: x\*\*2<br><br>print(cuadrado(21)) |

Resultado para ambos métodos: 441

---

## 🔹 ¿Qué es un argumento en Python?

Son los valores que se pasan a una función para que trabaje con información específica.

![Visualmente](/documentos-markdown/images/parametros.png)

### 💡 Ejemplos

#### Suma

```python
def sumar(a, b):
    return a + b

print(sumar(5, 6)) # 11
```

#### Saludo

```python
def saludar(nombre):
    return "Hola, " + nombre

print(saludar("Celeste")) # Hola, Celeste
```

---

## 🔹 ¿Qué es un paquete pip?

Es un gestor de paquetes, que se encarga de instalar, actualizar y eliminar paquetes que no forman parte de la biblioteca estándar.

### 💻 Sintaxis:

#### Instalar

```python
pip install nombre_del_paquete
```

#### Desinstalar

```python
pip uninstall nombre_del_paquete
```

#### Actualizar

```python
pip install --upgrade nombre_del_paquete
```

### 💡 Ejemplo práctico

```python
import requests

respuesta = requests.get("https://api.github.com")
print(respuesta.status_code) # 200

```
