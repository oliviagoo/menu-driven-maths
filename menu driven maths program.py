#menu driven maths
#version 2
#olivia g 13/5/20
#in this version I am doing the rest of the input

MENU_OPTIONS = [["Addition", "a"], ["Subtraction", "s"], ["Multiplication", "m"], ["Division", "d"], ["Quit", "q"]]

int_one = int(input("Enter the first integer: "))
int_two = int(input("Enter the second integer: "))
print(int_one)
print(int_two)

for i in MENU_OPTIONS:
    print("{}: press {}.".format(i[0], i[1]),end =" ")
print()
opt_choice = input("Choose one of these options: ")
print(opt_choice)
