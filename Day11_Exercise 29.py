import sys

def main():

    name = str(input("What is your name: "))#gets use input.
    age = int(input("What is your age: "))  # gets use input.
    country = str(input("What is your country of residence: "))  # gets use input.

    profile = [name, age, country]  # storing integers in a list.

    print(f"{profile}")#prints the integers.

    #nums = [num1 + num2 + num3 + num4]#computes the number list in a list.

    #print(f"{nums}")#prints the results.

if __name__ == "__main__":
    sys.exit(main())