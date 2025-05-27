alumnos = {}
num_alumnos = int(input("Ingrese el número de alumnos del curso "))

for i in range(num_alumnos):
    nom_alumno = input("Ingrese el nombre del alumno ")
    if nom_alumno in alumnos:
        pirnt("El alumno ya existe ")
    else:
        opcion = "s"
        notas = []
        while  opcion == "s":
            nota = 0
            nota = float(input("Ingrese la nota del alumno "))
            notas.append(nota)
            opcion = input("Desea ingresar otra nota (s/n) ")
        alumnos[nom_alumno] = notas
print(alumnos)
for  nom_al in  alumnos:
    conta_nota = 0
    suma_nota = 0
    for nota_al in  alumnos[nom_al]:
        conta_nota = conta_nota + 1
        suma_nota = suma_nota + nota_al
    promedio =  suma_nota / conta_nota
    print(f"El alumno {nom_al} obtuvo un promedio de {promedio}")