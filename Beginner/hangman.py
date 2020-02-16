# This will be similar to guessing the number, except we are guessing the word.
# The user needs to guess letters,
# Give the user no more than 6 attempts for guessing wrong letter.
# This will mean you will have to have a counter.
# You can download a ‘sowpods’ dictionary file or csv file to use as a way
# to get a random word to use.
from random import randint

def hangman():
    with open("hangman_sowpods.txt", "r") as sowpods:
        words = sowpods.readlines()
    word_index = randint(0, len(words)-1)
    word = words[word_index].lower().strip()
    words = []
    counter = 6

    letters = list(word)
    missing = ["_" for i in word]

    while counter:
        if not len(letters):
            print(f"Congratulations! You have guess the word: {word}")
            break
        inp = input(f"Guess a letter in the word: {''.join(missing)} ").lower()
        if inp in letters:
            print("You got a correct letter!")
            curr_index = -1
            while inp in letters:
                curr_index = word.index(inp, curr_index + 1)
                missing[curr_index] = inp
                letters.pop(letters.index(inp))
        else:
            counter -= 1
            print(f"Wrong answer, chances left: {counter}")
        if not counter:
            print("Game over!")
            print(f"The hidden word is {word}")
    return


hangman()