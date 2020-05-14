#menu driven maths
#version 5
#olivia g 15/5/20
#in this version I am putting parts of the code into functions

#function that takes input from the user for the menu choice
def menu():
    for i in MENU_OPTIONS:
        print("{}: press {}.".format(i[0], i[1]),end =" ")
    print()
    opt_choice = input("Choose one of these options: ")
    print(opt_choice)
    return opt_choice

#putting the operations into functions to make the code easier to read
def addition(one, two):
    answer = one + two
    return answer

def subtraction(one, two):
    answer = one - two
    return answer

def multiplication(one, two):
    answer = one * two
    return answer

def division(one, two):
    answer = one / two
    return answer

#constant - operations offered in the menu
MENU_OPTIONS = [["Addition", "a"], ["Subtraction", "s"], ["Multiplication", "m"], ["Division", "d"], ["Quit", "q"]]

#integer input
int_one = int(input("Enter the first integer: "))
int_two = int(input("Enter the second integer: "))
print(int_one)
print(int_two)

while True:
    #choosing a menu option
    opt_choice = menu()
    #performing the operation
    if opt_choice == MENU_OPTIONS[0][1]:
        answer = addition(int_one, int_two)
        print("{} + {} = {}".format(int_one, int_two, answer))
    elif opt_choice == MENU_OPTIONS[1][1]:
        answer = subtraction(int_one, int_two)
        print("{} - {} = {}".format(int_one, int_two, answer))
    elif opt_choice == MENU_OPTIONS[2][1]:
        answer = multiplication(int_one, int_two)
        print("{} * {} = {}".format(int_one, int_two, answer))
    elif opt_choice == MENU_OPTIONS[3][1]:
        answer = division(int_one, int_two)
        print("{} / {} = {:.2f}".format(int_one, int_two, answer))
    else:
        print("Goodbye!")
        break
