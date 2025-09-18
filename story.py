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
    


def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print("You follow the center path. The road widens and the forest thins.")


if __name__ == "__main__":
    intro()
