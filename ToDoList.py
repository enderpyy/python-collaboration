#python file succesfully created
#successfully spelled unsuccessfully
#ready to start programming

import time

to_do_list = []
    

def list_tasks():
    for i in range(len(to_do_list)):
        print(str(i + 1) + ": " + str(to_do_list[i]))



def console(user_input):
    print("""help - list all commands \n
add - add a task \n
view - list all tasks \n
mark - mark specific task as complete \n
delete - delete a task \n
exit - exit the console
""")
    while 1:
        user_input = str(input("Input command: ")).lower()
        if user_input == "add" or user_input == "a":
            new_task = str(input("Task name: "))
            to_do_list.append(new_task + "[]")
            print("")
        elif user_input == "view" or user_input == "v":
            list_tasks()
            print("")
        elif user_input == "mark" or user_input == "m":
            while 1:
                try:
                    complete_task = int(input("Enter an integer: "))-1
                    break  
                except ValueError:
                    print("Invalid input. Please enter an integer.\n")
            if complete_task + 1 > len(to_do_list):
                print("Invalid task, not in to do list\n")
            else:
                if to_do_list[complete_task][-1] != "\u2713]":
                    new_task = to_do_list[complete_task][:(len(to_do_list[complete_task])-1)]+ "\u2713]"
                    to_do_list[complete_task] = new_task
                else:
                    print("This task is already completed!")
            print("")
        elif user_input == "delete" or user_input == "d":
            list_tasks()
            delete_task = int(input("Which number task would you like to delete: "))
            to_do_list.pop(delete_task-1)
            print("")
        elif user_input == "exit" or user_input == "e":
            return
        elif user_input == "help" or user_input == "h":
            print("""help - list all commands \n
add - add a task \n
view - list all tasks \n
mark - mark specific task as complete \n
delete - delete a task \n
exit - exit the console
""")
        else:
            print("Invalid command. Type help for options.\n")

user_input = "h"

console(user_input)
