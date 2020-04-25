#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AcercaDeHerencia(Koan):

    class Perro:
        def __init__(self, nombre):
            self._nombre = nombre

        @property
        def nombre(self):
            return self._nombre

        def ladrar(self):
            return "GUAU!"

    class Chihuahua(Perro):

        def mover_cola(self):
            return "Soy feliz!"

        def ladrar(self):
            return "GUAU GUAU!"

    def test_subclases_pueden_heredar_de_otra(self):
        self.assertEqual(__, issubclass(self.Chihuahua, self.Perro))

    def test_instancias_heredan_comportamientos_de_la_clase_padre(self):
        rosco = self.Chihuahua("Rosco")
        self.assertEqual(__, rosco.nombre)

    def test_subclasses_aniaden_comportamientos_nuevos(self):
        rosco = self.Chihuahua("Rosco")
        self.assertEqual(__, rosco.mover_cola())

        fido = self.Perro("Fido")
        with self.assertRaises(___): 
            fido.mover_cola()

    def test_subclasses_aniaden_comportamientos_existentes(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.ladrar())

        fido = self.Perro("Fido")
        self.assertEqual(__, fido.ladrar())

    """
    # Ahora, tenemos la siguiente clase :
    """

    class BullDog(Perro):

        def ladrar(self):
            return super().ladrar() + ", GRR!"

    def test_subclasses_pueden_usar_metodos_del_padre_a_traves_de_super(self):

        ralph = self.BullDog("Ralph")
        self.assertEqual(__, ralph.ladrar())

