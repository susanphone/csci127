import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# April 23, 2020                                  |
# Susan McCartney                                 |
# -------------------------------------------------
#Turn a CSV into bar charts.

def process(file_name):
    # read the file_name into a pandas dataframe
    dataframe = pd.read_csv(file_name)
    #sort the values
    dataframe = dataframe.sort_values(dataframe.columns[1], ascending=False)
    dataframe.plot.bar(x= dataframe.columns[0])
    #set titles, x-axis, y-axis
    plt.title(file_name.replace(".csv", ""))
    x_axis = dataframe.columns[0]
    y_axis = dataframe.columns[1]
    
    #pre-determined labels
    plt.xlabel(x_axis)      # Note: x-axis should be determined above
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    plt.show()

# -------------------------------------------------

process("MSU College Enrollments.csv")
process("CS Faculty.csv")
