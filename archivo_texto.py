# Escritura de Archivo de Texto

# Creamos un nuevo archivo llamado my_notes.txt en modo escritura
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Soy Patrick Luna y esta es mi primera nota personal.\n")
    file.write("Hoy aprendí sobre operaciones de archivos en Python.\n")
    file.write("Espero continuar mejorando mis habilidades de programación.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo my_notes.txt en modo lectura
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # Utilizamos strip() para eliminar el salto de línea al final

# Al usar 'with', los archivos se cierran automáticamente al salir del bloque
