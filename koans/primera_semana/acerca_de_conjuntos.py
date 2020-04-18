#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AcercaDeConjuntos(Koan):

    def test_sets_mantiene_las_listas_unicas(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(__, there_can_only_be_only_one)

    def test_sets_vacios_tienen_sintaxis_diferente_a_los_sets_llenos(self):
        self.assertEqual(__, {1, 2, 3})
        self.assertEqual(__, set())

    def test_dicionaries_y_sets_usan_llaves(self):
        
        self.assertEqual(__, {1, 2, 3}.__class__)
        self.assertEqual(__, {'uno': 1, 'dos': 2}.__class__)

        self.assertEqual(__, {}.__class__)

    def test_creando_sets_usando_strings(self):
        self.assertEqual(__, {'12345'})
        self.assertEqual(__, set('12345'))

    def test_convirtiendo_un_set_en_una_lista_para_ordenarlo(self):
        self.assertEqual(__, sorted(set('12345')))

    # ------------------------------------------------------------------

    def test_set_usan_operadores_aritmeticos(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        self.assertEqual(__, scotsmen - warriors)
        self.assertEqual(__, scotsmen | warriors)
        self.assertEqual(__, scotsmen & warriors)
        self.assertEqual(__, scotsmen ^ warriors)

    # ------------------------------------------------------------------

    def test_se_puede_preguntar_si_el_elemento_pertenece_al_set(self):
        self.assertEqual(__, 127 in {127, 0, 0, 1} )
        self.assertEqual(__, 'cow' not in set('apocalypse now') )

    def test_podemos_comparar_subsets(self):
        self.assertEqual(__, set('cake') <= set('cherry cake'))
        self.assertEqual(__, set('cake').issubset(set('cherry cake')) )

        self.assertEqual(__, set('cake') > set('pie'))
