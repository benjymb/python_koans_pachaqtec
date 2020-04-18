#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AcercaDeTuplas(Koan):

    def test_creando_una_tupla(self):
        contando_tres =  (1, 2, 5)
        self.assertEqual(__, contando_tres[2])

    def test_tuplas_son_immutables_por_lo_que_la_asignacion_de_elementos_no_es_posible(self):

        contando_tres = (1, 2, 5)
        try:
            contando_tres[2] = "three"
        except TypeError as ex:
            msg = ex.args[0]

        # Nota, assertRegex() ubica parte del texto usando expresiones regulares,
        # para que no tengas que copiar todo el mensaje

        self.assertRegex(msg, __)

    def test_tuplas_son_immutables_por_lo_que_agregar_elementos_no_es_posible(self):
        contando_tres =  (1, 2, 5)
        with self.assertRaises(___): contando_tres.append("boom")

        # Tuples are less flexible than lists, but faster.

    def test_tuplas_solo_pueden_cambiar_por_reemplazo(self):
        contando_tres = (1, 2, 5)

        conteo_lista = list(contando_tres)
        conteo_lista.append("boom")
        contando_tres = tuple(conteo_lista)

        self.assertEqual(__, contando_tres)

    def test_tuplas_de_un_elemento_se_ven_raras(self):
        self.assertEqual(__, (1).__class__)
        self.assertEqual(__, (1,).__class__)
        self.assertEqual(__, ("¡Soy una tupla!",).__class__)
        self.assertEqual(__, ("No soy una tupla").__class__)

    def test_constructor_de_tuplas_puede_sorprendernos(self):
        self.assertEqual(__, tuple("¡Sorpresa!"))

    def test_creando_una_tupla_vacia(self):
        self.assertEqual(__ , ())
        self.assertEqual(__ , tuple()) # A veces, menos confuso.

    def test_tuplas_pueden_anidarse(self):
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(__, place)

    def test_tuplas_son_buenas_para_representar_registros(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )

        self.assertEqual(__, locations[2][0])
        self.assertEqual(__, locations[0][1][2])
