# Learning Outcomes

    Gain experience with matplotlib to display information.
    Continue to gain experience with numpy.

## Background

    The Registrars Office at Montana State University makes various enrollment statistics available.
    The file, Spring-2020.csv (below) captures some of the information that is available in the Spring 2020 Report G - Part A: Headcount Enrollment, All Students by Primary Major. The first line contains how many lines of data follow. Each subsequent line contains the name of one of MSU's colleges (such as CLS for the College of Letters & Science) followed by the Spring 2020 enrollment for that college.
## Read_file function
    The read_file function should return (1) a numpy array that contains each college name and (2) a corresponding numpy array that contains each college's enrollment.
## Main Function
    The main function should produce the desired bar graph using the information contained in the numpy arrays named college_names and college_enrollments.

## Assignment

    Write a program to generate a graph that matches the attached PNG image (below) as closely as possibly.

## Grading - 10 points

    1 point - The upper gray bar contains the words, "MSU Enrollments" and the tile reads, "Spring 2020"

    1 point - The x-axis is labeled College and the y-axis is labeled Enrollment.

    1 point - The y-axis goes from 0 to 5000 in increments of 1000.

    1 point - The x-axis contains the same college names that appear in the input file.

    2 points - The bar graph reflects the data in the file accurately.

    1 point - The colors of the bars in the bar graph alternate between "gold" and "dodgerblue".

    2 points - The function read_file returns (1) one numpy array that contains the names of the colleges and (2) a second numpy array that contains the enrollments of the colleges.
    
    1 point - The bar graph is created and plotted entirely in the main function.
