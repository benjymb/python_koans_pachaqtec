#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutHashes in the Ruby Koans
#

from runner.koan import *

class AcercaDeDiccionarios(Koan):

    def test_creando_diccionarios(self):
        dict_vacio = dict()
        self.assertEqual(dict, type(dict_vacio))
        self.assertDictEqual({}, dict_vacio)
        self.assertEqual(__, len(dict_vacio))

    def test_usando_los_literales_dictionary(self):
        dict_vacio = {}
        self.assertEqual(dict, type(dict_vacio))
        babel_fish = { 'uno': 'one', 'dos': 'two' }
        self.assertEqual(__, len(babel_fish))

    def test_accessesando_dictionaries(self):
        babel_fish = { 'uno': 'one', 'dos': 'two' }
        self.assertEqual(__, babel_fish['uno'])
        self.assertEqual(__, babel_fish['dos'])

    def test_cambiando_dictionaries(self):
        babel_fish = { 'uno': 'one', 'dos': 'two' }
        babel_fish['uno'] = 'eins'

        expected = { 'dos': 'two', 'uno': __ }
        self.assertDictEqual(expected, babel_fish)

    def test_dicionario_es_desordenado(self):
        dict1 = { 'uno': 'one', 'dos': 'two' }
        dict2 = { 'dos': 'two', 'uno': 'one' }

        self.assertEqual(__, dict1 == dict2)


    def test_usando_keys_y_values_para_dict(self):
        babel_fish = { 'uno': 'one', 'dos': 'two' }
        self.assertEqual(__, len(babel_fish.keys()))
        self.assertEqual(__, len(babel_fish.values()))
        self.assertEqual(__, 'uno' in babel_fish.keys())
        self.assertEqual(__, 'dos' in babel_fish.values())
        self.assertEqual(__, 'one' in babel_fish.keys())
        self.assertEqual(__, 'two' in babel_fish.values())

    def test_usando_items_para_dict(self):
        babel_fish = { 'uno': 'one', 'dos': 'two' }
        self.assertEqual(__, babel_fish.items())

    def test_usando_llaves_para_hacer_un_dict(self):
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(__, len(cards))
        self.assertEqual(__, cards['green elf'])
        self.assertEqual(__, cards['yellow dwarf'])

    def test_usando_dict_para_crear_un_diccionario(self):
        cards = {'one': 'uno', 'two': 'dos'}
        cards_2 = dict((('one', 'uno'), ('two', 'dos')))
        cards_3 = dict([('one', 'uno'), ('two', 'dos')])
        cards_4 = dict([['one', 'uno'], ['two', 'dos']])

        self.assertEqual(__, cards == cards_2)
        self.assertEqual(__, cards == cards_3)
        self.assertEqual(__, cards == cards_4)


