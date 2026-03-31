import sys

def main():

        list = ([20,40,60,80,10,50])#creats a list.

        print(f"{list}")#prints the list.

        new_list = list[1:5]#creats a new list, specifying which numbers to be added to our list using indexing
        print(f"{new_list}")#prints the middle four numbers of the existing list.


if __name__ == "__main__":
    sys.exit(main())