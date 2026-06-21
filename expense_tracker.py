tasks = []


print("----- To-Do List Application -----")


while True:


    print("\n1. Add Task")

    print("2. View Task")

    print("3. Remove Task")

    print("4. Exit")


    choice = int(input("Enter your choice: "))



    if choice == 1:


        task = input("Enter new task: ")


        tasks.append(task)


        print("Task added successfully")



    elif choice == 2:


        print("\nYour Tasks:")


        if len(tasks) == 0:

            print("No tasks available")


        else:

            for i in range(len(tasks)):

                print(i+1, ".", tasks[i])





    elif choice == 3:


        number = int(input("Enter task number to remove: "))


        tasks.pop(number-1)


        print("Task removed successfully")





    elif choice == 4:


        print("Thank you!")

        break



    else:


        print("Invalid choice")