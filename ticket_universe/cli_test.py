import os
import unittest
import subprocess

from argparse import Namespace
from ticket_universe import cli


BIN_PATH = os.path.dirname(__file__) + "/../bin"


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


class BinaryTest(unittest.TestCase):
    def test_without_args_exits_without_errors(self):
        _exit = subprocess.check_call([BIN_PATH + "/ticket-universe"])
        self.assertEqual(0, _exit)

    def test_with_simple_args_exits_without_errors(self):
        output, err = subprocess.Popen(
            [BIN_PATH + "/ticket-universe", "binary"], stdout=subprocess.PIPE
        ).communicate()
        self.assertIsNone(err)
        self.assertEqual(b"0\n1\n", output)
