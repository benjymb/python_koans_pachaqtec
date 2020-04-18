#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AcercaDeTrabajoConStrings(Koan):

    def test_usando_format_para_imprimir_variables(self):
        value1 = 'Uno'
        value2 = 2
        string = "Los valores son {0} y {1}".format(value1, value2)
        self.assertEqual(__, string)

    def test_valores_formateados_pueden_ser_mostrados_en_cualquier_orden_o_repetirse(self):
        value1 = 1
        value2 = 'dos'
        string = "Los valores son {1}, {0}, {0} y {1}!".format(value1, value2)
        self.assertEqual(__, string)

    def test_cualquier_expresion_en_python_expression_puede_formatearse(self):
        import math # Importando un modulo standard de python module que contiene funciones matematicas

        decimal_places = 4
        string = "La raíz cuadrada de 5 es {0:.{1}f}".format(
            math.sqrt(5), decimal_places
        )
        self.assertEqual(__, string)

    def test_puedo_obtener_una_sub_cadena_de_texto_de_una_cadena_de_texto(self):
        string = "Tocino, lechuga y tomate"
        self.assertEqual(__, string[7:10])

    def test_puedo_obtener_una_letra_de_una_cadena_de_texto(self):
        string = "Tocino, lechuga y tomate"
        self.assertEqual(__, string[1])

    def test_una_letra_puede_convertirse_a_un_entero(self):
        self.assertEqual(__, ord('a'))
        self.assertEqual(__, ord('b') == (ord('a') + 1))

    def test_las_cadenas_de_texto_pueden_partirse(self):
        string = "Salchicha Huevos Tocino"
        palabras = string.split()
        self.assertListEqual([__, __, __], palabras)

    def test_cadenas_de_texto_del_tipo_raw_no_interpretan_secuencias_de_escape(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual(__, string)
        self.assertEqual(__, len(string))

        # Util en expresiones regulares, rutas de archivos, URLs, etc.

    def test_cadenas_de_texto_pueden_unirse(self):
        words = ["Yo", "me", "quedo", "en casa."]
        self.assertEqual(__, ' '.join(words))

    def test_cadenas_de_texto_pueden_formatearse_usando_f(self):

        def sonido():
            return "guau!"
        
        persona = "vecino"
        
        self.assertEqual(__, f"Mi perro le dijo {sonido()} al {persona}.")

    def test_cadenas_de_texto_pueden_cambiar_entre_mayusculas_y_minusculas(self):
        self.assertEqual(__, 'guido'.capitalize())
        self.assertEqual(__, 'guido'.upper())
        self.assertEqual(__, 'TimBot'.lower())
        self.assertEqual(__, 'guido van rossum'.title())
        self.assertEqual(__, 'mayúsculas Y MINÚSCULAS'.swapcase())
