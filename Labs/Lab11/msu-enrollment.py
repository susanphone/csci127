import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# April 17, 2020                                  |
# Susan McCartney                                 |
# -------------------------------------------------
#Graph data from a csv file. 

#Take the CSV file and return two np arrays of the college names and enrollments.
def read_file(file_name):
    file = open(file_name, "r")
    college = []
    enrollments = []
    for line in file:
        print(line)
        items = line.split(",")
        print(items)
        if len(items) == 2:
            college.append(items[0])
            enrollments.append(int(items[1]))
    file.close()
    return np.array(college), np.array(enrollments)
    # -------------------------------------------------

#Take the file data and produce a bar chart alternating dodgerblue and gold.
def main(file_name):
    college_names, college_enrollments = read_file(file_name)
    print(college_names, college_enrollments)
    colors=[]
    for i in range(len(college_names)):
        if i % 2 == 0:
            colors.append("gold")
        else:
            colors.append("dodgerblue")


    plt.figure('MSU Enrollments')
    plt.xticks(range(len(college_enrollments)), college_names)
    plt.ylim(0, 5000)
    plt.title("Spring 2020")
    plt.xlabel("College")
    plt.ylabel("Enrollment")
    plt.bar(range(len(college_enrollments)), college_enrollments, color=colors)
    plt.show()

# -------------------------------------------------


main("spring-2020.csv")
