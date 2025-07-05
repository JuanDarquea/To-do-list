lista_tareas = [] # Definición de lista vacía adónde se guardarán las tareas. 

# Esta lista almacenará las tareas del usuario.
# Cada tarea será un diccionario con los siguientes campos:
tarea = {  # Definición de tarea como diccionario:
    # 'id': Identificador único de la tarea.
    'id': 1, 
    'titulo': 'Estudiar Python', # Título de la tarea.
    'descripcion': 'Aprender CRUD básico', # Descripción de la tarea.
    'completada': False, # Estado de la tarea (completada o no).
    'fecha_creacion': '2025/01/15', # Fecha de creación de la tarea.
    'fecha_limite': '2025-01-20' # Fecha límite para completar la tarea.
    } # Cerramos el diccionario de tarea.

# Variable para generar IDs únicos
contador_id = 1

def mostrar_menu(): # Definición de función para mostrar el menú principal
    """Muestra el menú principal de opciones"""
    print("\n=== LISTA DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Modificar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("=" * 23)

def agregar_tarea(): # Definición de función para agregar una nueva tarea
    """Agrega una nueva tarea a la lista"""
    global contador_id  # Necesitamos modificar esta variable globalmente
    
    # Pedimos los datos al usuario
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción: ")
    fecha_limite = input("Fecha límite (YYYY-MM-DD) o Enter para omitir: ")
    
    # Crear el diccionario de la tarea
    nueva_tarea = {
        'id': contador_id,
        'titulo': titulo,
        'descripcion': descripcion,
        'completada': False,
        'fecha_creacion': '2025-01-15',  # Por ahora fijo
        'fecha_limite': fecha_limite if fecha_limite else None
    }
    
    # Agregar a la lista
    lista_tareas.append(nueva_tarea)
    contador_id += 1
    
    print(f"\nTarea '{titulo}' agregada correctamente!")
    pause = input("\nPresiona Enter volver al menu...")

def ver_tareas(): # Definición de función para ver todas las tareas
    """Muestra todas las tareas en la lista"""
    #global lista_tareas  # Necesitamos acceder a la lista global
    # Primero verificamos si hay tareas
    if not lista_tareas:
        print("\n📝 No hay tareas en la lista.")
        return
    
    print(f"\n📋 LISTA DE TAREAS ({len(lista_tareas)} tareas)")
    print("=" * 50)
    
    # Recorremos cada tarea y la mostramos
    for tarea in lista_tareas:
        # Símbolo según el estado
        simbolo = "✅" if tarea['completada'] else "⏳"
        
        print(f"{simbolo} ID: {tarea['id']}")
        print(f"   Título: {tarea['titulo']}")
        print(f"   Descripción: {tarea['descripcion']}")
        print(f"   Fecha creación: {tarea['fecha_creacion']}")
        
        # Solo mostrar fecha límite si existe
        if tarea['fecha_limite']:
            print(f"   Fecha límite: {tarea['fecha_limite']}")
        
        print("-" * 30)

def main(): # Definición de la función principal
    """Función principal del programa"""
    while True: # Bucle infinito para mantener el programa en ejecución
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            print("\nAgregar tarea\n") 
            agregar_tarea() # Llamar a la función para agregar una tarea
        elif opcion == "2":
            ver_tareas() # Llamar a la función para ver todas las tareas
            pause = input("\nPresiona Enter volver al menu...") # Pausa para que el usuario vea las tareas
        elif opcion == "3":
            print("\nFunción modificar tarea - por implementar")
        elif opcion == "4":
            print("\nFunción eliminar tarea - por implementar")
        elif opcion == "5":
            print("\nSaliendo del programa...") # Mensaje de salida
            # Aquí podríamos guardar las tareas en un archivo si quisieramos persistencia
            # Por ahora solo salimos
            print("¡Hasta luego!\n")
            break # Salir del bucle y terminar el programa
        else:
            print("Opción inválida. Intenta de nuevo.") # Mensaje de error si la opción no es válida

# Ejecutar el programa
if __name__ == "__main__": # Comprobar si el script se está ejecutando directamente
    print("Bienvenido a la lista de tareas") # Mensaje de bienvenida
    main() # Llamar a la función principal para iniciar el programa