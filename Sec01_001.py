##  -----  Section 1  -----  Getting Started
##  -----==========-----  L_001  Introduction to the course

##  -----==========-----  L_002  Skip the basics if you understand this code

# address = ["Flat Floor Street", "18", "New York"]
# pins = {"Mike" : 1234, "Joe" : 1111, "Jack" : 2222}
#
# print(address[0], address[1])
#
# pin = int(input("Please enter your PIN: "))
#
# def find_in_file(f):
#     myfile = open("sample.txt")
#     fruits = myfile.read()
#     fruits = fruits.splitlines()
#     if f in fruits:
#         return "That fruit is in the list."
#     else:
#         return "No such fruit found!"
#
# if pin in pins.values():
#     fruit = input("Please enter fruit: ")
#     print(find_in_file(fruit))
# else:
#     print("Incorrect PIN!")
#     print("This information can only be accessed by: ")
#     for key in pins.keys():
#         print(key)

##  -----==========-----  L_003  Note: Instructor will use Python on a remote server for a few lessons.

##  -----==========-----  L_004  Your first Python program

# print("Hello!")

##  -----==========-----  L_005  The command line

##  pwd    "present working directory"  Show full path to present directory
##  ls    list contents of present directory
##  mkdir basics    create folder "basics"
##  cd X    "change directory"
##  cd ..    change to one directory "up"
##  touch myfile.txt    create an empty file named "myfile.txt"
##  rm myfile.txt    remove "myfile.txt"
##  cp ../myprogram.py .    copy a file from one level up to "here"
##  cp ../myprogram.py dog.py    copy a file from one level up to "here" and rename the file
##  cp myprogram.py basics/.    copy a file from here to one level down to "basics" folder
##  clear    clear the console of messages
##  mv myprogram.py basics/myprogram1.py    mv a file one level down and rename it
##  rm -r basics    remove all files in a directory and the directory

##  -----==========-----  L_006  The python shell  -----  idle

# $ python3
# >>> print("Hello!")
# Hello!
# >>> 3 + 4
# 7
# >>> exit()

