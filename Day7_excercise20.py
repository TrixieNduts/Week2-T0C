import sys

def main():

    fruit = input("Kindly what is your favourite fruit: ")#user input is stored in a var called fruit
    colour = input("Kindly what is your favourite colour: ")#user input is stored in a var called colour
    city = input("Kindly what is your favourite city: ")#user input is stored in a var called city

    words =[fruit, colour, city]#My words converted to a list(stored)
    print(f"{words}")#prints the words in a list form

    print(F"{words[0]}")#prints 1st word on my list
    print(F"{words[2]}")#prints last word on my list
    print(F"{len(words)}")#counts my list items



if __name__ == "__main__":
    sys.exit(main())