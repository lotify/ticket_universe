import argparse

from ticket_universe import universe
from ticket_universe.position import Position


def arguments() -> argparse.Namespace:
    command_desc = "example: ticket-universe fixed:LTFY- alpha numeric numeric numeric"
    positions_help = (
        "alpha | alpha:safe_latin | numeric | range:min:max | fixed:{} | binary"
    )

    args = argparse.ArgumentParser("ticket-universe", description=command_desc)
    args.add_argument(
        "positions", metavar="POSITION", type=str, nargs="*", help=positions_help
    )
    args.add_argument("--offset", default=0, type=int)
    args.add_argument("--limit", default=None, type=int)
    return args.parse_args()


def universe_from_args(args):
    return universe.Universe(
        [Position.from_string(s) for s in args.positions],
        limit=args.limit,
        offset=args.offset,
    )


def main(args: argparse.Namespace):
    _universe = universe_from_args(args)
    for t in _universe:
        print(t)
