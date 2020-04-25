#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutClassMethods in the Ruby Koans
#

from runner.koan import *

class AcercaDeAtributosDeClase(Koan):

    class Perro:
        def mover_cola(self):
            return 'La instancia esta moviendo la cola!'

        def ladrar(self):
            return "La instancia esta ladrando!"

        def grunir(self):
            return "La instancia esta gruniendo!"

        @staticmethod
        def ladrar():
            return "Usando el metodo estatico para ladrar, arg: None [No tengo argumentos!]"

        @classmethod
        def grunir(cls):
            return "Usando el metodo de la clase para grunir, arg: clase=" + cls.__name__

    def test_debido_a_que_las_clases_son_objetos_hay_funciones_que_se_comparten_para_la_clase(self):
        # Revisar patron Singleton
        self.assertRegex(self.Perro.grunir(), __)

    def test_los_metodos_estaticos_no_pertenecen_a_la_instancia(self):
        self.assertRegex(self.Perro.ladrar(), __)

