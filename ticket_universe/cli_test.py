import unittest
import subprocess

from argparse import Namespace
from ticket_universe import cli


class CliTest(unittest.TestCase):

    def test_limiting_output(self):
        args = Namespace(positions=['binary', 'binary', 'binary'], limit=4, offset=0)
        uni = cli.universe_from_args(args)
        tickets = [t for t in uni]
        self.assertEqual(len(uni) - 4, len(tickets))

    def test_offsetting_output(self):
        args = Namespace(positions=['binary', 'binary', 'binary'], limit=None, offset=4)
        uni = cli.universe_from_args(args)
        tickets = [t for t in uni]
        self.assertEqual(len(uni) - 4, len(tickets))


class BinaryTest(unittest.TestCase):

    def test_without_args_exits_without_errors(self):
        _exit = subprocess.check_call(['bin/ticket-universe'])
        self.assertEqual(0, _exit)

    def test_with_simple_args_exits_without_errors(self):
        p = subprocess.Popen(['bin/ticket-universe', 'binary'], stdout=subprocess.PIPE)
        output, err = p.communicate()
        self.assertIsNone(err)
        self.assertEqual(b'0\n1\n', output)
