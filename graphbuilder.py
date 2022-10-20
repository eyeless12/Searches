import matplotlib.pyplot as plot

from testType import TestType


class PlotFunc:
    def __init__(self, name, color, results: list):
        self.name = name
        self.color = color
        self.res = results


def draw_graph_with_func(test_type, x, func_res):
    ax1 = plot.figure(figsize=(12, 7)).add_subplot(111)

    for func in func_res:
        plot.plot(x, func.res, func.color,
                  alpha=0.7, label=func.name, mew=2, ms=10)

    plot.legend()
    if test_type is TestType.Time:
        ax1.set_title(u'Time By Substring Length')
        plot.ylabel(u'Time', fontsize=12)
    else:
        ax1.set_title(u'Memory By Substring Length')
        plot.xlabel(u'Substring length', fontsize=12)

    plot.grid(True)
    plot.show()
