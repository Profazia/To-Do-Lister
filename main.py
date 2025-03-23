from time import sleep
import pickle
import os
previous_tasks = {}

def saveTasks():
    with open("list.pydata", "wb") as list:
        pickle.dump(previous_tasks, list)

def getUserInput():
        print("\n---Options---:")
        print("1. Add a new task")
        print("2. Mark a task as completed")
        print("3. Delete a task")
        print("4. Display a list of tasks")
        print("5. Exit")
        try:
            userInput = int(input("\nEnter option number: "))
        except ValueError as e:
            print("\nEnter a number only")
            return False
        if (userInput > 5 or userInput < 1):
            print("\nPlease enter a option number")
            return False
        return userInput

def matchUserInput(userInput):
        match userInput:
            case 1:
                taskName = input("Enter task title: ")
                previous_keys = previous_tasks.keys()
                if (taskName in previous_keys):
                    print("\nTask already exists.")
                    return False
                else:
                    previous_tasks[taskName] = "Not Done"
                    saveTasks()
                    print("\nTask added successfully.")
                    return False
            case 2:
                index = 0
                tasks = [task for task in previous_tasks.keys() if previous_tasks[task] == "Not Done"]
                if len(tasks) > 0:
                    for task in tasks:
                        index += 1
                        print(f"{index}. {task}")
                    updateIndex = input("\nChoose a task: ")
                    try:
                        updateIndex = int(updateIndex)
                    except ValueError as e:
                        print("\nEnter a number only")
                        return False
                    else:
                        if (updateIndex > index or updateIndex < 1):
                            print("Enter a correct option number")
                            return False
                    taskName = tasks[updateIndex - 1]
                    previous_tasks[taskName] = "Done"
                    saveTasks()
                    print("\nTask marked as completed.")
                    return False
                else:
                    print("\nNo tasks left to mark as completed.")
                    return False
            case 3:
                index = 0
                tasks = [task for task in previous_tasks.keys()]
                if len(tasks) > 0:
                    for task in tasks:
                        index += 1
                        print(f"{index}. {task}: {previous_tasks[task]}")
                    updateIndex = input("\nChoose a task: ")
                    try:
                        updateIndex = int(updateIndex)
                    except ValueError as e:
                        print("\nEnter a number only")
                        return False
                    else:
                        if (updateIndex > index or updateIndex < 1):
                            print("\nEnter a correct option number")
                            return False
                    taskName = tasks[updateIndex - 1]
                    previous_tasks.pop(taskName)
                    saveTasks()
                    print("Task deleted.")
                    return False
                else:
                    print("\nNo tasks to delete.")
                    return False
            case 4:
                index = 0
                to_do_list = previous_tasks.keys()
                if (len(to_do_list) > 0):
                    for task in to_do_list:
                        index += 1
                        print(f"{index}. {task}: {previous_tasks[task]}")
                    return False
                else:
                    print("\nNo Tasks To Display")
                    return False
            case 5:
                print("\nExiting...")
                return True
            
            

print("Welcome to To-Do Lister")
try:
    if not os.path.exists("list.pydata"):
        with open("list.pydata", "w+b") as list:
            pickle.dump({}, list)
    with open("list.pydata", "r+b") as file_list:
        if (file_list.read(0)):
            data = pickle.load(file_list)
            if (len(data.keys()) > 0):
                index = 0
                previous_tasks = data
                print("Previous Data -> ")
                for key in data.keys():
                    value = data[key]
                    index += 1
                    print(f"{index}. {key} -> Status: {value}")
            else: 
                print("\nNo previous data found.")
                pickle.dump({}, file_list)
                previous_tasks = {}
        else: 
            print("\nNo previous data found.")
            pickle.dump({}, file_list)
            previous_tasks = {}
    while True:
        userInput = getUserInput()
        if (userInput == False):
            continue
        matchedUserInput = matchUserInput(userInput)
        if (matchedUserInput == False):
            continue
        elif (matchedUserInput == True):
            break
        else:
            break
except Exception as e:
    print("\nSome Error Occured ! Exiting in 3 seconds.", e)
    sleep(3)