#primero llamo a json
import json

#creo el diccionario y agrego 3 alumnos nuevos
data={"data":[{"cedula":"12345678","nombre":"Mario","apellido":"Gonzalez","nota1":85,"nota2":90,"nota3":95},
              {"cedula":"87654321","nombre":"Ana","apellido":"Martinez","nota1":78,"nota2":82,"nota3":88},
              {"cedula":"11223344","nombre":"Luis","apellido":"Perez","nota1":92,"nota2":89,"nota3":94},
              {"cedula":"27903157","nombre":"Kenneth","apellido":"Perez","nota1":10,"nota2":20,"nota3":30},
              {"cedula":"28313462","nombre":"Manuel","apellido":"Gutierrez","nota1":15,"nota2":25,"nota3":35},
              {"cedula":"10377989","nombre":"Pedro","apellido":"Rojas","nota1":18,"nota2":28,"nota3":38}]}
#creo una funcion que modifique el archivo json con los alumnos nuevos
def agregar(diccionario):
    with open('alumnos.json','w') as file:
        json.dump(diccionario,file,indent=4)
    return print("los nuevos alumnos se han agregado satisfactoriamente!","\n")
#creo una fucnion que muestre la lista de alumnos, incluyendo a los nuevos
def leer(archivo):
    with open(archivo,'r') as file:
        dato=json.load(file)
        for estudiante in dato["data"]:
            print("Cedula:",estudiante['cedula'],"  ",
                  "Nombre:",estudiante['nombre'],"  ",
                  "Apellido:",estudiante['apellido'],"  ",
                  "Nota 1:",estudiante['nota1'],"  ",
                  "Nota 2:",estudiante['nota2'],"  ",
                  "Nota 3:",estudiante['nota3'])

#pruebo el programa
agregar(data)
archivo='alumnos.json'
leer('alumnos.json')