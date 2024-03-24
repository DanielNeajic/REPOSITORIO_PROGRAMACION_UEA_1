# Creamos un diccionario con información personal ficticia para cada persona
informacion_personas = [
    {"Nombre": "Daniel Neajic", "Edad": 27, "Ciudad": "loja"},
    {"nombre": "Vale Garcia", "edad": 28, "ciudad": "Ambato"},
    {"nombre": "Carlos Parra", "edad": 29, "ciudad": "Cuenca"},
    {"nombre": "Gabriel Valdez", "edad": 30, "ciudad": "Quito"}
]

# Accedemos al valor asociado con la clave "ciudad" y lo modificamos
informacion_personas[0]["Ciudad"] = "Puyo"

# Agregamos una nueva clave-valor representando la profesión de la persona
informacion_personas[0]["Profesion"] = "Servidor Publico"

# Verificamos si la clave "telefono" existe y la agregamos si no existe
if "Telefono" not in informacion_personas[0]:
    informacion_personas[0]["Telefono"] = "0992937972"

# Eliminamos la clave "edad" del diccionario
if "edad" in informacion_personas[0]:
    del informacion_personas[0]["edad"]

# Imprimimos el diccionario final de la primera persona
print("Información de la primera persona después de las modificaciones:")
print(informacion_personas[0])
