import time
import tracemalloc
from testType import TestType
import gc


def count_time(string, substring, function):
    start_time = time.time()
    function(substring, string)
    end_time = time.time() - start_time
    return end_time


def count_memory(string, substring, function):
    gc.collect()
    start_memory = tracemalloc.get_traced_memory()[0]
    tracemalloc.start()
    function(substring, string)
    end_memory = tracemalloc.get_traced_memory()[0] - start_memory
    gc.collect()
    return end_memory if end_memory > 0 else 0


def test(function, string, substring, test_type : TestType):
    if test_type is TestType.Time:
        return count_time(string, substring, function)
    else:
        return count_memory(string, substring, function)
