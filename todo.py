import os
from datetime import datetime

todo_list = []

def add_item(item, priority, due_date):
    priority_map = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }
    priority = priority_map[priority]
    todo_list.append((item, priority, due_date))
    with open("todo.txt", "a") as file:
        file.write(item + "," + str(priority) + "," + due_date + "\n")
    print("Item added successfully.")

def remove_item(item):
    for i, tup in enumerate(todo_list):
        if tup[0] == item:
            todo_list.pop(i)
            with open("todo.txt", "w") as file:
                for t in todo_list:
                    file.write(t[0] + "," + str(t[1]) + "," + t[2] + "\n")
            print("Item removed successfully.")
            return
    print("Item not found.")

def view_list():
    global todo_list
    priority_map = {
        1: "Low",
        2: "Medium",
        3: "High"
    }
    try:
        with open("todo.txt", "r") as file:
            todo_list = [line.strip().split(',') for line in file]
            todo_list = [(t[0], priority_map[int(t[1])], t[2]) for t in todo_list]
        print("Here's your to-do list:")
        for item, priority, due_date in sorted(todo_list, key=lambda x: x[1]):
            print(f"{item} (Priority: {priority}) Due: {due_date}")
    except FileNotFoundError:
        todo_list = []
        print("The to-do list is empty.")

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
            priority = input("Enter the priority level (Low, Medium, High): ")
            due_date = input("Enter the due date (MM-DD-YYYY): ")
            add_item(item, priority, due_date)
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
