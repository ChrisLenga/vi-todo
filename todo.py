import os

todo_list = []

def add_item(item):
    todo_list.append(item)
    print("Item added successfully.")

def remove_item(item):
    todo_list.remove(item)
    print("Item removed successfully.")

def view_list():
    print("Here's your to-do list:")
    for item in todo_list:
        print(item)

def menu():
    while True:
        print("--- To-Do List ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter the item: ")
            add_item(item)
        elif choice == 2:
            item = input("Enter the item: ")
            remove_item(item)
        elif choice == 3:
            view_list()
        elif choice == 4:
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()