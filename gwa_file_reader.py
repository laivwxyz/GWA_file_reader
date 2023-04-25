# Dela Cruz, Lailanie E. _ BSCpE 1-4
# Assignment 4
# Programming Exercises 2

# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will outputs the name of the student who got the highest GWA (including the GWA).

def highest_gwa():
# create file named student_info.txt for reading
    with open('student_info.txt', 'r') as student_info:
        # initialize variables
        highest_gwa = 0
        highest_gwa_student = ''

        # read student_info.txt each line
        for line in student_info:
            # split the line into the student's name and their GWA
            name, gwa = line.strip().split(',')

            # convert the GWA to a float
            gwa = float(gwa)

            # check the students who have a highest GWA
            if gwa > highest_gwa:
                highest_gwa = gwa
                highest_gwa_student = name

        # print out the name of the student with the highest GWA
        print('\033[41m' + f'== The student with the highest GWA is {highest_gwa_student} with a GWA of {highest_gwa}.==')

highest_gwa()