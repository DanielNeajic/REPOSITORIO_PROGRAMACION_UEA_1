# Escritura de Archivo de Texto
file_name = "my_notes.txt"

# Modo de apertura: "w" para escritura (write)
archivo_escritura = open(file_name, "w")

# Método write(): escribir una Nota a la vez
archivo_escritura.write("Nota 1: Hoy es un buen día.\n")
archivo_escritura.write("Nota 2: No olvidar comprar leche.\n")
archivo_escritura.write("Nota 3: Reunión a las 3 pm.\n")
archivo_escritura.write("Nota 4: Clase de la noche 8PM\n")

# Cerramos el archivo de escritura
archivo_escritura.close()

# Lectura de Archivo de Texto
# Modo de apertura: "r" para lectura (read)
archivo_lectura = open(file_name, "r")

# Leemos y mostramos el contenido para verificar
contenido = archivo_lectura.read()
print("Contenido del archivo después de escribir:")
print(contenido)

archivo_lectura.close()
