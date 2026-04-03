import sys

def main():

    num1 = int(input("Kindly input random number1: "))#gets use input.
    num2 = int(input("Kindly input random number2: "))  # gets use input.
    num3 = int(input("Kindly input random number3: "))  # gets use input.
    num4 = int(input("Kindly input random number4: "))  # gets use input.

    num1 = num1 ** 2#gets the root od a number.
    num4 = num4 ** 3#gets the square of a number.
    nums = [num1, num2, num3, num4]  # storing integers in a list.

    print(f"{nums}")#prints the integers.

    nums = [num1 + num2 + num3 + num4]#computes the number list in a list.

    print(f"{nums}")#prints the results.





if __name__ == "__main__":
    sys.exit(main())