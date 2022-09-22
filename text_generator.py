import string
from random import choice


def get_text(substring_size, position):
    substring = 'a{0}'.format(''.join(choice(string.ascii_uppercase + string.digits)
                                      for _ in range(substring_size)))
    string_to_find = ''.join(choice(string.ascii_uppercase + string.digits)
                             for _ in range(position)) + substring
    return string_to_find, substring
