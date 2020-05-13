#menu driven maths
#version 4
#olivia g 13/5/20
#in this version I am making the program loop until the user quits

#constant - operations offered in the menu
MENU_OPTIONS = [["Addition", "a"], ["Subtraction", "s"], ["Multiplication", "m"], ["Division", "d"], ["Quit", "q"]]

#integer input
int_one = int(input("Enter the first integer: "))
int_two = int(input("Enter the second integer: "))
print(int_one)
print(int_two)

while True:
    #choosing a menu option
    for i in MENU_OPTIONS:
        print("{}: press {}.".format(i[0], i[1]),end =" ")
    print()
    opt_choice = input("Choose one of these options: ")
    print(opt_choice)

    #performing the operation
    if opt_choice == MENU_OPTIONS[0][1]:
        print("{} + {} = {}".format(int_one, int_two, int_one + int_two))
    elif opt_choice == MENU_OPTIONS[1][1]:
        print("{} - {} = {}".format(int_one, int_two, int_one - int_two))
    elif opt_choice == MENU_OPTIONS[2][1]:
        print("{} * {} = {}".format(int_one, int_two, int_one * int_two))
    elif opt_choice == MENU_OPTIONS[3][1]:
        print("{} / {} = {:.2f}".format(int_one, int_two, int_one / int_two))
    else:
        print("Goodbye!")
        break
