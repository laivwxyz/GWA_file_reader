# Dela Cruz, Lailanie E. _ BSCPE 1-4
# Assignment 4
# Programming Exercises 2

# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will outputs the name of the student who got the highest GWA (including the GWA).

def highest_gwa():
# create file named students_info.txt for reading
    with open('student_info.txt', 'r') as student_info:
        # initialize variables
        # read students_info.txt each line
            # split the line into the student's name and their GWA
            # convert the GWA to a float
            # check the students who have a highest GWA
        # print out the name of the student with the highest GWA

highest_gwa()