import random

with open("words.txt", "r") as f:
    new_file = open("new_words.txt", "w+")

    for word in f:
        original = word.strip()
        if len(original) > 3:

            first_letter = original[0]
            last_letter = original[-1]
            other_letters = list(original[1:-1])
            new_word = first_letter

            while len(other_letters) > 0:
                letter = random.choice(other_letters)
                other_letters.remove(letter)
                new_word += letter

            new_word += last_letter
            new_file.write(new_word + "\n")

        elif not len(original) == 0:
            new_file.write(original + "\n")
    new_file.close()
