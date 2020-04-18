#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


# Starting a classname or attribute with an underscore
# normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = ["__", "___", "____", "_____", "Koan"]

__ = "-=> ¡Completame! <=-"


class ___(Exception):
    pass


____ = "-=> ¿True o False? <=-"

_____ = 0


class Koan(unittest.TestCase):
    pass
