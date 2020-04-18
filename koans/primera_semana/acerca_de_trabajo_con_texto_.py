#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AcercaDeStrings(Koan):

    def test_strings_con_comillas_dobles_son_strings(self):
        string = "Hello, world."
        self.assertEqual(__, isinstance(string, str))

    def test_strings_con_comillas_simples_tambien_son_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(__, isinstance(string, str))

    def test_strings_con_triple_comillas_son_tambien_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(__, isinstance(string, str))

    def test_triple_comillas_simples_funcionan_tambien(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(__, isinstance(string, str))

    def test_strings_del_tipo_puro_o_raw_son_strings(self):
        string = r"Konnichi wa, world!"
        self.assertEqual(__, isinstance(string, str))

    def test_strings_del_tipo_f_o_format_son_strings(self):
        string = f"Konnichi wa, world!"
        self.assertEqual(__, isinstance(string, str))

    def test_usando_comillas_simples_para_crear_strings_comillas_dobles(self):
        string = 'Y ella me dijo, "Anda a casa"'
        self.assertEqual(__, string)

    def test_usando_comillas_dobles_para_crear_strings_comillas_simples(self):
        string = "Don't"
        self.assertEqual(__, string)

    def test_usando_backslash_para_omitir_comillas_en_strings(self):
        a = "Y ella me dijo, \"Don't\""
        b = 'Y ella me dijo, "Don\'t"'
        self.assertEqual(__, (a == b))

    def test_usando_backslash_al_final_de_linea_para_saltar_la_siguiente(self):
        string = "Fue la mejor de las épocas,\n\
Fue la peor de las épocas."
        self.assertEqual(__, len(string))

    def test_usando_triple_comillas_dobles_se_usan_para_continuar_en_varias_lineas(self):
        string = """
¡Howdy,
mundo!
"""
        self.assertEqual(__, len(string))

    def test_que_al_usar_triple_comillas_se_necesita_escapar_menos(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(__, (a == b))

    def test_mas_une_strings(self):
        string = "Hello, " + "world"
        self.assertEqual(__, string)

    def test_strings_adyacentes_son_concatenatedas_automaticamente(self):
        string = "Hello" ", " "world"
        self.assertEqual(__, string)

    def test_mas_no_modica_los_string_inicial(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual(__, hi)
        self.assertEqual(__, there)

    def test_mas_igual_anade_al_final_del_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual(__, hi)

    def test_strings_interpretan_los_caracteres_de_secuencia(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(__, len(string))
