# escenario1.py

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
    print("¿Qué impacto tiene este umbral?")
    print("¿Debería el umbral ser igual para todos los grupos, o distinto para promover equidad?")


def ejecutar_escenario():
    """Ejecuta el escenario de asignación de recursos."""
    print("=== Escenario 1: Asignación de recursos basada en puntaje y grupo ===")
    for i in range(1, 3):
        puntaje, grupo, umbral = obtener_datos_solicitante(i)
        mostrar_resultado(puntaje, umbral, grupo)


if __name__ == "__main__":
    ejecutar_escenario()
