#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AcercaDeBucles(Koan):

    def test_usando_for(self):
        lista_valores = []
        for num in range(1, 5):
            lista_valores.append(num)
        
        self.assertEqual(__, lista_valores)

    def test_usando_while(self):
        lista_valores = []
        num = 1
        while len(lista_valores) < 5:
            lista_valores.append(num)
            num += 1
        self.assertEqual(__, lista_valores)

    def test_usando_pass_para_bucles_sin_cuerpo(self):
        for num in range(1,5):
            pass

        self.assertEqual(__, num)

    def test_usando_break_para_salir_del_bucle(self):
        for num in range(1, 5):
            break

        self.assertEqual(__, num)
            
    def test_usando_enumerate_y_for(self):
        for i, valor in enumerate(['Fido', 'Firulais', 'Rascal']):
            break

        self.assertEqual(__, i)
        self.assertEqual(__, valor)
