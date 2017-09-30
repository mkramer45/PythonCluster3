number = input("Just Pick a Number!")
number = 0

while True:
    try:
        number = int(input("Just Pick a Number! \n"))
    except ValueError:
        print("It's Not a Number Dumbass \n")
        continue
    if number % 4 == 0:  # if the number is a multiple of 4
        print("The Number" + str(number) + "is a multiple of 4 and an even number")
    elif number % 2 == 0:  # if it is a multiple of 2 and an even number
        print("The Number" + str(number) + "is an even number")
    else:
        print(("The Number" + str(number) + "is an odd number"))
