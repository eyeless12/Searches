import random as r
from searcher import *
import counter
import graphbuilder
import text_generator
from testType import TestType


def main():
    x = []  # Needle length
    test_type = TestType.Time
    runners = {'Standard': graphbuilder.PlotFunc('Standard', 'b*'),
               'Rabin': graphbuilder.PlotFunc('Rabin', 'g^'),
               'KMP': graphbuilder.PlotFunc("KMP", 'rs'),
               'Aho': graphbuilder.PlotFunc('Aho', 'yP')}

    for i in range(10, 25):
        print(f"{i}/24")
        (string, substring) = text_generator.get_text(r.randint(2 ** (i - 7),
                                                                2 ** (i - 3)), 10000)
        for (key, value) in runners.items():
            value.res.append(counter.test(algos[key],
                                          string, substring, test_type))
        x.append(i)

    graphbuilder.draw(test_type, x, runners.values())


if __name__ == '__main__':
    main()
