import matplotlib.pyplot as plt

from testType import TestType


class PlotFunc:
    name = ''
    color = ''

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.res = []


def draw(test_type, x, func_res):
    ax1 = plt.figure(figsize=(12, 7)).add_subplot(111)

    for func in func_res:
        plt.plot(x, func.res, func.color,
                 alpha=0.7, label=func.name, mew=2, ms=10)

    plt.legend()
    if test_type is TestType.Time:
        ax1.set_title(u'Time By Substring Length')
        plt.ylabel(u'Time [ms]', fontsize=12)
    else:
        ax1.set_title(u'Memory By Substring Length')
        plt.xlabel(u'Needle length [2^n]', fontsize=12)
    plt.grid(True)
    plt.show()
