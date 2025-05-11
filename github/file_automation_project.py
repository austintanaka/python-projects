import os.path
import shutil
from datetime import datetime

history = []

while True:
    action = input("choose action move ,copy ,delete")
    try:
        if action == "move":
            a = input(r"please input the first data")
            b = input(r"please input the second data")
            shutil.move(a, b)
            print("success to move the data")
            history.append(f"{a} move to {b}")

        elif action == "copy":
            a = input(r"please input the first data")
            b = input(r"please input the second data")
            if os.path.isdir(a):
                shutil.copytree(a, b)
            else:
                shutil.copy(a, b)

            print("success to copy the data")
            history.append(f"{a} copy to {b}")

        elif action == "delete":
            a = input(r"please input the first data")
            shutil.rmtree(a)
            print("success to delete the data ")
            history.append(f"{a} delete")

        elif action == "history":
            if history:
                print("\nCalculation History:")
                for record in history:
                    print(record)

            else:
                print("No history yet!")

        elif action =="exit":
            print("exit.....")
            exit()


        else:
            print("Invalid action! Please choose move, copy, delete, history, or quit.")



    except FileNotFoundError:
        print("Error: Source path not found!")

    except Exception as e:
        print("Something went wrong:", e)



