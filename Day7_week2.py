import sys

def main():

    fruit = input("Kindly what is your favourite fruit: ")
    colour = input("Kindly what is your favourite colour: ")
    city = input("Kindly what is your favourite city: ")

    words =[fruit, colour, city]

    print(f"{words}")

if __name__ == "__main__":
    sys.exit(main())