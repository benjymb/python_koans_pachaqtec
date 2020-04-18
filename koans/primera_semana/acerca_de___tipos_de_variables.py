#!/usr/bin/env python
# -*- coding: utf-8 -*-


from runner.koan import Koan, __, _____


class AcercaDeTiposDeVariables(Koan):

    def test_descubriendo_tipos_variables(self):
    
        self.assertEqual(__, True.__class__)
        self.assertEqual(__, False.__class__)
        self.assertEqual(__, type(True) == True.__class__)
        
        self.assertEqual(__, type(None))

        self.assertEqual(__, type(0))
        self.assertEqual(__, type(3.14))
        self.assertEqual(__, type(3.14))
        self.assertEqual(__, type(159863))
        self.assertEqual(__, type(0xABFC))
        self.assertEqual(__, type(3j))

        self.assertEqual(__, type("¡Hola, mundo!"))
        

