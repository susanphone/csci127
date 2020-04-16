import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# April 16, 2020                                  |
# Susan McCartney                                 |
# -------------------------------------------------


def read_file(file_name):
   csv = np.array("spring-2020.csv", delimiter=',')
   college = csv[:,1]
   population = csv[:,2]


    # -------------------------------------------------


def main(file_name):
    college_names, college_enrollments = read_file(file_name)

    print(college_names, college_enrollments
    # for name in file_name:
    #     if name == "Arts" or name == "EHHD College" or name == "NACOE":
    #         plt.color = "dodgerblue"
    #     else:
    #         plt.color = "gold"
    # college_enrollments = [1000, 2000, 3000, 4000, 5000]
    plt.bar(college_names, college_enrollments)
    plt.title("Spring 2020")
    plt.xlabel("College")
    plt.ylabel("Enrollment")
    plt.show()


# -------------------------------------------------


main("spring-2020.csv")
