#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AcercaDeListas(Koan):

    def test_creando_listas(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(__, len(empty_list))

    def test_usando_literales_de_lista(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, __], nums)

        nums.append(333)
        self.assertListEqual([1, 2, __], nums)

    def test_accediendo_a_los_elementos_de_la_lista(self):
        noms = ['mantequilla', 'de mani', 'y', 'mermelada']

        self.assertEqual(__, noms[0])
        self.assertEqual(__, noms[3])
        self.assertEqual(__, noms[-1])
        self.assertEqual(__, noms[-3])

    def test_usando_slicing_en_listas(self):
        noms = ['mantequilla', 'de mani', 'y', 'mermelada']

        self.assertEqual(__, noms[0:1])
        self.assertEqual(__, noms[0:2])
        self.assertEqual(__, noms[2:2])
        self.assertEqual(__, noms[2:20])
        self.assertEqual(__, noms[4:0])
        self.assertEqual(__, noms[4:100])
        self.assertEqual(__, noms[5:0])

    def test_slicing_en_los_bordes(self):
        noms = ['mantequilla', 'de mani', 'y', 'mermelada']

        self.assertEqual(__, noms[2:])
        self.assertEqual(__, noms[:2])

    def test_listas_y_rangos(self):
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        self.assertEqual(__, list(range(5)))
        self.assertEqual(__, list(range(5, 9)))

    def test_rangos_con_saltos(self):
        self.assertEqual(__, list(range(5, 3, -1)))
        self.assertEqual(__, list(range(0, 8, 2)))
        self.assertEqual(__, list(range(1, 8, 3)))
        self.assertEqual(__, list(range(5, -7, -4)))
        self.assertEqual(__, list(range(5, -8, -4)))

    def test_inserciones_en_listas(self):
        knight = ['You', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(__, knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(__, knight)

    def test_usando_pop_en_listas(self):
        stack = [10, 20, 30, 40]
        stack.append('ultimo')

        self.assertEqual(__, stack)

        popped_value = stack.pop()
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)

        popped_value = stack.pop(1)
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)

        # Notar que hay una funcion pop, pero no una funcion push.

        # Parte de la filosofia de Python es que idealmente debe existir una unica
        # manera de hacer cualquier cosa.
