#menu driven maths
#version 8
#olivia g 15/5/20
#in this version I am commenting out print lines that are for testing

#function that forces the user to enter an integer
def forceint(msg):
    while True:
        try:
            number = int(input(msg))
            break
        except ValueError:
            print("Please enter a valid whole number.")
    return number 

#function that takes input from the user for the menu choice
def menu():
    for i in MENU_OPTIONS:
        print("{}: press {}.".format(i[0], i[1]),end =" ")
    print()
    opt_choice = input("Choose one of these options: ")
    #print(opt_choice)
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

#main routine
#constant - operations offered in the menu
MENU_OPTIONS = [["Addition", "a"], ["Subtraction", "s"], ["Multiplication", "m"], ["Division", "d"], ["Quit", "q"]]

#integer input
int_one = forceint("Enter the first integer: ")
int_two = forceint("Enter the second integer: ")
#print(int_one)
#print(int_two)

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
    #ends the loop and finishes the program
    elif opt_choice == MENU_OPTIONS[4][1]:
        print("Goodbye!")
        break
    #if it is none of these options, it must be an invalid input
    else:
        print("Please choose a valid option")
