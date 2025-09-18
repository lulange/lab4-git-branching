def intro():
    print("You wake up in a dark forest. You can go left or right or down a center path.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("He says that you have just stomped all over his friend's home.")
    print("You can either apologize or duel the squirrel.")
    choice = input("which do you choose? (fight/say sorry)")
    if choice == "fight":
        print("You accept the squirel's duel")
        print("The squirrel produces a small sword from behind a log.")
        print("You draw your daggers.")
        print("Before the duel can properly begin, you quickly throw a dagger, shaving off a whisker from the squirrel's face.")
        print("The squirrel runs away in fright.")
        stomp = input("You are now free to stomp all over and make sure to crush the squirrel's friend's home. (stomp/leave)")
        if stomp == "stomp":
            print("You ruthlessly stomp all over.")
        elif stomp == "leave":
            print("You walk away glad you didn't get scratched up.")
        else:
            return
    elif choice == "say sorry":
        print("You apologize and the squirrel realizes you meant nothing by it.")
    else:
        print("The squirrel throws a nut at your head at struts away.")


def center_path():
    print("You follow the center path. The road widens and the forest thins.")


if __name__ == "__main__":
    intro()
