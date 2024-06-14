from io import open

# Apertura y lectura del archivo de texto:
# Abre el archivo de texto "personas.txt" ubicado en el directorio "Ejercicio_1" en modo de lectura ("r").
# Lee todas las líneas del archivo y las almacena en la lista lineas.
# Cierra el archivo después de leerlo para liberar recursos del sistema.
# Procesamiento de las líneas del archivo:
fichero = open("Ejercicio_1/personas.txt", "r",  encoding='utf-8') 
lineas = fichero.readlines()
fichero.close()


personas = []
#Itera sobre cada línea en la lista lineas.
#Para cada línea, elimina el carácter de nueva línea ("\n") al final usando replace("\n", "").
#Divide la línea en campos utilizando el separador ";" mediante el método split(";").
#Crea un diccionario persona con los campos extraídos de la línea y lo agrega a la lista personas.
#Impresión de la información de las personas:

for linea in lineas:
    campos = linea.replace("\n", "").split(";")
    persona = {'id': campos[0], 'nombre': campos[1], 'apellido': campos[2], 'nacimiento': campos[3]}
    personas.append(persona)


# Itera sobre cada diccionario de persona en la lista personas.
# Imprime información formateada de cada persona, incluyendo su id, nombre, apellido y fecha de nacimiento.
for p in personas:
    print(f"(id={p['id']}) {p['nombre']} {p['apellido']} => {p['nacimiento']}")



