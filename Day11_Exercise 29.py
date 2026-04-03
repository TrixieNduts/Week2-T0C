import sys
from profile import Profile


def main():

    name = str(input("What is your name: "))#gets use input as str.
    age = int(input("What is your age: "))  # gets use input as int.
    country = str(input("What is your country of residence: "))  # gets use input as str.

    profile = [name, age, country]  # stores values in a list.

    print(f"Original list: {profile}")#prints the list.

    summary = [profile[0].upper(),profile[1] + 5,profile[2].lower()]

    print(f"Updated list: {summary}")#prints the results.

if __name__ == "__main__":
    sys.exit(main())