from talon import Context, Module, actions

mod = Module()


# https://github.com/cursorless-dev/cursorless-talon/blob/ad696598ef38a2154906fb6c6b1d1901ba427227/src/modifiers/ordinal_scope.py#L13C1-L20C32
@mod.capture(rule="<user.ordinals_small> | [<user.ordinals_small>] last")
def ordinal_or_last2(m) -> int:
    """An ordinal or the word 'last'"""
    if m[-1] == "last":
        return -getattr(m, "ordinals_small", 1)
    return m.ordinals_small - 1
