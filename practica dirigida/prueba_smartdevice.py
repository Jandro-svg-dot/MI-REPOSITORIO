import unittest
from smartdevice import SmartDevice

class Pruebas(unittest.TestCase):
    def setUp(self):
       self.sd = SmartDevice("Samsung", "Galaxy", "Wi-fi")
    
    def test_marca_no_es_iphone (self):
        self.assertFalse(self.sd._marca == "IPhone")
        
    def test_marca_no_existe(self):
        self.assertIsNotNone(self.sd._marca)
        
    def test_obtiene_respuesta_metodo_conectar(self):
        cadena = self.sd.conectar()
        self.assertGreater(len(cadena), 0)
        
    def test_marca_distinta_a_modelo(self):
        self.assertNotEqual(self.sd._marca, self.sd._modelo)
        
    def test_conectar_es_distinto_a_desconectar(self):
        self.assertNotEqual(self.sd.conectar(), self.sd.desconectar())
        
    def test_marca_esta_en_lista(self):
        marcas = ["Apple", "Samsung", "Microsoft"]
        self.assertIn(self.sd._marca, marcas)
        
    def test_respuestas_de_las_2_superclases(self):
        rpta1 = self.sd.conectar()
        rpta2 = self.sd.iniciar()
        self.assertTrue(len(rpta1)>len(rpta2))
        
if __name__ == '__main__':
    unittest.main()