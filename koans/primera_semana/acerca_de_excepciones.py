#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AcercaDeExcepciones(Koan):

    class MiErrorEspecial(RuntimeError):
        pass

    def test_instruccion_try(self):
        result = None
        try:
            self.fail("Upss")
        except Exception as ex:
            resultado = 'Excepción manejada'
            ex2 = ex

        self.assertEqual(__, resultado)
        self.assertEqual(__, ex2.args[0])

    def test_lanzando_un_error_especifico(self):
        resultado = None
        try:
            raise self.MiErrorEspecial("Mi mensaje")
        except self.MiErrorEspecial as ex:
            result = 'Excepción manejada'
            msg = ex.args[0]

        self.assertEqual(__, result)
        self.assertEqual(__, msg)

    def test_instruccion_else(self):
        result = None
        try:
            pass
        except RuntimeError:
            result = '¡Se rompió!'
            pass
        else:
            result = 'No pasó nada'

        self.assertEqual(__, result)


    def test_instruccion_finally(self):
        result = None
        try:
            self.fail("Upss")
        except:
            # Ningun codigo va aquí
            pass
        finally:
            result = 'Esto siempre se ejecuta'

        self.assertEqual(__, result)
