#one way of importing modules
#from functions import get_todos, write_todos

#another way to import modules
#import functions

#for importing modules from a directory
from modules import functions
import time

now = time.strftime("%d-%b-%Y %H:%M:%S")
print("It is ", now)
while True:
    # Get user input and strip space characters from it
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    # Check if user action is add
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    #Check if user action is show
    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # Prints out items in list with a number next to them to correspond to the items index +1
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    # Check if user action is edit
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new ToDo: ")

            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your Command is not Valid!")
            continue

    # Check if user action is complete
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no index with that number.")
            continue

    #Check if user action is exit
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")

print('Bye!')