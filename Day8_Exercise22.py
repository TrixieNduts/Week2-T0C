import sys

def main():

        number1 = input("Kindly input the first number: ")#asking for user input
        number2 = input("Kindly input the second number: ")#asking for user input
        number3 = input("Kindly input the third number: ")#asking for user input

        numbers =[number1, number2, number3]#storing user input into a list

        print(f"{numbers}")#prints the list

        numbers[0] = int(numbers[0])#converts list to int
        numbers[1] = int(numbers[1])#converts list to int
        numbers[2] = int(numbers[2])#converts list to int

        print(f"Total = {numbers[0] + numbers[1]+ numbers[2]}")# prints the sum



if __name__ == "__main__":
    sys.exit(main())