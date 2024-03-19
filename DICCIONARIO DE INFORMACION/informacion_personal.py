# Crear el diccionario
informacion_personal = {
    "Nombre": "Daniel Neajic",
    "edad": 27,
    "Ciudad": "Puyo",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["Ciudad"] = "Puyo"

# Agregar una nueva clave-valor representando la profesión
informacion_personal["Profesion"] = "Estudiante Universitario"

# Verificar si la clave "telefono" existe y agregarla si no
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0992937972"

# Eliminar la clave "edad"
informacion_personal.pop("edad")

# Imprimir el diccionario final
print("Diccionario Final:")
print(informacion_personal)
