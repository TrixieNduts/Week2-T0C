import sys

def main():

        items = ([10,20,30])#creats a list.
        copy = items[:]#creates a full copy by slicing with no strat or end.
        #copy.append(99)#a test to see the independency.
        print(f"Original: {items}")  # prints the original list.
        print(f"copy: {copy}")#prints the list copy.




if __name__ == "__main__":
    sys.exit(main())