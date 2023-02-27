f = open("prueba.txt", "r")
contenido = f.read()
print(contenido)
f.close()


#2
with open("prueba.txt", "r") as f:
     contenido = f.read()
     print(contenido)

with open("prueba.txt", "r") as f:
    contenido = f.readline()
    print(contenido)

with open("prueba.txt", "r") as f:    #ruta_absoluta
    contenido = f.readlines()
    for line in contenido:
        print(line.strip())

with open("prueba.txt", "w") as f:    #w="write" escribe y borras lo quer estaba
    f.write("Estamos escribiendo un archivo")

#a="add" agrega son borrar lo que ya estaba
with open("prueba.txt", "a") as f:
    for numero in range(0,10):
         f.write(f"\nEstamos escribiendo un nuevo archivo {numero}")

diccionario ={"personal": {nombre: 'rocio', apellido: 'josa', edad :29}}
with open("prueba.txt", "w") as f:
    f.write(json.dumps(diccionario, indent=4))

#Actividad clase
with open("hobby.txt", "a") as f:
   for hobby in range (0,3):
        f.write(f'{input("Ingrese su hobby: ")}')