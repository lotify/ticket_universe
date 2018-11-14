import argparse

from ticket_universe import universe
from ticket_universe.position import Position


def arguments(*args, **kwargs) -> argparse.Namespace:
    parser = argument_parser()
    args = parser.parse_args(*args, **kwargs)
    return args


def argument_parser():
    command_desc = "example: ticket-universe fixed:LTFY- alpha numeric numeric numeric"
    positions_help = (
        "alpha | alpha:safe_latin | numeric | range:min:max | fixed:{} | binary"
    )
    parser = argparse.ArgumentParser("ticket-universe", description=command_desc)
    parser.add_argument(
        "positions", metavar="POSITION", type=str, nargs="*", help=positions_help
    )
    parser.add_argument("--offset", default=0, type=int)
    parser.add_argument("--limit", default=None, type=int)
    return parser


def universe_from_args(args):
    return universe.Universe([Position.from_string(s) for s in args.positions])


def main(args: argparse.Namespace = None):
    _arguments = args or arguments()
    _universe = universe_from_args(_arguments)

    if len(_universe) == 0:
        print_help()

    for t in _universe.generate(_arguments.limit, _arguments.offset):
        print(t)


def print_help():
    parser = argument_parser()
    parser.print_help()
