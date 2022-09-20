import string
from random import choice


def get_text(needle_size, position):
    substring = 'a{0}'.format(''.join(choice(string.ascii_uppercase + string.digits)
                                      for _ in range(needle_size)))
    string_to_find = ''.join(choice(string.ascii_uppercase + string.digits)
                             for _ in range(position)) + substring
    return string_to_find, substring
