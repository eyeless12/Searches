import time
from tracemalloc import get_tracemalloc_memory
from testType import TestType


def count_time(string, substring, function):
    start_time = time.time()
    function(substring, string)
    end_time = time.time() - start_time
    return end_time


def count_memory(string, substring, function):
    start_memory = get_tracemalloc_memory()
    function(substring, string)
    end_memory = get_tracemalloc_memory() - start_memory
    return end_memory


def test(function, string, substring, test_type : TestType):
    if test_type is TestType.Time:
        return count_time(string, substring, function)
    else:
        return count_memory(string, substring, function)
