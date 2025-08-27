# Decisiones IA Ética

## 📘 Descripción

Este proyecto aborda la asignación de recursos en escenarios donde se aplican umbrales diferenciados por grupo, con el objetivo de promover la equidad. A través de un programa en Python, se simulan decisiones de asignación basadas en puntajes y grupos, generando reflexiones éticas sobre la justicia y el impacto de estas decisiones.

## 🎯 Objetivo

El propósito del programa es:

- Simular la asignación de recursos considerando diferentes umbrales por grupo.
- Generar reflexiones éticas sobre la justicia y el impacto de estas decisiones.
- Proporcionar una herramienta para analizar y discutir la equidad en la asignación de recursos.

## 👥 Integrantes del Grupo

- **Miembro 1**: JHONATAN MACANCELA
-

## 📅 Fecha

- **Fecha de inicio**: 26 DE AGOSTO DEL 2025

## ⚙️ Requisitos

- Python 3.x
- [Otras dependencias, si las hay]

## # Decisiones IA Ética - Escenarios 1 y 2

def escenario1():
    print("¡Hola, mundo!")

def escenario2():
    print("=== Escenario 2: Comparación entre grupos ===")
    
    # Solicitar datos del solicitante 1
    puntaje1 = float(input("Ingrese puntaje del solicitante 1 (0-100): "))
    grupo1 = input("Grupo del solicitante 1 (A/B): ").upper()
    umbral1 = float(input(f"Umbral aplicado al grupo {grupo1} (0-100): "))
    
    # Solicitar datos del solicitante 2
    puntaje2 = float(input("Ingrese puntaje del solicitante 2 (0-100): "))
    grupo2 = input("Grupo del solicitante 2 (A/B): ").upper()
    umbral2 = float(input(f"Umbral aplicado al grupo {grupo2} (0-100): "))
    
    # Mostrar resultados
    print("\n=== Resultados y reflexión ===")
    
    # Evaluar solicitante 1
    print(f"\nGrupo {grupo1} – Puntaje: {puntaje1} – Umbral: {umbral1}")
    if puntaje1 >= umbral1:
        print("→ Recurso asignado.")
    else:
        print("→ Recurso no asignado.")
    reflexion1 = "¿Es justo este resultado? ¿Qué impacto tiene este umbral?"
    print(reflexion1)
    
    # Evaluar solicitante 2
    print(f"\nGrupo {grupo2} – Puntaje: {puntaje2} – Umbral: {umbral2}")
    if puntaje2 >= umbral2:
        print("→ Recurso asignado.")
    else:
        print("→ Recurso no asignado.")
    reflexion2 = "¿Es justo este resultado? ¿Qué impacto tiene este umbral?"
    print(reflexion2)
    
    # Comparar umbrales
    if umbral1 == umbral2:
        print("\nLos umbrales son iguales para ambos grupos.")
        equidad = "¿Debería el umbral ser igual para todos los grupos, o distinto para promover equidad?"
        print(equidad)
    else:
        print("\nLos umbrales son diferentes para los grupos.")
        equidad = "¿Debería el umbral ser igual para todos los grupos, o distinto para promover equidad?"
        print(equidad)

# Ejecutar ambos escenarios
escenario1()
escenario2()

Copia el código proporcionado y pégalo en un archivo de texto. Guarda el archivo con el nombre decisiones_ia_etica.py en tu computadora.

Ejecutar el código:

Abre una terminal o línea de comandos.

Navega hasta el directorio donde guardaste el archivo decisiones_ia_etica.py.

Ejecuta el siguiente comando:python decisiones_ia_etica.py

El programa te solicitará que ingreses los puntajes, grupos y umbrales para dos solicitantes. Después de ingresar los datos, el programa mostrará los resultados y las reflexiones éticas correspondientes.