#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AcercaDeClases(Koan):
    
    class Perro:
        "Un perro necesita paseos constantes. No dejes que el maneje un auto"

    def test_las_instancias_se_crean_abriendo_y_cerrando_parentesis(self):
        """
        # NOTA: El atributo .__name__ convertira la referencia a la clase
        # en una cadena de texto
        """
        fido = self.Perro()
        self.assertEqual(__, fido.__class__.__name__)

    def test_las_clases_tienen_cadenas_de_texto_para_documentacion(self):
        self.assertRegex(self.Perro.__doc__, __)

    # ------------------------------------------------------------------

    class Perro2:
        def __init__(self):
            self._nombre = 'Paul'

        def set_nombre(self, nombre):
            self._nombre = nombre

    def test_usando_el_metodo_init_para_inicializar_la_clase(self):
        dog = self.Perro2()
        self.assertEqual(__, dog._nombre)

   
    def test_tambien_se_puede_acceder_a_los_attributos_usando_getattr(self):

        fido = self.Perro2()
        fido.set_nombre("Fido")

        self.assertEqual(__, getattr(fido, "_nombre"))
        # getattr(), setattr() and delattr() son formas de acceder, modificar o eliminar
        # atributos por metodos, en lugar del uso de operadores.


    # ------------------------------------------------------------------

    class Perro4:
        def __init__(self, nombre_inicial):
            self._nombre = None

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self, otro_nombre):
            self._nombre = otro_nombre

        @nombre.getter
        def nombre(self):
            del self._nombre

        def __str__(self):
            return f"Mi nombre es {self.nombre}"

    def test_init_puede_dar_valores_iniciales_a_instancias(self):
        fido = self.Perro4("Fido")
        self.assertEqual(__, fido.nombre)

    def test_debo_enviar_la_cantidad_correcta_de_parametros_a_init(self):
        with self.assertRaises(___):
            self.Perro4()

        # Por que ocurre esto?

    def test_usando_propiedades(self):
        fido = self.Perro4("Fido")
        self.assertEqual(__, fido.nombre)
        fido.nombre = "Roco"
        self.assertEqual(__, fido.nombre)

    def test_probando_la_funcion_str(self):
        fido = self.Perro4("Fido")
        self.assertEqual(__, str(fido))

    
    def test_objetos_diferentes_tienen_diferentes_valores(self):
        fido = self.Perro4("Fido")
        rover = self.Perro4("Rover")

        self.assertEqual(__, rover.nombre == fido.nombre)

    def test_usando_la_funcion_dir(self):
        fido = self.Perro4("Fido")
        self.assertEqual(__, dir(fido))

        # La funcion dir() lista los atributos y metodos
        # un objeto.
