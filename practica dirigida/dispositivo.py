# Practica dirigida
# Tema: Herencia Multiple
#       Pruebas unitarias
# Fecha: 06-05-2025

class Dispositivo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        
    def conectar(self):
        return f'El dispositivo de marca {self._marca} se conectó'
    
    def desconectar(self):
        return f'El dispositivo de marca {self._marca} se desconectó'
    
    def ejecutar(self):
        return f'El dispositivo de marca {self._marca} está ejecutando una acción'