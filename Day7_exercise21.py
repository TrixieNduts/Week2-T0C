import sys

def main():

    fruit = input("Kindly what is your favourite fruit: ")#user input is stored in a var called fruit
    colour = input("Kindly what is your favourite colour: ")#user input is stored in a var called colour
    city = input("Kindly what is your favourite city: ")#user input is stored in a var called city

    words =[fruit, colour, city]#My words converted to a list(stored)
    print(f"{words}")#prints the words in a list form

    words[1] = "UPDATE" #reassining the 2nd word a new value
    print(f"{words}")  # Replaces the second word using index 1

if __name__ == "__main__":
    sys.exit(main())
