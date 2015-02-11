exit = False
from functions import *
list = []
completed_list = []

while exit is not True:
    selection = menu()

    if selection == "1":
        list = add_item(list)
    elif selection == "2":
        list = remove_item(list)
    elif selection == "3":
        list, completed_list = complete(list, completed_list)
    elif selection == "4":
        view_tasks(list, completed_list)
    elif selection == "5":
        exit = True


