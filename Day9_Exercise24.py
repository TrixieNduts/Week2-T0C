import sys

def main():

    word1 = input("Kindly input random word1: ")
    word2 = input("Kindly input random word2: ")
    word3 = input("Kindly input random word3: ")
    word4 = input("Kindly input random word4: ")
    word5 = input("Kindly input random word5: ")

    words = [word1, word2, word3, word4, word5]
    print(f"{words}")

    a_words = words[0].lower() == 'a'
    print(f"{a_words}")

if __name__ == "__main__":
    sys.exit(main())