#!/usr/bin/env python
# -*- coding: utf-8 -*-


from runner.koan import Koan, __, _____


class AcercaDeAsserts(Koan):

    def test_assert_verdad(self):
        """

        Debemos llegar a la verdad, usando los asserts
        
        """

        self.assertTrue(_____)  # Esto debe ser igual a True

    def test_assert_con_mensaje(self):
        """
        
        Podemos aumentar nuestro conocimiento mas facilmente, leyendo los mensajes.
        
        """
        self.assertTrue(False, "Esto debe ser igual a True -- Por favor corrije esto")

    def test_llenar_valores(self):
        """

        Algunas veces, se te pedira que iguales los valores
        
        """
        self.assertEqual(__, 1 + 1)

    def test_assert_igualdad(self):
        """

        Para probar nuestra logica, debemos comparar nuestras expectativas con la realidad.
        
        """
        valor_esperado = __
        valor_real = 1 + 1
        self.assertTrue(valor_real == valor_esperado)

    def test_a_better_way_of_asserting_equality(self):
        """

        Podemos probar nuestra logica de una mejor manera
        
        """
        valor_esperado = __
        valor_real = 1 + 1

        self.assertEqual(valor_real, valor_esperado)

    def test_que_unittest_asserts_trabaja_del_mismo_modo_que_los_asserts_python(self):
        """

        Hay que entender lo que se usa por debajo.
        
        """

        # Esto lanza una exception del tipo AssertionError
        assert False

