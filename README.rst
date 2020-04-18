============
Python Koans
============

Esta version de Python Koans es un port de Edgecase's "Ruby Koans" que puede ser encontrado en
http://rubykoans.com/.

Esta es una adaptacion de Python Koans de Greg Malcom, simplificado y traducido al espaniol por Benjy Malca.
Esta version se puede encontrar en https://github.com/gregmalcolm/python_koans 

Esta version de Python Koans es un tutorial interactivo para aprender a programar en Python haciendo que los tests
se ejecuten correctamente.

Una gran cantidad de tests han sido *arreglados*, completando las partes faltantes de las funciones assert. Por ejemplo:

    self.assertEqual(__, 1+2)

el que puede ser arreglado reemplazando __ con la solucion:

    self.assertEqual(3, 1+2)

Occasionally you will encounter some failing tests that are already filled out.
In these cases you will need to finish implementing some code to progress. For
example, there is an exercise for writing some code that will tell you if a
triangle is equilateral, isosceles or scalene.

As well as being a great way to learn some Python, it is also a good way to get
a taste of Test Driven Development (TDD).


Downloading Python Koans
------------------------

Python Koans is available through git on Github:

    http://github.com/gregmalcolm/python_koans


Installing Python Koans
-----------------------

Aside from downloading or checking out the latest version of Python Koans, you
need to install the Python interpreter.

At this time of writing, there are two versions of the Python Koans:

* one for use with Python 2.7 (earlier versions are no longer supported)
* one for Python 3.1+

You should be able to work with newer Python versions, but older ones will
likely give you problems.

You can download Python from here:

    http://www.python.org/download

After installing Python make sure the folder containing the python executable
is in the system path. In other words, you need to be able to run
Python from a command console. With Python 2 it will be called `python`
or `python.exe` depending on the operating system. For Python 3 it will either
be `python3` or for windows it will be `python.exe`.

If you have problems, this may help:

    http://www.python.org/about/gettingstarted

Windows users may also want to update the line in the batch file `run.bat` to
set the python path::

    SET PYTHON_PATH=C:\Python27


Getting Started
---------------

Jake Hebbert has created a couple of screencasts available here:

http://www.youtube.com/watch?v=e2WXgXEjbHY&list=PL5Up_u-XkWgNcunP_UrTJG_3EXgbK2BQJ&index=1

Or if you prefer to read:

From a \*nix terminal or windows command prompt go to the python
koans\\python_VERSION folder and run::

    python contemplate_koans.py

or::

    python3 contemplate_koans.py

In my case I'm using Python 3 with windows, so I fire up my command
shell (cmd.exe) and run this:

.. image:: https://user-images.githubusercontent.com/2614930/28401747-f723ff00-6cd0-11e7-9b9a-a6993b753cf6.png

Apparently a test failed::

    AssertionError: False is not True

It also tells me exactly where the problem is, it's an assert on line 12
of .\\koans\\about_asserts.py. This one is easy, just change False to True to
make the test pass.

Sooner or later you will likely encounter tests where you are not sure what the
expected value should be. For example::

    class Dog:
        pass

    def test_objects_are_objects(self):
        fido = self.Dog()
        self.assertEqual(__, isinstance(fido, object))

This is where the Python Command Line can come in handy. In this case I can
fire up the command line, recreate the scenario and run queries:

.. image:: https://user-images.githubusercontent.com/2614930/28401750-f9dcb296-6cd0-11e7-98eb-c20318eada33.png