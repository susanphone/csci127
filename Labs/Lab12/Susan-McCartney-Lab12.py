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
    dataframe = pd.read_csv(file_name)
    for file in dataframe:
        lab = pd.DataFrame(dataframe, columns=["College Name", "College Enrollemnt", "CS Professor", "Years at MSU"])
    #     data.to_csv('lab12.csv', index=False, header=True)
    # lab = pd.read_csv('lab12.csv', names=['College Name', 'College Enrollment', 'CS Professor', 'Years as MSU'])
    # if (lab.'College Enrollment'.dtype == 'int'):
    #     print(lab.'College Enrollment'.dtype)
    sorted_data1 = lab.sort_values(['College Enrollment'])
    sorted_data2 = lab.sort_values(['Years at MSU'])
    # print(sorted_data1, sorted_data2)
    lists = [sorted_data1, sorted_data2]
    # data = pd.DataFrame(file_name)
    # print(data)
    
    #labels found from DataFrame.column on source-----column headers
    #use lesson1.py

    # sort and plot the dataframe using arguments "title", "legend", "x", "y", and "kind"
#which title to sort
    if lists == sorted_data1:
        x_axis = 'College Enrollment'
        y_axis = 'College Name'
        title = 'fig1'
    if lists == sorted_data2:
        x_axis = 'CS Professor'
        y_axis = 'Years at MSU'
        title = 'fig2'
    # The only statements that may use the matplotlib library appear next.
    lists.plot(x= x_axis, y= y_axis, kind='bar')
    
    plt.title(title)
    # Do not modify them.
    plt.xlabel(x_axis)      # Note: x-axis should be determined above
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    plt.show()

# -------------------------------------------------

process("MSU College Enrollments.csv")
process("CS Faculty.csv")
