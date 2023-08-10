import random

num = input("Enter a Number to guess range: ")

if num.isdigit():
    num = int(num)

    if num <= 0:
        print (" Please type a number larger than 0 next time.")
        quit()

else:
    print ("Please Type A Number Next Time")
    quit()

number = random.randint(0, num)
guesses = 0
while True:
    guesses +=1
    user_num = input("Guess a Number: ")
    if user_num.isdigit():
        user_num = int(user_num)
    else:
        print ("Please type a number next time.")
        continue

    if user_num == number:
        print ('You Got It')
        break
    else:
        if user_num > number:
            print (" you were above a number!")
        else:
            print (" you were below a number!")

print (" your total guesses is " + str (guesses))
