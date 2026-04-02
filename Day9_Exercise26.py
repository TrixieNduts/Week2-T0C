import sys

def main():

        values = ([5,6,7,8])#creats a list.
        print(f"{values}")#prints the list.

        first_two = values[0:2]#creats a new list called first_two with the specified values only, using indexes (applies -1)
        print(f"{first_two}")#prints the new list containing the 2 specified values




if __name__ == "__main__":
    sys.exit(main())