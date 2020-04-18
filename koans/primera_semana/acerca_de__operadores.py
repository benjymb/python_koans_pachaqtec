#!/usr/bin/env python
# -*- coding: utf-8 -*-


from runner.koan import Koan, __, _____


class AcercaDeOperadores(Koan):

    def test_descubriendo_operadores_numericos(self):
        self.assertEqual(__, 1 + 2)
        self.assertEqual(__, 1 - 2)
        self.assertEqual(__, 3 * 3)
        self.assertEqual(__, 4 / 4)
        self.assertEqual(__, 3 // 4)
        self.assertEqual(__, 8 % 2)
        self.assertEqual(__, 2 % 3)
        
        
    def test_descubriendo_operadores_logicos(self):
        self.assertTrue(__ < __)
        self.assertTrue(__ > __)
        self.assertTrue(__ >= __)
        self.assertTrue(__ <= __)
        self.assertTrue(__ == __)
        self.assertTrue(__ != __)
        
        
        
        
        

