# escenario2.py

def asignar_recurso(puntaje, umbral):
    """Determina si un solicitante recibe el recurso según su puntaje y el umbral."""
    return puntaje >= umbral


def obtener_umbral_por_grupo(grupo):
    """Asigna un umbral específico según el grupo del solicitante."""
    umbrales = {'A': 50, 'B': 40}  # Umbrales diferenciados por grupo
    return umbrales.get(grupo, 50)  # Valor por defecto: 50


def obtener_datos_solicitante(numero):
    """Solicita al usuario los datos de un solicitante."""
    puntaje = float(
        input(f"Ingrese puntaje del solicitante {numero} (0-100): "))
    grupo = input(f"Grupo del solicitante {numero} (A/B): ").upper()
    umbral = obtener_umbral_por_grupo(grupo)
    return puntaje, grupo, umbral


def mostrar_resultado(puntaje, umbral, grupo):
    """Muestra los resultados y reflexiones éticas."""
    asignado = asignar_recurso(puntaje, umbral)
    resultado = "Recurso asignado." if asignado else "Recurso no asignado."
    print(f"\nGrupo {grupo} – Puntaje: {puntaje} – Umbral: {umbral}")
    print(f"→ {resultado}")
    print("\n¿Es justo este resultado?")
    print("Aplicar umbrales diferenciados puede ser considerado justo si se reconoce que los grupos pueden haber enfrentado desventajas históricas o estructurales. Por ejemplo, si el Grupo B ha tenido menos acceso a recursos educativos, un umbral más bajo para este grupo puede ayudar a nivelar el campo de juego.")
    print("\n¿Qué impacto tiene este umbral?")
    print("Los umbrales diferenciados pueden tener varios impactos: positivos, como promover la equidad al proporcionar a grupos desfavorecidos una oportunidad justa de acceder a recursos; y negativos, si no se implementan adecuadamente, pueden generar percepciones de injusticia entre los grupos no beneficiados.")
    print("\n¿Debería el umbral ser igual para todos los grupos, o distinto para promover equidad?")
    print("La equidad no siempre implica igualdad. En contextos donde existen disparidades históricas o estructurales, aplicar umbrales iguales puede perpetuar esas desigualdades. Por lo tanto, establecer umbrales diferenciados puede ser una estrategia válida para promover la equidad.")


def ejecutar_escenario():
    """Ejecuta el escenario de asignación de recursos."""
    print("=== Escenario 2: Comparación entre grupos ===")
    for i in range(1, 3):
        puntaje, grupo, umbral = obtener_datos_solicitante(i)
        mostrar_resultado(puntaje, umbral, grupo)


if __name__ == "__main__":
    ejecutar_escenario()
