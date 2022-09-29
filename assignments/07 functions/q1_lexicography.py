def precedes(str_1, str_2):
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """

    if str_1.lower() < str_2.lower():
        return str_1

    return str_2
