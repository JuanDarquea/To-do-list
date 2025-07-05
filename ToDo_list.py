
Task = [] # List to store tasks
def add_task(): # Function to add a task
    Task_description = input("Escribe tu tarea") # Ask user for task description
    Task.append(Task_description) # Append the task to the list
    print(f"Tarea '{Task_description}' añadida a la lista de tareas.") # Confirmation message
    print("Iniciando la lista de tareas...") # Starting message
    add_task() # Call the function again to allow adding more tasks
    print("Lista de tareas actual:", Task)  # Print current tasks
    
