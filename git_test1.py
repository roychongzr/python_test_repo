# Python program to explain os.system() method
	
# importing os module
import os

# Command to execute
# Using Windows OS command
cmd1 = 'git add .'
cmd2 = 'git commit -m "a new file using python on visual studio code" '
cmd3 = 'git branch -M main'
cmd4 = 'git remote add origin https://github.com/roychongzr/python_test_repo.git'
cmd5 = 'git push -u origin main'

# # Using os.system() method
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
os.system(cmd4)
os.system(cmd5)