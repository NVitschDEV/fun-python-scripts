import random

swiss_grades = [1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6]
german_grades = [6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1]
american_grades = [
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "B",
    "B",
    "B",
    "B",
    "C",
    "F",
]
french_grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def grademaker():
    grades = []
    number = 1

    while number == 1:
        s1 = input(
            "What grading System would you like to use? 1. Swiss, 2. German, 3. American System, 4. French System "
        )
        print("'done' when you are done")
        if s1 == "1":
            print("Swiss System")
            print("This is the Grade of your Student:")
            grade_random = random.choice(swiss_grades)
            print(grade_random)
            grades.append(grade_random)
        elif s1 == "2":
            print("German System")
            print("This is the Grade of your Student:")
            grade_random = random.choice(german_grades)
            print(grade_random)
            grades.append(grade_random)
        elif s1 == "3":
            print("American System")
            print("This is the Grade of your Student:")
            grade_random = random.choice(american_grades)
            print(grade_random)
            grades.append(grade_random)
        elif s1 == "4":
            print("French System")
            print("This is the Grade of your Student:")
            grade_random = random.choice(french_grades)
            print(grade_random)
            grades.append(grade_random)
        elif s1 == "done":
            number = 2
        else:
            print("please enter something valid!")

    print(f"Here are the realistic Grades: {grades}")


grademaker()
