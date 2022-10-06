from aho import *


class Searcher:
    unicode_size = 1105
    key_max = 1


def simple_search(substring, string):
    left_border = 0
    right_border = len(substring)
    while right_border < len(string):
        if string[left_border: right_border] == substring:
            return left_border
        left_border += 1
        right_border += 1
    return -1


def create_table(string):
    len_needle = len(string)
    table = [len_needle for _ in range(Searcher.unicode_size)]

    for i in range(len_needle):
        if table[ord(string[i])] == len_needle:
            table[ord(string[i])] = len_needle - i

    return table


def aho_korasik(substring, string):
    root = aho_create_statemachine([substring])
    node = root

    for i in range(len(string)):
        while node is not None and string[i] not in node.goto:
            node = node.fail
        if node is None:
            node = root
            continue
        node = node.goto[string[i]]
        for pattern in node.out:
            return i - len(pattern) + 1
    return -1


def bauer_moore(substring, string):
    table = create_table(substring)
    len_hay = len(string)
    len_needle = shift = needle_pos = ptr = len(substring)
    while shift <= len_hay and needle_pos > 0:
        if substring[needle_pos - 1] == string[ptr - 1]:
            needle_pos -= 1
            ptr -= 1
        else:
            shift += table[ord(string[ptr - 1])]
            ptr = shift
            needle_pos = len_needle
    if needle_pos <= 0:
        return ptr
    return -1


def prefix(text):
    len_text = len(text)
    prefix_table = [0] * len_text
    for i in range(1, len_text):
        curr = prefix_table[i - 1]
        while curr > 0 and text[curr] != text[i]:
            curr = prefix_table[curr - 1]
        if text[curr] == text[i]:
            curr = curr + 1
        prefix_table[i] = curr
    return prefix_table


def kmp(substring, string):
    prefix_table = prefix(substring)
    curr = 0
    for i in range(len(string)):
        while curr > 0 and substring[curr] != string[i]:
            curr = prefix_table[curr - 1]
        if substring[curr] == string[i]:
            curr = curr + 1
        if curr == len(substring):
            return i - len(substring) + 1
    return -1


def full_hash(needle, key):
    curr_hash = 0
    for i in range(len(needle)):
        curr_hash += Searcher.key_max * (ord(needle[i]) % key)
        Searcher.key_max *= key
    Searcher.key_max //= key
    return curr_hash


def rabin_karp(substring, string):
    key = 37
    len_hay, len_needle = len(string), len(substring)
    needle_hash = full_hash(substring, key)
    Searcher.key_max = 1
    curr_hash = full_hash(string[:len_needle], key)

    for i in range(len_needle, len_hay):
        if curr_hash == needle_hash and substring == string[i - len_needle: i]:
            return i - len_needle
        curr_hash = int(curr_hash // key + Searcher.key_max * (ord(string[i]) % key))

    Searcher.key_max = 1
    if substring == string[-len_needle:]:
        return len_hay - len_needle
    return -1


algos = {'Standard': simple_search,
         'Rabin': rabin_karp,
         'KMP': kmp,
         'Aho': aho_korasik}
