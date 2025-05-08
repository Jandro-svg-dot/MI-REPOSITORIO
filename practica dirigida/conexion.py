# Practica dirigida
# Tema: Herencia Multiple
#       Pruebas unitarias
# Fecha: 06-05-2025

class Conexion:
    def __init__(self, mensaje):
        self._mensaje = mensaje
        
    def iniciar(self):
        
        return f'Inicio de conexión: {self._mensaje}'
    
    def terminar(self):
        return f'Fin de conexión: {self._mensaje}'
    
