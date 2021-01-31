# Name: Arjot Singh Rai
# 7Shifts coding exercise
# Run as follows:
#   python add.py
#   or
#   python3 add.py

import re

# function to run tests
def Add_test():
    error_count = 0

    if Add("") != 0:
        print("Error: Adding an empty string should result into 0!")
        error_count += 1
    if Add("1") != 1:
        print("Error: Adding a string with one element should result into the number itself!")
        error_count += 1
    if Add("1,2,5") != 8:
        print("Error: Adding a set of numbers did not give the correct result!")
        error_count += 1
    if Add("1\n,2,5") != 8:
        print("Error: New lines resulting in incorrect addition!")
        error_count += 1
    if Add("1,2\n,5") != 8:
        print("Error: New lines resulting in incorrect addition!")
        error_count += 1
    try:
        if Add("1, 2 \n , 3") != 6:
            print("Error: Entering random spaces resulting in incorrect output!")
            error_count += 1
    except:
        print("Error: Entering random spaces causing an exception!")
        error_count += 1
    try:
        Add("-1,2,3")
        print("Error: Entering a negative number is not raising an exception!")
        error_count += 1
    except:
        pass
    try:
        if Add("//@1@2@3") != 6:
            print("Error: Custom delimiter resulted in wrong output.")
            error_count += 1
    except:
        print("Error: Entering custom delimiter causing an exception!")
        error_count += 1
    try:
        if Add("//@@\n1@@2@@3") != 6:
            print("Error: delimiter with arbitrary length resulted in wrong output.")
            error_count += 1
    except:
        print("Error: Entering delimiter with arbitrary length causing an exception!")
        error_count += 1

    try:
        if Add("//@+\n1@2++3") != 6:
            print("Error: use of multiple delimiters resulted in wrong output.")
            error_count += 1
    except:
        print("Error: Entering multiple delimeters causing an exception!")
        error_count += 1

    print("Total number of errors: ", error_count)

# helper function to return a tuple which contains a regex string and the new string without the control code
def get_delimiters(input_string):
    delimiters = set()

    i = 2 # loop counter

    while input_string[i] != "\\n" and not input_string[i].isdigit():
        if input_string[i] not in delimiters:
            delimiters.add(input_string[i])
        i = i + 1
    return "[" + "".join(delimiters) +"]+", input_string[i:]

def Add(input_string):
    if input_string == "":
        return 0
    delimiter = "[,]+" #default delimiter
    if input_string[0:2] == "//":
        delimiter, input_string = get_delimiters(input_string)

    # clean up the string so that its ready to be split, then split using the delimiter
    split_string = re.split(delimiter, input_string)

    total = 0
    negative_number_list = []

    # calculate the sum
    for i in split_string:
        #strip() removes any whitespace character around strings
        try:
            cur_number = int(i.strip().strip("\\n"))
            if cur_number <= 1000: # bonus challenge 1
                if cur_number < 0:
                    negative_number_list.append(str(cur_number))
                total += cur_number
        except:
            raise Exception("String cannot be split properly!")

    # check if there were any negative numbers
    # if there were negative numbers throw an exception
    if len(negative_number_list) > 0:
        raise Exception("Negatives not allowed! The negative numbers inputted are: " + ",".join(negative_number_list))

    return total

if __name__ == "__main__":
    while True:
        input_string = input("Enter a string(q or Q to quit): ")
        if input_string == "q" or input_string == "Q":
            break
        result = Add(input_string)
        print("The result for ", input_string, " is: ", result)

    print("\n************RUNNING TESTS****************")
    Add_test()