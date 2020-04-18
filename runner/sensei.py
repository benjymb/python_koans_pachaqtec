#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re
import sys
import os
import glob

from . import helper
from .mockable_test_result import MockableTestResult
from runner import path_to_enlightenment

from libs.colorama import init, Fore, Style
init()  # init colorama


class Sensei(MockableTestResult):
    def __init__(self, stream):
        unittest.TestResult.__init__(self)
        self.stream = stream
        self.prevTestClassName = None
        self.tests = path_to_enlightenment.koans()
        self.pass_count = 0
        self.lesson_pass_count = 0
        self.all_lessons = None

    def startTest(self, test):
        MockableTestResult.startTest(self, test)

        if helper.cls_name(test) != self.prevTestClassName:
            self.prevTestClassName = helper.cls_name(test)
            if not self.failures:
                self.stream.writeln()
                self.stream.writeln("{0}{1}Revisando {2}".format(
                    Fore.RESET, Style.NORMAL, helper.cls_name(test)))
                if helper.cls_name(test) not in (
                    'AcercaDeAsserts', 'AcercaDeTemasExtra'
                ):
                    self.lesson_pass_count += 1

    def addSuccess(self, test):
        if self.passesCount():
            MockableTestResult.addSuccess(self, test)
            self.stream.writeln(
                "  {0}{1}{2} has expanded your awareness.{3}{4}"
                .format(
                    Fore.GREEN, Style.BRIGHT, test._testMethodName,
                    Fore.RESET, Style.NORMAL
                )
            )
            self.pass_count += 1

    def addError(self, test, err):
        # Having 1 list for errors and 1 list for failures would mess with
        # the error sequence
        self.addFailure(test, err)

    def passesCount(self):
        return not (
            self.failures and
            helper.cls_name(self.failures[0][0]) !=
            self.prevTestClassName
        )

    def addFailure(self, test, err):
        MockableTestResult.addFailure(self, test, err)

    def sortFailures(self, testClassName):
        table = list()
        for test, err in self.failures:
            if helper.cls_name(test) == testClassName:
                m = re.search(r"(?<= line )\d+", err)
                if m:
                    tup = (int(m.group(0)), test, err)
                    table.append(tup)

        if table:
            return sorted(table)
        else:
            return None

    def firstFailure(self):
        if not self.failures:
            return None

        table = self.sortFailures(helper.cls_name(self.failures[0][0]))

        if table:
            return (table[0][1], table[0][2])
        else:
            return None

    def learn(self):
        self.errorReport()
        self.stream.writeln("")
        self.stream.writeln("")
        self.stream.writeln(self.report_progress())
        if self.failures:
            self.stream.writeln(self.report_remaining())
        self.stream.writeln("")
        self.stream.writeln(self.say_something_zenlike())

        if self.failures:
            sys.exit(-1)

        self.stream.writeln(
            "\n{0}**************************************************"
            .format(Fore.RESET)
        )
        self.stream.writeln(
            "\n{0}Ese fué el último. ¡Muy bien!"
            .format(Fore.MAGENTA)
        )
        self.stream.writeln(
            "\nSi quieres más ejercicios, "
            "revisa el archivo acerca_de_ejercicios_extra.py{0}{1}"
            .format(Fore.RESET, Style.NORMAL)
        )

    def errorReport(self):
        problem = self.firstFailure()
        if not problem:
            return None
        test, err = problem
        self.stream.writeln(
            "  {0}{1}{2} ha dañado tu "
            "karma.".format(Fore.RED, Style.BRIGHT, test._testMethodName)
        )
        self.stream.writeln(
            "\n{0}{1}Aún no has acabado con todos los ejercicios ..."
            .format(Fore.RESET, Style.NORMAL)
        )
        self.stream.writeln("{0}{1}{2}".format(
            Fore.RED, Style.BRIGHT, self.scrapeAssertionError(err))
        )
        self.stream.writeln("")
        self.stream.writeln(
            "{0}{1}Revisa las siguientes líneas de código:"
            .format(Fore.RESET, Style.NORMAL)
        )
        self.stream.writeln("{0}{1}{2}{3}{4}".format(
            Fore.YELLOW, Style.BRIGHT,
            self.scrapeInterestingStackDump(err), Fore.RESET, Style.NORMAL)
        )

    def scrapeAssertionError(self, err):
        if not err:
            return ""

        error_text = ""
        count = 0
        for line in err.splitlines():
            m = re.search("^[^^ ].*$", line)
            if m and m.group(0):
                count += 1

            if count > 1:
                error_text += ("  " + line.strip()).rstrip() + '\n'
        return error_text.strip('\n')

    def scrapeInterestingStackDump(self, err):
        if not err:
            return ""

        lines = err.splitlines()

        sep = '@@@@@SEP@@@@@'

        stack_text = ""
        for line in lines:
            m = re.search("^  File .*$", line)
            if m and m.group(0):
                stack_text += '\n' + line

            m = re.search(r"^    \w(\w)+.*$", line)
            if m and m.group(0):
                stack_text += sep + line

        lines = stack_text.splitlines()

        stack_text = ""
        for line in lines:
            m = re.search("^.*[/\\\\]koans[/\\\\].*$", line)
            if m and m.group(0):
                stack_text += line + '\n'

        stack_text = stack_text.replace(sep, '\n').strip('\n')
        stack_text = re.sub(
                r'(acerca_de_\w+.py)',
                r"{0}\1{1}".format(Fore.BLUE, Fore.YELLOW), stack_text
            )
        stack_text = re.sub(
                r'(line \d+)',
                r"{0}\1{1}".format(Fore.BLUE, Fore.YELLOW), stack_text
            )
        return stack_text

    def report_progress(self):
        return "Has completado {0} ({2} %) koans y " \
                "{1} (de {3}) lecciones.".format(
                    self.pass_count,
                    self.lesson_pass_count,
                    self.pass_count * 100 // self.total_koans(),
                    self.total_lessons()
                )

    def report_remaining(self):
        koans_remaining = self.total_koans() - self.pass_count
        lessons_remaining = self.total_lessons() - self.lesson_pass_count

        return "Estás aún a {0} koans y {1} lecciones de completar " \
            "tu objetivo.".format(
                koans_remaining,
                lessons_remaining)

    # Hat's tip to Tim Peters for the zen statements from The 'Zen
    # of Python' (http://www.python.org/dev/peps/pep-0020/)
    #
    # Also a hat's tip to Ara T. Howard for the zen statements from his
    # metakoans Ruby Quiz (http://rubyquiz.com/quiz67.html) and
    # Edgecase's later permutation in the Ruby Koans
    def say_something_zenlike(self):
        if self.failures:
            turn = self.pass_count % 37

            zenness = ""
            if turn == 0:
                zenness = "Bello es mejor que feo."
            elif turn == 1 or turn == 2:
                zenness = "Explícito es mejor que implícito."
            elif turn == 3 or turn == 4:
                zenness = "Simple es mejor que complejo."
            elif turn == 5 or turn == 6:
                zenness = "Complejo es mejor que complicado."
            elif turn == 7 or turn == 8:
                zenness = "Plano es mejor que anidado."
            elif turn == 9 or turn == 10:
                zenness = "Disperso es mejor que denso."
            elif turn == 11 or turn == 12:
                zenness = "La legibilidad cuenta."
            elif turn == 13 or turn == 14:
                zenness = "Los casos especiales no son tan especiales " \
                          "como para quebrantar las reglas."
            elif turn == 15 or turn == 16:
                zenness = "Aunque lo práctico gana a la pureza."
            elif turn == 17 or turn == 18:
                zenness = "Los errores nunca deberían dejarse pasar " \
                          "silenciosamente."
            elif turn == 19 or turn == 20:
                zenness = "A menos que hayan sido silenciados explícitamente."
            elif turn == 21 or turn == 22:
                zenness = "Frente a la ambigüedad, rechaza " \
                          "la tentación de adivinar."
            elif turn == 23 or turn == 24:
                zenness = "Debería haber una -y preferiblemente " \
                          "sólo una- manera obvia de hacerlo."
            elif turn == 25 or turn == 26:
                zenness = "Aunque esa manera puede no ser obvia al " \
                          "principio a menos que seas holandés."
            elif turn == 27 or turn == 28:
                zenness = "Ahora es mejor que nunca."
            elif turn == 29 or turn == 30:
                zenness = "Aunque nunca es a menudo mejor que " \
                          "ya mismo."
            elif turn == 31 or turn == 32:
                zenness = "Si la implementación es difícil de explicar, " \
                          "es una mala idea."
            elif turn == 33 or turn == 34:
                zenness = "Si la implementación es fácil de explicar, " \
                          "puede que sea una buena idea."
            else:
                zenness = "Los 'namespaces' son una gran idea " \
                          "¡Hagamos más de esas cosas!"

            zenness += "\n\nhttp://www.python.org/dev/peps/pep-0020/"
            zenness += "\nhttps://gist.github.com/javierdaza/"\
                       "4258b74e2eb7cfd4f55286061b592f37\n\n"

            return "{0}{1}{2}{3}".format(
                Fore.CYAN, zenness, Fore.RESET, Style.NORMAL
            )
        else:
            return "{0}Aunque, nadie espera a la Santa Inquisicion." \
                .format(Fore.CYAN)

        # Hopefully this will never ever happen!
        return "Ops! Ocurrio un error. Nadie es perfecto :("

    def total_lessons(self):
        all_lessons = self.filter_all_lessons()
        if all_lessons:
            return len(all_lessons)
        else:
            return 0

    def total_koans(self):
        return self.tests.countTestCases()

    def filter_all_lessons(self):
        cur_dir = os.path.split(os.path.realpath(__file__))[0]
        if not self.all_lessons:
            self.all_lessons = glob.glob(
                '{0}/../koans/../acerca_de_*.py'.format(cur_dir)
            )
            self.all_lessons = list(
                filter(
                    lambda filename: "acerca_de_temas_extra" not in filename,
                    self.all_lessons
                )
            )

        return self.all_lessons
