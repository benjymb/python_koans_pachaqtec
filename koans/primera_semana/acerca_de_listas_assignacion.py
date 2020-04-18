#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AcercaDeListasAsignacion(Koan):

    def test_asignacion(self):
        nombres = ["John", "Smith"]
        self.assertEqual(__, nombres)

    def test_asignacion_en_paralelo(self):
        nombre, apellido = ["John", "Smith"]
        self.assertEqual(__, nombre)
        self.assertEqual(__, apellido)

    def test_parallel_assignments_with_extra_values(self):
        title, *nombres, apellido = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual(__, title)
        self.assertEqual(__, nombres)
        self.assertEqual(__, apellido)

    def test_parallel_assignments_with_sublists(self):
        nombre, apellido = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(__, nombre)
        self.assertEqual(__, apellido)

    def test_swapping_with_parallel_assignment(self):
        nombre = "Roy"
        apellido = "Rob"
        nombre, apellido = apellido, nombre
        self.assertEqual(__, nombre)
        self.assertEqual(__, apellido)

