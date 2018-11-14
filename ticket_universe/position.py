from typing import Union

from ticket_universe.errors import MissingCharset


class Position:
    def __init__(self, characters: [str]):
        self.characters = characters

    def __len__(self):
        return len(self.characters)

    def __iter__(self):
        return iter(self.characters)

    @classmethod
    def from_string(cls, s) -> "Position":
        chunks = s.split(":")
        _type = chunks[0]
        _args = chunks[1:]
        return build_type(_type, _args)


class FixedPosition(Position):
    def __init__(self, character: str):
        Position.__init__(self, [character])


class RangedPosition(Position):
    def __init__(self, _min: Union[str, int], _max: Union[str, int]):
        _range = (
            [str(num) for num in range(int(_min), int(_max) + 1)]
            if _min != _max
            else []
        )
        Position.__init__(self, _range)


class BinaryPosition(Position):
    def __init__(self):
        Position.__init__(self, ["0", "1"])


class NumericPosition(Position):
    def __init__(self):
        Position.__init__(self, list("0123456789"))


class AlphaPosition(Position):
    def __init__(self, charset: str = "latin"):
        Position.__init__(self, self._import_charset(charset))

    @staticmethod
    def _import_charset(charset) -> [str]:
        import ticket_universe.charsets as charset_factories

        charset_factory = getattr(charset_factories, charset, None)
        if charset_factory is None:
            raise MissingCharset(charset)

        return charset_factory()


def build_type(_type: str, args):
    import sys

    module = sys.modules[__name__]
    position_type = getattr(module, _type.title() + "Position")
    return position_type(*args)
