print("Welcome to Treasure Island. Your mission is to find the treasure.")
left_or_right = input("left or right? ")

if left_or_right.lower().strip() == "left":
    swim_or_wait = input("swim or wait ")
    if swim_or_wait.lower().strip() == "wait":
        door = input("Which Door? Red <or> Blue <or> Yellow ")
        if door.lower().strip() == "yellow":
            print("You Win!🎉")
            print("Here is your treasure 💰💰💰💰💰💰💰💰")
        elif door.lower().strip() == "red":
            print("Burned by fire. Game Over 🔥")
        elif door.lower().strip() == "blue":
            print("Eaten by Beasts. Game Over ☠️")
        else:
            print("Game Over! 🙃")
    else:
        print("Attacked by trout. Game Over 🌊")
else:
    print("Fall into a hole. Game Over 🤸‍♀️")