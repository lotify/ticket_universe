import argparse

from ticket_universe import universe
from ticket_universe.position import Position


def arguments(*args, **kwargs) -> argparse.Namespace:
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
    return parser.parse_args(*args, **kwargs)


def universe_from_args(args):
    return universe.Universe(
        [Position.from_string(s) for s in args.positions],
        limit=args.limit,
        offset=args.offset,
    )


def main(args: argparse.Namespace = None):
    _universe = universe_from_args(args or arguments())
    for t in _universe:
        print(t)
