import argparse

from ticket_universe import position
from ticket_universe import universe


def arguments() -> argparse.Namespace:
    command_desc = 'example: ticket-universe fixed:LTFY- alpha numeric numeric numeric'
    positions_help = "alpha | alpha:safe_latin | numeric | range:min:max | fixed:{} | binary"

    args = argparse.ArgumentParser('ticket-universe', description=command_desc)
    args.add_argument('positions', metavar='POSITION', type=str, nargs='*', help=positions_help)
    args.add_argument('--offset', default=0, type=int)
    args.add_argument('--limit', default=None, type=int)
    return args.parse_args()


def position_from_arg(position_str):
    chunks = position_str.split(':')
    _type = chunks[0]
    _args = chunks[1:]
    return position.build_type(_type, _args)


def universe_from_args(args):
    return universe.Universe(
        [position_from_arg(s) for s in args.positions],
        limit=args.limit,
        offset=args.offset
    )


def main(args: argparse.Namespace):
    _universe = universe_from_args(args)
    for t in _universe:
        print(t)


if __name__ == '__main__':
    main(arguments())
