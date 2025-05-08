from conexion import Conexion
from dispositivo import Dispositivo

class SmartDevice(Dispositivo, Conexion):
    def __init__(self, marca, modelo, mensaje):
        super().__init__(marca, modelo)
        Conexion.__init__(self, mensaje)
        
    def status(self):
        # métodos iniciar, conectar, ejecutar, desconectar y terminar en orden.
        print(Conexion.iniciar(self))
        print(super().conectar())
        print(super().ejecutar())
        print(super().desconectar())
        print(Conexion.terminar(self))
        
    def status2(self):
        return f'{Conexion.iniciar(self)}\n{super().conectar()}\n{super().ejecutar()}\n{super().desconectar()}\n{Conexion.terminar(self)}'
        
# Prueba:
sd = SmartDevice("Iphone","15", "5G")
sd.status()
