""" Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una   vez   completado   el   ingreso   de   los   datos,   su   programa   debe   mostrar   en   pantalla   el   listado completo de los alumnos.
Nota:
El uso de listas con diccionarios le será de utilidad. """

# Función para ingresar las calificaciones de un alumno
def ingresar_calificaciones():
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la primera calificación: "))
    nota2 = float(input("Ingrese la segunda calificación: "))
    nota3 = float(input("Ingrese la tercera calificación: "))
    return {'Alumno': nombre, 'Notas': [nota1, nota2, nota3]}


cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

lista_alumnos = []

for i in range(cantidad_alumnos):
    alumno = ingresar_calificaciones()
    lista_alumnos.append(alumno)

print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)
