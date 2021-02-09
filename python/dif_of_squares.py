#checks if file exists, if not, makes and gives starting number
import os
if os.path.exists("squareroots.txt") is False:
    with open("squareroots.txt", "w") as file1:
        file1.write("number, square, difference"+"\n")
        file1.write("0")
#        print("File Made")
#else:
#     print("File's already there. Let's expand it.")

#starts for last line's value
with open("squareroots.txt", "r") as file1:
    last_line = file1.readlines()[-1]
    last_number = int(last_line.split(",")[0])

if last_number == 0:
    y = 0
else:
    y=(last_number)**2

print("There are {0} squares so far.".format(last_number))
bigger_by =  int(input("How many more do you want?" + "\n"))

with open("squareroots.txt", "a") as file1:
    for n in range(last_number+1, last_number+1+bigger_by):
        x = n**2
        z = x - y
        a = z - i #x - y - i (number - diference - 
        file1.write(str(n) + ", " + str(x) + ", " + str(z) + ", " + str(a) + ";\n")
        y = x
