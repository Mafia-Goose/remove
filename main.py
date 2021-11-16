import os


def work() -> object:
    xd = input("Insert file name ")
    if os.path.exists(xd):
        os.remove(xd)
        print()
        print("File successfully removed")

    else:
        print()
        print("The file does not exist")


work()
#it work now :troll:
