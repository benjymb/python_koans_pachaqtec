from runner.koan import *


class Perro:
    def nombre(self):
        return "Fido"

    def _cola(self):
        """
        # Anteponiendo un subguion a nuestros metodos,
        # indicamos que el metodo es 'privado'.
        # Es una convencion.
        """ 
        return "agitandose"

    def __intensidad_de_ladrido(self):
        """
        # Anteponiendo un doble subguion a nuestros metodos,
        # el nombre del metodo cambiara a 
        # `_Perro__intensidad_de_ladrido`
        # Se utiliza para evitar que clases hijas
        # tengan el mismo nombre del metodo
        """
        return 'muy alto y agudo'


class AcercaDeMetodos(Koan):

    def test_llamando_a_metodos_en_otros_objetos(self):
        labrador = Perro()
        self.assertEqual(__, labrador.nombre())

    def test_llamando_a_metodos_privados(self):
        labrador = Perro()

        # Esto no es adecuado, pero se permite.
        self.assertEqual(__, labrador._cola())

    def test_descubriendo_el_nuevo_nombre_de_metodos_que_empiezan_con_doble_subguion(self):
        labrador = Perro()
        with self.assertRaises(___): 
            password = labrador.__password()

        # Pero aun se puede acceder!
        self.assertEqual(__, labrador._Perro__password())