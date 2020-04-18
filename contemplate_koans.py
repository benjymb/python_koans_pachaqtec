#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Acknowledgment:
#
# Python Koans is a port of Ruby Koans originally written by Jim Weirich
# and Joe O'brien of Edgecase. There are some differences and tweaks specific
# to the Python language, but a great deal of it has been copied wholesale.
# So thanks guys!
#

import sys

if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print("\nEste programa requiere la version 3 de Python pero esta " +
              "ejecutandose con Python 2!\n\n"
              "Usaste la llamada incorrecta? \nPrueba con:\n\n" +
              "    python3 contemplate_koans.py\n")
    else:
        if sys.version_info < (3, 3):
            print("\n" +
                  "********************************************************\n" +
                  "ATENCION:\n" +
                  "Este programa requiere la version 3.3 de " +
                  "Python o superior.\n" +
                  "Tu version de Python es antigua, por lo que te puede dar " +
                  "problemas!\n\n" +
                  "Pero veamos hasta donde podemos llegar...\n" +
                  "********************************************************\n")

        from runner.mountain import Mountain

        Mountain().walk_the_path(sys.argv)
