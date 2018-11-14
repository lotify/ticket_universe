def latin() -> [str]:
    """[A-Z]"""
    return list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def safe_latin() -> [str]:
    """[A-Z] excluding (O, I, L)"""
    return list("ABCDEFGHJKMNPQRSTUVWXYZ")
