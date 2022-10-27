import random as r
import sys

from searcher import Searcher
import counter
import graphbuilder
import text_generator
import gc
from testType import TestType


def parse_enter(enter):
    if enter == "-h":
        print("""
This code is benchmarking algorithms for finding a substring in a string

Flags:
-t for time benchmarking
-m for memory benchmarking""")
        sys.exit(0)
    elif enter == "-t":
        return TestType.Time
    elif enter == "-m":
        return TestType.Memory
    else:
        print("""
        Unknown flag! Use -h for help""")
        sys.exit(1)


def init_plot_func(results: dict):
    colors = ['y', 'g', 'b', 'm', 'c']
    plot_funcs = []
    for (key, value) in results.items():
        plot_funcs.append(graphbuilder.PlotFunc(key, colors.pop(), value))
    return plot_funcs


def main():
    gc.disable()
    x = []

    if len(sys.argv) == 1:
        print("""Wrong usage! Use -h for help""")
        sys.exit(1)
    test_type = parse_enter(sys.argv[1])
    methods_results = {'Standard': [],
                       'Rabin': [],
                       'Aho': [],
                       'Bauer': [],
                       'KMP': []}

    start_point = 7
    end_point = 21
    for i in range(start_point, end_point):
        print(f"{i}/{end_point}")
        (string, substring) = text_generator.get_text(r.randint(2 ** (i - 7),
                                                                2 ** (i - 3)), 10000)
        for (key, value) in methods_results.items():
            methods_results[key].append(counter.test(Searcher.algos[key], string, substring, test_type))
        x.append(i)

    graphbuilder.draw_graph_with_func(test_type, x, init_plot_func(methods_results))


if __name__ == '__main__':
    main()
