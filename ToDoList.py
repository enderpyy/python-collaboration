#python file succesfully created
#successfully spelled unsuccessfully
#ready to start programming

import time

#stores tasks
to_do_list = []
    
#lists all tasks in to do list, formatted
def list_tasks():
    for i in range(len(to_do_list)):
        print(str(i + 1) + ": " + str(to_do_list[i]))


#runs the console on which the user can interact with their to do list
def console():
    #initial help command
    print("""help - list all commands \n
add - add a task \n
view - list all tasks \n
mark - mark specific task as complete \n
delete - delete a task \n
exit - exit the console
""")
    while 1:
        #user inputs command
        user_input = str(input("Input command: ")).lower()
        #adding tasks - all tasks have a 1 letter shortcut
        if user_input == "add" or user_input == "a":
            new_task = str(input("Task name: "))
            to_do_list.append(new_task + "[]") #[] is the check box
            print("")
        # view all tasks
        elif user_input == "view" or user_input == "v":
            list_tasks()
            print("")
        # mark a task as complete using a number, the number appears when the user lists tasks
        elif user_input == "mark" or user_input == "m":
            while 1:
                try:
                    complete_task = int(input("Enter an integer: "))-1
                    break  
                except ValueError: #if they dont input a number
                    print("Invalid input. Please enter an integer.\n")
            if complete_task + 1 > len(to_do_list) or complete_task < 0:
                print("Invalid task, not in to do list\n")
            else:
                if to_do_list[complete_task][-1] != "\u2713]": #u2713 - unicode for checkmark
                    new_task = to_do_list[complete_task][:(len(to_do_list[complete_task])-1)]+ "\u2713]"
                    to_do_list[complete_task] = new_task
                else:
                    print("This task is already completed!")
            print("")
        #delete tasks
        elif user_input == "delete" or user_input == "d":
            list_tasks()
            while 1:
                try:
                    delete_task = int(input("Which number task would you like to delete: ")) - 1
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            if delete_task + 1 > len(to_do_list) or delete_task < 0:
                print("Invalid task, not in to do list\n")
            else:
                to_do_list.pop(delete_task)
                print("")
        #exit console
        elif user_input == "exit" or user_input == "e":
            return
        #help command
        elif user_input == "help" or user_input == "h":
            print("""help - list all commands \n
add - add a task \n
view - list all tasks \n
mark - mark specific task as complete \n
delete - delete a task \n
exit - exit the console
""")
        #if user enters wrong command
        else:
            print("Invalid command. Type help for options.\n")

#run console
console()
