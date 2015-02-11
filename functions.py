# Creates the to do list menu
def menu():
    print "1 = add a task"
    print "2 = delete a task"
    print "3 = mark task complete"
    print "4 = view tasks"
    print "5 = exit"

    # Asks the user what they want to do
    selection = raw_input("What do you want to do?: ")

    # Prompts the user to select an appropriate number
    while int(selection)not in range(1, 6):
        selection = raw_input("Please enter a number between 1 and 5: ")

    return selection

# Function adds item to list
def add_item(list):
    # Asks user to input a task
    task = raw_input("What do you need to do?: ")
    list.append(task)
    print "Your task has been added."

    return list

# Function removes item from list
def remove_item(list):

    # A counter to number each task in the list so the user can select which task to remove
    i = 1

    # Defines task as the items in list
    for task in list:
        print str(i) + " " + task
        # += is a shorthand for incrementing. This will increment by 1.
        i += 1
    selection = raw_input("What do you want to remove?: ")

    # Len is length
    while selection not in [str(i) for i in range(1, len(list) + 1)]:
        selection = raw_input("Please enter a number 1 through " + str(len(list)) + ": ")
    # index is the number in the list. Index starts with 0. User will not start with 0.
    # Change user input so computer can use it.
    list.pop(int(selection)-1)
    print "Your task has been removed."

    return list

# Function marks task as complete
# Can do this way but easier as a class, for future reference
def complete(list, completed_list):
    i = 1
    for task in list:
        print str(i) + " " + task
        i += 1
    print "All"
    selection = raw_input("Which task(s) did you complete?: ")

    # ! means the opposite. So here, if selection doesn't == All
    if selection != "All":
        while selection not in [str(i) for i in range (1, len(list) + 1)]:
            selection = raw_input("Please enter a number 1 through " + str(len(list)) + ": ")
        # Moves item/s to the completed list
        completed_list.append(int(selection)-1)
        list.pop(int(selection)-1)
        print "Your task is complete."
    else:
        completed_list += list
        # Clears out list
        list = []
        print "All of your tasks are complete."

    return list, completed_list

# shows the user a list of current tasks or finished tasks
def view_tasks(list, completed_list):
    print completed_list
    print "Choose 1 for current tasks"
    print "Choose 2 for completed tasks"
    selection = raw_input("Do you want to see current tasks or completed tasks?: ")

    while int(selection) not in range(1,3):
        selection = raw_input("Please choose 1 or 2: ")

    if int(selection) == 1:
        for task in list:
            print task
    else:
        for task in completed_list:
            print task

