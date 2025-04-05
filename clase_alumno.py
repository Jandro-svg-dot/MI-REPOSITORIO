print("Hola mundo.")
"""Las propiedades se encapsulan definiendo variables privadas"""
"""Cuando cree un alumno, se proporcionarà el nombre y la edad"""
class alumno:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def getnombre(self):
        return self.__nombre
    
    def getedad(self):
        return self.__edad
    
a1 = alumno("Maria", 20)
a2 = alumno("Juan", 21)
a3 = alumno("Ana", 19 )

edad_mayor = 0
edad_menor = 99

if a1.getedad() > edad_mayor:
    edad_mayor = a1.getedad()
    alumno_mayor = a1.getnombre()
if a2.getedad() > edad_mayor:
    edad_mayor = a2.getedad()
    alumno_mayor = a2.getnombre()
if a3.getedad() > edad_mayor:
    edad_mayor = a3.getedad()
    alumno_mayor = a3.getnombre()
print(f"El alumno mayor es {alumno_mayor} y tiene {edad_mayor} años de edad")

alumnos = [a1, a2, a3]
suma = 0
nombres = ''
for alum in alumnos:
    if alum.getedad() < edad_menor:
        edad_menor = alum.getedad()
        alumno_menor = alum.getnombre()
    suma = suma + alum.getedad()
    nombres = nombres + alum.getnombre() + ' ' 
print(f"El alumno menor es {alumno_menor} y tiene {edad_menor} años de edad.")
print(f"Entre {nombres} suman {suma} años.")