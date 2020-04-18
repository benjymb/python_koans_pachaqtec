#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AcercaDeLasComprensiones(Koan):


    def test_creando_listas_con_comprensiones_de_listas(self):
        animales = [
            'cordero', 
            'perezoso', 
            'pangolin', 
            'cereal para desayunar',
            'murcielago de fruta'
        ]

        comprehension = [animal.capitalize() for animal in animales]

        self.assertEqual(__, comprehension[4])

    def test_filtrando_usando_comprensiones_de_listas(self):
        animales = [
            'spam', 'perezoso', 'cuy', 'cereal para desayunar',
            'murcielago de fruta'
        ]

        comestible = [animal for animal in animales if animal == 'cereal para desayunar']

        self.assertEqual(__, len(animales))
        self.assertEqual(__, len(comestible))

    def test_desempacando_tuplas_en_comprensiones_de_listas(self):
        lista_de_tuplas = [(1, 'leñador'), (2, 'inquisición'), (4, 'spam')]
        comprehension = [ skit * number for number, skit in lista_de_tuplas ]

        self.assertEqual(__, comprehension[0])

    def test_doblando_comprensiones_de_listas(self):
        lista_de_huevos = ['huevo duro', 'huevo frito']
        lista_de_carnes = ['pequeño spam', 'jamón spam', 'spam frito']

        comprehension = [ '{0} y {1}'.format(huevo, carne) for huevo in lista_de_huevos for carne in lista_de_carnes]

        self.assertEqual(__, comprehension[0])
        self.assertEqual(__, len(comprehension))

    def test_creando_un_conjunto_con_comprension_de_conjunto(self):
        comprehension = { x for x in 'aabbbcccc'}

        self.assertEqual(__, comprehension)  # ¡Recuerda que los elementos dentro de un conjunto (set) son únicos!

    def test_creando_un_diccionario_con_comprensiones_de_diccionarios(self):
        dict_de_armas = {
            'primera': 'miedo', 'segunda': 'sorpresa',
            'tercera':'eficiencia despiadada', 'cuarta':'devocion fanática',
            'quinta': None
        }

        dict_comprehension = { k.upper(): weapon for k, weapon in dict_de_armas.items() if weapon}

        self.assertEqual(__, 'primera' in dict_comprehension)
        self.assertEqual(__, 'PRIMERA' in dict_comprehension)
        self.assertEqual(__, len(dict_de_armas))
        self.assertEqual(__, len(dict_comprehension))
