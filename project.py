from tabulate import tabulate
import os

meun = [
    [1, "Add a new task"],
    [2, "Remove a task"],
    [3, "Modify existing tasks"],
    [4, "View tasks"],
    [9, "Exit"]
]
headers = ["Index", "Choices"]
header1 = ["Index", "Tasks"]
choices = [1, 2, 3, 4, 9]
tasks = []
showtasks = []

def main():
    os.system('clear')
    import_file()
    while True:
        choice = get_choice()
        if choice == 1:
            new_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            modify_tasks()
        elif choice == 4:
            os.system('clear')
            view_tasks()
            print("------------------------------------------------")
            print("The tasks is showed.")
            print("------------------------------------------------")
        else:
            save_tasks()
            print("------------------------------------------------")
            print("Thank you for your using! All the things are saved.")
            print("------------------------------------------------")
            break

def import_file():
    try:
        with open("tasks.txt", "r") as file:
            global tasks
            tasks = [line.strip() for line in file.readlines() if line.strip()]
            print("Tasks imported successfully!")
    except FileNotFoundError:
        print("No tasks file found. Starting with an empty task list.")
    except Exception as e:
        print(f"An error occurred while importing tasks: {e}")

def get_choice():
    while True:
        try:
            print(tabulate(meun, headers, tablefmt="heavy_grid"))
            choice = input("What is your choice: ")
            choice = int(choice)
            if choice in choices:
                return choice
            else:
                raise ValueError
        except:
            os.system('clear')
            print("------------------------------------------------")
            print("Invalid input, please input again!")
            print("------------------------------------------------")

def new_task():
    os.system('clear')
    newtask = input("What is your task: ")
    tasks.append(newtask.strip())
    view_tasks()
    print("------------------------------------------------")
    print("The task is added!")
    print("------------------------------------------------")

def remove_task():
    os.system('clear')
    while True:
        try:
            view_tasks()
            removetaskindex = input("Which task you want to remove: ")
            removetaskindex = int(removetaskindex)
            if removetaskindex < int(len(tasks)):
                tasks.remove(tasks[removetaskindex])
                print("------------------------------------------------")
                print("The task is removed!")
                print("------------------------------------------------")
                break
            else:
                raise ValueError
        except:
            os.system('clear')
            print("------------------------------------------------")
            print("Invalid input, please input again!")
            print("------------------------------------------------")

def modify_tasks():
    os.system('clear')
    while True:
        try:
            view_tasks()
            index = input("Which task you want to modify: ")
            index = int(index)
            if index < len(tasks):
                tasks[index] = input("Please enter your modification: ")
                print("------------------------------------------------")
                print("The task is modified!")
                print("------------------------------------------------")
                break
            else:
                raise ValueError
        except:
            os.system('clear')
            print("------------------------------------------------")
            print("Invalid input, please input again!")
            print("------------------------------------------------")

def view_tasks():
    print("Here is the task info:")
    i = 0
    for i in range(len(tasks)):
        showtasks.append([i,tasks[i]])
        i += 1
    print(tabulate(showtasks, header1, tablefmt="heavy_grid"))
    showtasks.clear()

def save_tasks():
    try:
        with open('tasks.txt', 'w') as file:
            for task in tasks:
                file.write(f'{task}\n')
        print('Tasks saved successfully!')
    except Exception as e:
        print(f'An error occurred while saving tasks: {e}')

if __name__ == "__main__":
    main()
