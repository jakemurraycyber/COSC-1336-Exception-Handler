################################################
#                                              #
# This is a program that averages the numbers  #
# from an external file                        #
#                                              #
# By: Jake Murray                              #
# Date: 3/29/25                                #
# Version: 1.0.0                               #
#                                              #
################################################

# Set Flag variable to determine if file is valid and can be read
validFile = True
infile = None

# if file is not valid, inform user and end the program
try:
    infile = open("numbers10.txt", 'r')
except IOError:
    print("Valid file not found. Please try again.")
    validFile = False

# If a valid file is provided, proceed with program
if validFile:
    counter = 0
    total = 0

    for line in infile:
        try:
            total += int(line)
            counter += 1
        # if line is not number, throw error, end program
        except ValueError:
            print("The file can only contain numbers. Please try again.")
            flag = False
            break

    # If file and all lines were valid, produce the average of the numbers encountered
    if validFile:
        # Only calculate the average if the counter does not equal 0
        if counter != 0:
            average = total / counter
            print(f"The average is: {average}.")
    infile.close()
