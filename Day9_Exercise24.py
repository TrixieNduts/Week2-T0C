import sys

def main():

    word1 = input("Kindly input random word1: ")
    word2 = input("Kindly input random word2: ")
    word3 = input("Kindly input random word3: ")
    word4 = input("Kindly input random word4: ")
    word5 = input("Kindly input random word5: ")

    words = [word1, word2, word3, word4, word5]
    print(f"{words}")

    a_words = []

    if words[0][0].lower() == 'a':
        a_words = a_words + [words[0]]

    if words[1][0].lower() == 'a':
        a_words = a_words + [words[1]]

    if words[2][0].lower() == 'a':
        a_words = a_words + [words[2]]

    if words[3][0].lower() == 'a':
        a_words = a_words + [words[3]]

    if words[4][0].lower() == 'a':
        a_words = a_words + [words[4]]


    print(f"Words beginning with 'a' or 'A': {a_words}")

if __name__ == "__main__":
    sys.exit(main())