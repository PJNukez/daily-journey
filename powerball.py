import random

# step 1 - ask the players to select 5 numbers.
while True:
    print("Enter 5 different numbers from 1 - 69, with a space between each number.\n(For example: 5 7 12 23 59)")
    response = input("> ")
    number = response.split(" ")
    print(f"Your selected numbers: {number}")
    # check that the players entered 5 things.
    if len(number) != 5:
        print("error, please enter 5 numbers.")
        continue
    # convert strings into integers.
    try:
        for i in range(5):
            number[i] = int(number[i])
    except ValueError:
        print("error, please enter numbers.")
        continue
    # check that the numbers are between 1 and 69.
    between_1_69 = True
    for item in number:
        if not (1<= item <= 69):
            print("The numbers must be between 1 and 69")
            between_1_69 = False
            break
    if not between_1_69:
        continue
    # check that the numbers are unique.
    if len(set(number)) != 5:
        print("You must enter 5 different numbers")
        continue
    break

# step 2 - ask the players to select the powerball number between 1 to 26.
while True:
    print("Enter the powerball number from 1 to 26.")
    response =input("> ")
    try:
        powerball = int(response)
    except ValueError:
        print("Please enter numbers")
        continue
    if not (1<= powerball <= 26):
        print("The powerball number must be between 1 to 26.")
        continue
    break

#  step 3 - ask the players to select the number of times they want to play.
while True:
    print("How many times do you want to play? (Max: 100)?\n2$ per time.")
    response = input("> ")
    # convert a string to an integer.
    try:
        numPlays = int(response)
    except ValueError:
        print("Error, please enter a number (ex.10, 25 or 100).")
        continue
    # check that the number is between 1 - 100.
    if not (1<= numPlays <= 100):
        print("Number of times must be between 1 to 100.")
        continue
    break

# step 4 - run the simulation.
# calculate price.
price = "$" + str(2 * numPlays)
print(f"It's cost {price} to plays {numPlays} times.")
# loop playtimes
for i in range(numPlays):
    possibleNumber = list(range(1, 70))
    # shuffle numbers in possibleNumber list.
    random.shuffle(possibleNumber)
    winningNumber = possibleNumber[0:5]
    winningPowerball = random.randint(1, 26)
    # display winning numbers
    print("The winning numbers are: ", end="")
    allwiningNumber =""
    for num in winningNumber:
        allwiningNumber += str(num) + " "
    allwiningNumber += "and " + str(winningPowerball)
    print(allwiningNumber, end="")

    # check for winner.
    if (set(number) == set(winningNumber) and powerball == winningPowerball):
        print(" (You win!)")
        break
    else:
        print(" (You lose!)")

print(f"You have wasted {price}.\nThanks for playing!")
print("test github")
print("confirm updating powerball")