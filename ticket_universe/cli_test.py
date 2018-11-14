import io
import sys
import unittest

from argparse import Namespace
from contextlib import contextmanager

from ticket_universe import cli


@contextmanager
def capture(command, *args, **kwargs):
    out, sys.stdout = sys.stdout, io.StringIO()
    try:
        command(*args, **kwargs)
        sys.stdout.seek(0)
        yield sys.stdout.read()
    finally:
        sys.stdout = out


class CliTest(unittest.TestCase):
    def test_limiting_output(self):
        args = Namespace(positions=["binary", "binary", "binary"], limit=4, offset=0)
        with capture(cli.main, args) as output:
            self.assertEqual(4, output.count('\n'))

    def test_offsetting_output(self):
        args = Namespace(positions=["binary", "binary", "binary"], limit=None, offset=4)
        with capture(cli.main, args) as output:
            self.assertEqual(4, output.count('\n'))

    def test_calling_main_without_args_prints_help(self):
        args = cli.arguments([])
        with capture(cli.main, args) as o, capture(cli.print_help) as h:
            self.assertEqual(h, o)

    def test_calling_main_with_args_prints_universe(self):
        args = Namespace(positions=["binary"], limit=None, offset=0)
        with capture(cli.main, args) as output:
            self.assertEqual("0\n1\n", output)
