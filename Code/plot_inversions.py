#!/usr/bin/env python

from pyknon.plot import plot2, plot2_bw
from pyknon.simplemusic import inversion

def plot_color():
    n1 = [11, 10, 7]

    for x in range(12):
        plot2(n1, inversion(n1, x), "ex-inversion-plot-{0:02}.ps".format(x))

    n2 = [1, 3, 7, 9, 4]
    plot2(n2, inversion(n2, 9), "ex-inversion-plot.ps")


def plot_black_and_white():
    n1 = [11, 10, 7]

    for x in range(12):
        plot2_bw(n1, inversion(n1, x), "ex-inversion-plot-bw-{0:02}.ps".format(x))

    n2 = [1, 3, 7, 9, 4]
    plot2_bw(n2, inversion(n2, 9), "ex-inversion-plot-bw.ps")


if __name__ == "__main__":
    plot_color()
    plot_black_and_white()
