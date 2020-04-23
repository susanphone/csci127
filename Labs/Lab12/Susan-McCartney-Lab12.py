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
    df = pd.read_csv(file_name, header=0)
    # print(df)
    dataset = pd.DataFrame(data=df, index=None)
    print(dataset)



    # data = pd.DataFrame(file_name)
    # print(data)
    
    #labels found from DataFrame.column on source-----column headers
    #use lesson1.py
    # sort and plot the dataframe using arguments "title", "legend", "x", "y", and "kind"
    data_chart = pd.Series(['College Enrollment'], ['Years at MSU'])
    #which title to sort
    if data_chart == 'College Enrollemnt':
        x_axis = 'College Enrollment'
        y_axis = 'College Name'
        plt.title = 'fig1'
    if data_chart == 'Years at MSU':
        x_axis = 'CS Professor'
        y_axis = 'Years at MSU'
        plt.title = 'fig2'
    # # The only statements that may use the matplotlib library appear next.
    # data_chart.plot(x= x_axis, y= y_axis, kind='bar')
    # Do not modify them.
    plt.xlabel(x_axis)      # Note: x-axis should be determined above
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    plt.show()

# -------------------------------------------------


process("MSU College Enrollments.csv")
process("CS Faculty.csv")
