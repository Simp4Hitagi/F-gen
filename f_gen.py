import random
from random import randint
import time

def f_gen():
    user_name = input("What's your name?\n")
    print("Hi", user_name, "This is a random fact generator that prints 1 of 50 facts.\n")

    with open(r'50 Facts.txt', 'r') as file:
        contents = file.read()
        find() 

    #specified_time = 2 #seconds
    #time.sleep(specified_time)
    user_response = input("Would you like to see a random fact?\n")
    
    while user_response == str("Y"):
            print(contents[randint(1,50)])
            question1 = input("Would you like to see another random fact? (Y/N)\n")
            if question1 != str("Y"):
                break

f_gen()

#fact_num = eval(input("Enter fact number:\n"))

# find a way so that the randint doesn't repeat twice


# def search_str(file_path, word):
#     with open(file_path, 'r') as file:
#         # read all content of a file
#         content = file.read()
#         # check if string present in a file
#         if word in content:
#             print('string exist in a file')
#         else:
#             print('string does not exist in a file')

# search_str(r'E:\demos\files_demos\account\sales.txt', 'laptop')