#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *

class AcercaDeNone(Koan):

    def test_none_es_un_objeto(self):
        "A diferencia de NULL en otros lenguajes de programación"
        self.assertEqual(__, isinstance(None, object))

    def test_none_es_universal(self):
        "¡None es universal!"
        self.assertEqual(____, None is None)

    def test_cual_es_la_excepcion_lanzada_cuando_llamas_a_un_metodo_que_no_existe(self):
        """
        ¿Cuál es la excepción lanzada cuando llamamos a un metodo que no existe?

        PISTA: Ejecuta la consola de python con las siguientes lineas.

        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            ex2 = ex

        # ¿Cuál fue la excepción?
        #
        
        self.assertEqual(__, ex2.__class__)

        # ¿Cuál fue el mensaje de la excepción?
        # (PISTA: reemplaza __ con parte del mensaje de error.)
        self.assertRegex(ex2.args[0], __)

    def test_none_es_diferente(self):
        """
        None es diferente de otras cosas que son iguales a False
        """
        self.assertEqual(__, None is not 0)
        self.assertEqual(__, None is not False)
