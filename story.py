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
    choice = input("What do you do? (pull on it/leave it)")
    if choice == "pull it":
        print("The sword comes free and as you marvel at its eerie blue glow, you hear an ear-splitting wooshing sound.")
        print("A dragon suddenly lands in front of you. It appears not to be pleased you have taken the sword.")
    elif choice == "leave it":
        print("You walk around for a while but ultimately can't find your way out of the forest.")
        return
    else:
        return
    choice = input("Thoughts racing, you realize you can either run or fight. Which do you choose? (run/fight)")
    if choice == "run":
        print("You dash in the other direction right before the dragon pounces.")
        print("The sword glows brightly as the dragon gets close with a snap of its jaws.")
    elif choice == "fight":
        print("You brandish the sword. It glows brighter as if to say it was made for this")
        print("The dragon pounces on you, engulfing you in its mouth.")
        print("But since you held the sword up, the dragon impales itself on the bright steel.")
    else:
        print("You stand still and are eaten.")


def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print("You follow the center path. The road widens and the forest thins.")


if __name__ == "__main__":
    intro()
