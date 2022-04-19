
#Úvodní text
print("Hi there!")
znak = "-"
print(znak*40)
print("I\'ve generated a random 4 digit number for you.")
print("Let\'s play a bulls and cows game.")
print(znak*40)


# Import modulu random
import random


# List čísel
def getCislo(num):
    return [int(i) for i in str(num)]


# Ověření, zda číslo není duplikované
def noDuplicate(num):
    num_li = getCislo(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


# Generování čísla
def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicate(num):
            return num


# Hlavní kód
def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getCislo(num)
    guess_li = getCislo(guess)

    for i, j in zip(num_li, guess_li):


        if j in num_li:

            # Přesná shoda
            if j == i:
                bull_cow[0] += 1

            # Shoda, ale špatná pozice
            else:
                bull_cow[1] += 1

    return bull_cow



num = generateNum()

playing = True

# Hra
try:
    while playing:
        guess = int(input("Enter your guess: "))


        if not noDuplicate(guess):
            print("Without repeating digits. Try again.")
            continue
        if guess < 1000 or guess > 9999:
            print("Four digit number only. Try again.")
            continue

        bull_cow = numOfBullsCows(num, guess)
        if bull_cow[0] != 1 and bull_cow[1] != 1:
            print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
        else:
            print(f'{bull_cow[0]} bull, {bull_cow[1]} cow')


        if bull_cow[0] == 4:
            print("You guessed right!")
            break


except(ValueError):
    print("Wrong input. Numbers only!")