import json
lista_tareas = [] # Definición de lista vacía adónde se guardarán las tareas. 
contador_id = 1

def pause():
    input("\nPresiona Enter volver al menu...") 

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
    if not lista_tareas: # Si la lista está vacía
        # Mostramos un mensaje y salimos
        print("\n📝 No hay tareas en la lista.")
        pause()
        return
    # Si hay tareas, mostramos el encabezado
    print(f"\n📋 LISTA DE TAREAS ({len(lista_tareas)} tareas)") # Encabezado: utiliza la función `len` para dar un conteo de las tareas totales. 
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
    else: pause() # Pausa agregada al final del if. 

def modificar_tarea(): # Definición de función para modificar una tarea existente
    """Modifica una tarea existente en la lista"""
    
        # Verificar si hay tareas
    if not lista_tareas:
        print("\n📝 No hay tareas para modificar.")
        pause()
        return # Si no hay tareas, regresamos al main. 
    
    # Mostrar tareas disponibles
    print(f"\n{len(lista_tareas)} TAREAS DISPONIBLES:") #Encabezado de lista de tareas disponibles con un contador de cuántas tareas tiene. 
    for tarea in lista_tareas:
        estado = "✅" if tarea['completada'] else "⏳"
        print(f"{estado} ID: {tarea['id']} - {tarea['titulo']}")
    
    # Pedir el ID de la tarea a modificar
    try:
        id_buscar = int(input("\nIngresa el ID de la tarea a modificar: "))
    except ValueError:
        print("\n❌ Por favor ingresa un número válido.")
        return
    
    # Buscar la tarea
    tarea_encontrada = None
    for tarea in lista_tareas:
        if tarea['id'] == id_buscar:
            tarea_encontrada = tarea
            break
    
    if not tarea_encontrada:
        print("\n❌ No se encontró una tarea con ese ID.")
        return
    
    # Mostrar opciones de modificación
    print(f"\n🔧 Modificando tarea: {tarea_encontrada['titulo']}")
    print("¿Qué deseas modificar?")
    print("1. Título")
    print("2. Descripción")
    print("3. Marcar como completada/pendiente")
    print("4. Fecha límite")
    
    opcion = input("\nSelecciona una opción (1-4): ")
    
    if opcion == "1":
        nuevo_titulo = input("\nNuevo título: ")
        tarea_encontrada['titulo'] = nuevo_titulo
        print("\n✅ Título actualizado!")
        pause()
    elif opcion == "2":
        nueva_descripcion = input("\nNueva descripción: ")
        tarea_encontrada['descripcion'] = nueva_descripcion
        print("\n✅ Descripción actualizada!")
        pause()
    elif opcion == "3":
        tarea_encontrada['completada'] = not tarea_encontrada['completada']
        estado_nuevo = "completada" if tarea_encontrada['completada'] else "pendiente"
        print(f"\n✅ Tarea marcada como {estado_nuevo}!")
        #pause()
    elif opcion == "4":
        nueva_fecha = input("\nNueva fecha límite (YYYY-MM-DD) o Enter para quitar: ")
        tarea_encontrada['fecha_limite'] = nueva_fecha if nueva_fecha else None
        print("\n✅ Fecha límite actualizada!")
        pause()
    else:
        print("\n❌ Opción inválida.")
        #pause()

def eliminar_tarea(): # Definición de función para eliminar una tarea existente
    """Elimina una tarea de la lista"""
    
    # Verificar si hay tareas
    if not lista_tareas: # Si la lista está vacía
        # Mostrar mensaje y regresar
        print("\n📝 No hay tareas para eliminar.")
        pause()
        return
    
    # Mostrar tareas disponibles
    print(f"\n📋{len(lista_tareas)} TAREAS DISPONIBLES:") 
    for tarea in lista_tareas: # Recorremos la lista de tareas
        estado = "✅" if tarea['completada'] else "⏳" # Determinamos el estado de la tarea
        print(f"{estado} ID: {tarea['id']} - {tarea['titulo']}") # Mostramos el ID y el título de cada tarea
    
    # Pedir el ID de la tarea a eliminar
    try: # Intentar convertir la entrada a entero
        # Pedir al usuario el ID de la tarea a eliminar
        id_eliminar = int(input("\nIngresa el ID de la tarea a eliminar: ")) # Convertir a entero
    except ValueError: # Si ocurre un error de conversión
        # Mostrar mensaje de error y regresar
        print("\n❌ Por favor ingresa un número válido.")
        return
    
    # Buscar la tarea
    tarea_a_eliminar = None # Inicializar variable para almacenar la tarea a eliminar
    # Inicializar el índice de la tarea a eliminar
    indice_tarea = -1 # Inicializar el índice de la tarea a eliminar como -1
    
    for i, tarea in enumerate(lista_tareas): # Recorremos la lista de tareas con su índice
        if tarea['id'] == id_eliminar: # Si encontramos la tarea con el ID proporcionado
            # Asignamos la tarea a eliminar y su índice
            tarea_a_eliminar = tarea # Guardamos la tarea encontrada
            indice_tarea = i # Guardamos el índice de la tarea encontrada
            break
    
    if not tarea_a_eliminar: # Si no se encontró la tarea
        # Mostrar mensaje de error y regresar
        print("\n❌ No se encontró una tarea con ese ID.")
        return
    
    # Confirmar eliminación
    print(f"\n⚠️  ¿Estás seguro de que quieres eliminar la tarea:")
    print(f"   '{tarea_a_eliminar['titulo']}'?")
    # Pedimos confirmación al usuario
    print("   Esta acción no se puede deshacer.")
    confirmacion = input("\nEscribe 'si' para confirmar: ").lower() # Convertimos la entrada a minúsculas para evitar errores de mayúsculas/minúsculas
    
    if confirmacion == 'si': # Si el usuario confirma la eliminación
        lista_tareas.remove(tarea_a_eliminar) # Eliminamos la tarea de la lista
        print(f"\n✅ Tarea '{tarea_a_eliminar['titulo']}' eliminada correctamente!")
    else: # Si el usuario no confirma la eliminación
        print("\n❌ Eliminación cancelada.")

def cargar_tareas(): # Definición de variable cargar tareas al archivo JSON
    """Carga las tareas desde el archivo JSON"""
    global lista_tareas, contador_id # Necesitamos modificar estas variables globalmente
    
    try: # Intentamos abrir el archivo JSON
        with open("tareas.json", "r", encoding="utf-8") as archivo: # Abrimos el archivo en modo lectura
            lista_tareas = json.load(archivo) # Cargamos las tareas desde el archivo
            
            # Calcular el siguiente ID disponible
            if lista_tareas:
                contador_id = max(tarea['id'] for tarea in lista_tareas) + 1 # Encontramos el ID máximo y le sumamos 1
            else:
                contador_id = 1 # Si la lista está vacía, comenzamos desde 1
                
            print(f"\n✅ Se cargaron {len(lista_tareas)} tareas del archivo.") 
            
    except FileNotFoundError: # Si el archivo no existe
        # Mostramos un mensaje y comenzamos con una lista vacía
        print("\n📝 No se encontró archivo previo. Empezando con lista vacía.")
        lista_tareas = []
        contador_id = 1
        
    except json.JSONDecodeError: # Si el archivo JSON está corrupto
        # Mostramos un mensaje de error y comenzamos con una lista vacía
        print("\n❌ El archivo está corrupto. Empezando con lista vacía.")
        lista_tareas = []
        contador_id = 1

def guardar_tareas(): # Definición de función para guardar las tareas en un archivo JSON
    """Guarda las tareas en el archivo JSON"""
    try: # Intentamos abrir el archivo JSON en modo escritura
        with open("tareas.json", "w", encoding="utf-8") as archivo: # Abrimos el archivo en modo escritura
            json.dump(lista_tareas, archivo, indent=2, ensure_ascii=False) # Guardamos las tareas en formato JSON con indentación de 2 espacios y sin codificar caracteres especiales
        # Si todo sale bien, mostramos un mensaje de éxito
        print("\n💾 Tareas guardadas correctamente.") 
        
    except Exception as e: # Si ocurre un error al guardar
        # Mostramos un mensaje de error
        print(f"\n❌ Error al guardar: {e}")

def main(): # Definición de la función principal
    """Función principal del programa"""
    cargar_tareas() # Cargar las tareas desde el archivo JSON al iniciar el programa

    while True: # Bucle infinito para mantener el programa en ejecución
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            print("\nAgregar tarea\n") 
            agregar_tarea() # Llamar a la función para agregar una tarea
            guardar_tareas() # Guardar las tareas después de agregar una nueva
        elif opcion == "2":
            ver_tareas() # Llamar a la función para ver todas las tareas
        elif opcion == "3":
            modificar_tarea() # Llamar a la función para modificar una tarea
            guardar_tareas() # Guardar las tareas después de modificar una  
        elif opcion == "4":
            eliminar_tarea() # Llamar a la función para eliminar una tarea
            guardar_tareas() # Guardar las tareas después de eliminar una
        elif opcion == "5":
            print("\nSaliendo del programa...") # Mensaje de salida
            # Aquí podríamos guardar las tareas en un archivo si quisieramos persistencia
            # Por ahora solo salimos
            print("¡Hasta luego!\n")
            break # Salir del bucle y terminar el programa
        else:
            print("\nOpción inválida. Intenta de nuevo.") # Mensaje de error si la opción no es válida

# Ejecutar el programa
if __name__ == "__main__": # Comprobar si el script se está ejecutando directamente
    print("Bienvenido a la lista de tareas") # Mensaje de bienvenida
    main() # Llamar a la función principal para iniciar el programa