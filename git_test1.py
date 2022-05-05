# Python program to explain os.system() method
	
# importing os module
import os

# Using readlines()
file1 = open('scripting2.txt', 'r')
every_lines = file1.readlines()

count = 0
# Strips the newline character
for each_line in every_lines:
	# count += 1
	# print("Line{}: {}".format(count, each_line.strip()))
    os.system(f"{each_line.strip()}")
    print("😊")
    # os.system(each_line.strip())


# 1. read from a file and

# 2. Go into a loop