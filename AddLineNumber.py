#!/usr/bin/python
import re, string, sys

input_file_found = None
try:
    file_path = sys.argv[1].strip()
    # note the first argument is the 'file_name.py'
    file = open(file_path, "r")
    text_list = file.readlines()
    file.close()

    for i in range(len(text_list)):
        text_list[i] = str(i + 1) + ": " + text_list[i]

    file = open(file_path, "w")
    for line in text_list:
        print(line, file=file)
    file.close()

except FileNotFoundError:
    print("File was not found.")

