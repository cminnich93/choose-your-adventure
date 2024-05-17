name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are at the beach, you can't swim but you can go left or right on the shore. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You get to a shopping center, you can go in one of the stores or continue walking. Type shop to shop at the stores and walk to keep walking: ")

    if answer == "shop":
        print("You have spent all your money.")
    elif answer == "walk":
        print("You walked for many miles and ran out of water. Maybe you should've gotten some at a store!")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input(
        "You get to a cave. It looks dark, but you hear music inside. Do you go in?")
    
    if answer == "yes":
        print("You find an awesome party with a killer DJ and a light show!")
    elif answer == "no":
        answer = input(
        "A mysterious stranger approaches you on the beach. Do you talk to them?")

    if answer == "yes":
        print("You talk to the stranger and they give you a golden ticket. You win!")
    elif answer == "no":
        print("You ignore the stranger. They call the cops. You lose!")

else: 
    print("Not a valid option. You lose")

print("Thank you for trying", name)
