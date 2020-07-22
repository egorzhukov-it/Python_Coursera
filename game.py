import random

number = random.randint(0, 101)

while True:

    answer = input("Введите число: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Введите правильное число: ")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("Нужно меньше")
        continue
    elif user_answer < number:
        print("Нужно больше")
        continue
    else:
        print("УРА")
        break