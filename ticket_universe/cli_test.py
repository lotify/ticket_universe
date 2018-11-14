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
        uni = cli.universe_from_args(args)
        tickets = [t for t in uni]
        self.assertEqual(len(uni) - 4, len(tickets))

    def test_offsetting_output(self):
        args = Namespace(positions=["binary", "binary", "binary"], limit=None, offset=4)
        uni = cli.universe_from_args(args)
        tickets = [t for t in uni]
        self.assertEqual(len(uni) - 4, len(tickets))

    def test_calling_main_without_args_returns_help(self):
        with capture(cli.main, cli.arguments([])) as output:
            self.assertEqual("", output)

    def test_calling_main_with_args_prints_universe(self):
        with capture(
            cli.main, Namespace(positions=["binary"], limit=None, offset=0)
        ) as output:
            self.assertEqual("0\n1\n", output)
