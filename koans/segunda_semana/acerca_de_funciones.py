#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

def mi_funcion_global(a,b):
    return a + b

def funcion_que_no_retorna_nada(a, b):
    resultado = a + b

def funcion_con_argumentos_que_tienen_valor_por_defecto(
    a, b='Soy el valor por defecto de la variable b'
):
    return [a, b]

def funcion_con_cantidad_variable_de_argumentos_no_nombrados(*args):
    return args

def funcion_vacia():
    """
    # RECORDAR : Se usa la palabra reservada pass para indicar
    # bloques de codigo vacio.
    """
    pass

def funcion_vacia_que_hace_trampa():
    pass
    return "XD"


class AcercaDeFunciones(Koan):

    def test_llamando_a_funcion_global(self):
        self.assertEqual(__, mi_funcion_global(2,3))

    """
    # NOTA: Llamar a una funcion con una cantidad de parametros diferentes
    # a lo esperado, no lanzara una excepcion SyntaxisError.
    # Es un error en tiempo de ejecucion.
    """

    def test_llamando_funciones_con_el_numero_de_parametros_inadecuados(self):
        try:
            mi_funcion_global()
        except TypeError as exception:
            mensaje = exception.args[0]

        self.assertRegex(mensaje,
            r'mi_funcion_global\(\) missing 2 required positional arguments')

        try:
            mi_funcion_global(1, 2, 3)
        except Exception as e:
            mensaje = e.args[0]

        """
        # NOTA: Cuidado con los parentesis, necesitan ser escapados.
        # r'\(\)'
        """
        self.assertRegex(mensaje, __)

    def test_llamando_funcion_que_no_retorna_nada(self):
        self.assertEqual(__, funcion_que_no_retorna_nada(1, 2))

    def test_llamando_funcion_con_argumentos_que_tienen_valor_por_defecto(self):
        self.assertEqual(__, funcion_con_argumentos_que_tienen_valor_por_defecto(1))
        self.assertEqual(__, funcion_con_argumentos_que_tienen_valor_por_defecto(1, 2))

    def test_llamando_funcion_con_cantidad_variable_de_argumentos_no_nombrados(self):
        self.assertEqual(__, funcion_con_cantidad_variable_de_argumentos_no_nombrados())
        self.assertEqual(('uno',), funcion_con_cantidad_variable_de_argumentos_no_nombrados('uno'))
        self.assertEqual(__, funcion_con_cantidad_variable_de_argumentos_no_nombrados('uno', 'dos'))

    def test_llamando_funcion_vacia(self):
        self.assertEqual(__, funcion_vacia())

    def test_llamando_funcion_vacia_que_hace_trampa(self):
        self.assertEqual(____, "XD" != funcion_vacia_que_hace_trampa())

    
 