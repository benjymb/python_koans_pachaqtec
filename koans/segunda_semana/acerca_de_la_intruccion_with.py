#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

import re # Se usa para comparar expresiones regulares.

class AcercaDeLaInstruccionWith(Koan):

    def contar_lineas(self, nombre_archivo):
        try:
            archivo = open(nombre_archivo)
            try:
                return len(archivo.readlines())
            finally:
                archivo.close()
        except IOError:
            self.fail()

    def test_contando_lineas(self):
        self.assertEqual(__, self.contar_lineas("archivo_ejemplo.txt"))

    """
    ## ------------------------------------------------------------------
    ## PENSEMOS ACERCA DE LO QUE ACABA DE OCURRIR
    ##
    ## Las funciones contar_lineas y encontrar_linea son similares, pero diferentes.
    ## Ambas siguen el patron (o la forma de) "sandwich code" (codigo sandwich).
    ##
    ## Codigo sandwich es todo codigo que viene en 3 partes: (1) la rebanada superior
    ## de pan, (2) la carne, y (3) la rebanada inferior de pan.
    ## Las rebanadas de pan, siempre son las mismas, pero la carne cambia 
    ## la mayoria de las veces.
    ##
    ## En este caso, la carne es la parte mas importante de nuestro codigo.
    ##
    ## Python resuelve este problema usando Context Managers. Consideremos
    ## la siguiente clase (notese los metodos __enter__ y __exit__):
    ##
    """

    class AdministradorDeContexto():
        def __init__(self, nombre_archivo):
            self._nombre_archivo = nombre_archivo
            self._archivo = None

        def __enter__(self):
            self._archivo = open(self._nombre_archivo)
            return self._archivo

        def __exit__(self, cls, value, tb):
            self._archivo.close()

    # Ahora, podemos escribir :

    def contar_lineas_2(self, nombre_archivo):
        with self.AdministradorDeContexto(nombre_archivo) as archivo:
            return len(archivo.readlines())

    def test_contando_lineas_2(self):
        self.assertEqual(__, self.contar_lineas_2("archivo_ejemplo.txt"))

    def contar_lineas_3(self, nombre_archivo):
        with open(nombre_archivo) as archivo:
            return len(archivo.readlines())

    def test_la_funcion_incluida_open_es_un_administrador_de_contexto(self):
        self.assertEqual(__, self.contar_lineas_3("archivo_ejemplo.txt"))
