# open()
"""
"r" - Read
"a" - Append - creates the file if it does not exist, will append to the end of the file
"w" - Write - creates the file if it does not exist, will overwrite any existing content
"x" - Create - returns an error if the file exists
"""
"""
"t" - Text mode
"b" - Binary mode (e.g. images)
"""

f = open("files\myfile.txt", "x")
f.close()

f = open("files\myfile.txt", "w")
f.write("Hello! Welcome to files\myfile.txt:)")
f.close()

f = open("files\myfile.txt", "a")
f.write("This file is for testing purposes.")
f.write("Have a good day!")
f.close()

f = open("files\myfile.txt", "rt") # f = open("files\myfile.txt")
print(f.read()) # Hello! Welcome to files\myfile.txt:)This file is for testing purposes.Have a good day!
f.close()

f = open("files\myfile.txt", "rt")
print(f.read(5)) # 5 char # Hello
f.close()

f = open("files\myfile.txt", "rt")
print(f.readline())
print(f.readline())
print(f.readline())
# Hello! Welcome to files\myfile.txt:)This file is for testing purposes.Have a good day!
f.close()

f = open("files\myfile.txt", "rt")
for x in f:
  print(x) # Hello! Welcome to files\myfile.txt:)This file is for testing purposes.Have a good day!
f.close()

import os

if os.path.exists("files\myfile.txt"):
  os.remove("files\myfile.txt")
else:
  print("The file does not exist")

os.rmdir("files") # You can only remove empty folders.
# OSError: [WinError 145] The directory is not empty: 'files'