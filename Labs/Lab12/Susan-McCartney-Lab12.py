import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# April 23, 2019                                  |
# Susan McCartney                                 |
# -------------------------------------------------

def process(file_name):
    # read the file_name into a pandas dataframe
    file = pd.read_csv(file_name)
    print(file)
    data = pd.DataFrame(file_name, columns= pd.DataFrame(columns))
    print(data)
    
    #labels found from DataFrame.column on source-----column headers
    #use lesson1.py
    # sort and plot the dataframe using arguments "title", "legend", "x", "y", and "kind"

    #which title to sort
    # # The only statements that may use the matplotlib library appear next.

    # # Do not modify them.
    # plt.xlabel(x_axis)      # Note: x-axis should be determined above
    # plt.ylabel(y_axis)      # Note: y-axis should be determined above
    # plt.show()

# -------------------------------------------------


process("MSU College Enrollments.csv")
process("CS Faculty.csv")
