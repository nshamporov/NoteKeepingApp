import os
from os import listdir
from os.path import isfile, join 
import importlib
import sys

def main():
    while True:
                                #Printing Choices
        title = "Note Keeping App"
        print(f"\n{'=' * 10} {title} {'=' * 10}")
        print("\nWhat would you like to do?\n")
        print("1. Add new note.")
        print("2. View a note.")
        print("3. Edit a note.")
        print("4. Delete a note.")
        print("\n5. Exit")


        user_choice = input("\nEnter number 1, 2, 3, 4, or 5: ")  

                                #Function to transfer to the module of the specified choice
        if user_choice == "1":
            add = importlib.import_module("add")
            add.create()
        elif user_choice == "2":
            view = importlib.import_module("view")
            view.view()
        elif user_choice == "3":
            edit = importlib.import_module("editing")
            edit.edit()
        elif user_choice == "4":
            delete = importlib.import_module("delete")
            delete.delete()
        elif user_choice == "5":
            print("\n===>See you next time!" + f"\n\n{'=' * 38}")       #Exits the program
            break
        else:
            print("\n/ / / Wrong input. Try again. / / /")

if __name__ == "__main__":
    main()


#Need documentation
