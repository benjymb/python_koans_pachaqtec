#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

def pedir_orden(plato):
    return lambda cantidad: f"{cantidad} {plato}"

class AcercaDeLambdas(Koan):

    def test_lambdas_pueden_asignarse_a_variables(self):

        aniadir_uno = lambda n : n + 1
        
        self.assertEqual(__, aniadir_uno(10))

    def test_accediendo_a_lambdas_por_asignacion(self):

        ceviche = pedir_orden('ceviche')
        sopa = pedir_orden('sopa')

        self.assertEqual(__, ceviche(3))
        self.assertEqual(__, sopa(2))

    def test_accediendo_a_lambdas_sin_asignacion(self):
        self.assertEqual(__, pedir_orden('causa')(3))
