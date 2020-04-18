#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AcercaDeLaVerdadYLaFalsedad(Koan):

    def valor_real(self, condition):
        if condition:
            return 'Este valor es verdadero o True'
        else:
            return 'Este valor es una falsedad o False'

    def test_true_es_tratado_como_true(self):
        self.assertEqual(__, self.valor_real(True))

    def test_false_es_tratado_como_false(self):
        self.assertEqual(__, self.valor_real(False))

    def test_none_es_tratado_como_false(self):
        self.assertEqual(__, self.valor_real(None))

    def test_cero_es_tratado_como_false(self):
        self.assertEqual(__, self.valor_real(0))

    def test_coleciones__vacias_son_tratadas_como_false(self):
        self.assertEqual(__, self.valor_real([]))
        self.assertEqual(__, self.valor_real(()))
        self.assertEqual(__, self.valor_real({}))
        self.assertEqual(__, self.valor_real(set()))

    def test_cadenas_de_texto_son_tratadas_como_false(self):
        self.assertEqual(__, self.valor_real(""))

    def test_todo_lo_demas_es_tratado_como_true(self):
        self.assertEqual(__, self.valor_real(1))
        self.assertEqual(__, self.valor_real([0]))
        self.assertEqual(__, self.valor_real((0,)))
        self.assertEqual(
            __,
            self.valor_real("El lenguaje Python se llama asi por la serie Monty Python")
        )
        self.assertEqual(__, self.valor_real(' '))
        self.assertEqual(__, self.valor_real('0'))
