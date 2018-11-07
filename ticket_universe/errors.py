class MissingCharset(Exception):
    def __init__(self, charset, *args, **kwargs):
        Exception.__init__(self, "Charset '{}' missing".format(charset), *args, **kwargs)