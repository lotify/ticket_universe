from ticket_universe.errors import MissingCharset


class Position:

    def __init__(self, characters: [str]):
        self.characters = characters

    def __len__(self):
        return len(self.characters)

    def __iter__(self):
        return iter(self.characters)


class FixedPosition(Position):
    def __init__(self, character: str):
        Position.__init__(self, [character])


class RangedPosition(Position):
    def __init__(self, _min: int, _max: int):
        _range = [str(num) for num in range(_min, _max + 1)] if _min != _max else []
        Position.__init__(self, _range)


class BinaryPosition(Position):
    def __init__(self):
        Position.__init__(self, ['0', '1'])


class NumericPosition(Position):
    def __init__(self):
        Position.__init__(self, list('0123456789'))


class AlphaPosition(Position):
    def __init__(self, charset: str = 'latin'):
        Position.__init__(self, self._import_charset(charset))

    @staticmethod
    def _import_charset(charset) -> [str]:
        import ticket_universe.charsets as charset_factories

        charset_factory = getattr(charset_factories, charset, None)
        if charset_factory is None:
            raise MissingCharset(charset)

        return charset_factory()
