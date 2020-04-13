# --------------------------------------
# CSCI 127: Joy and Beauty of Data
# MatPlotLib Introductory Example
# --------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math

# --------------------------------------


def plot_line(x1, y1, x2, y2):
    """Plot a line using the specified points."""
    x = [x1, x2]
    y = [y1, y2]
# change lines to magenta dashes
    plt.plot(x, y, '--m')


# --------------------------------------

def plot_sine_wave(start_x, stop_x, amplitude):
    """Plot a sine wave."""
    x_array = np.linspace(start_x, stop_x, 1000)
    y_list = []
    for x in x_array:
        y_list.append(amplitude * math.sin(x))
#Change width of wave
    plt.plot(x_array, y_list, linewidth = 5)

# --------------------------------------

def main(graph_min, graph_max):

    # plt.xlim(graph_min, graph_max)
    # plt.ylim(graph_min, graph_max)
#replace limits with equivalent plt.axis statement
    plt.axis([graph_min, graph_max, graph_min, graph_max])

    plot_line(graph_min, graph_min, graph_max, graph_max)
    plot_line(graph_min, graph_max, graph_max, graph_min)
    plot_sine_wave(graph_min // 2, graph_max // 2, graph_max // 4)
#Label the x and y axis
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()

# --------------------------------------


main(-100, 100)
