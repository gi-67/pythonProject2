import random

def get_position(player, position):
    snakes = {17: 7, 54: 34, 62: 19, 98: 79}
    ladders = {4: 14, 9: 31, 20: 38, 28: 84, 40: 59, 51: 67, 63: 81, 71: 91}

    if position in snakes:
        print(f"{player} landed on a snake! Moving down to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        print(f"{player} landed on a ladder! Moving up to {ladders[position]}")
        position = ladders[position]
    return position

def dice_roll(player, position):
    roll = random.randint(1,6)
    print(f"{player} rolled a {roll}")
    position += roll
    if position > 100:
        print(f"{player} rolled too high! Staying at position {position - roll}")
        position -= roll
    return get_position(player, position)


def play():
    player1 = input("Enter the name of player1: ")
    player2 = input("Enter the name of player2: ")
    player3 = input("Enter the name of player3: ")
    player4 = input("Enter the name of player4: ")
    p1_pos = p2_pos = p3_pos = p4_pos = 0
    while p1_pos < 100 and p2_pos < 100 and p3_pos <100 and p4_pos <100:
        input(f"{player1}'s turn. Press enter to roll the dice.")
        p1_pos = dice_roll(player1, p1_pos)
        print(f"{player1} is now at position {p1_pos}")
        if p1_pos >=100:
            break
        input(f"{player2}'s turn. Press enter to roll the dice.")
        p2_pos = dice_roll(player2, p2_pos)
        print(f"{player2} is now at position {p2_pos}")
        if p2_pos >=100:
            break
        input(f"{player3}'s turn. Press enter to roll the dice.")
        p3_pos = dice_roll(player3, p3_pos)
        print(f"{player3} is now at position {p3_pos}")
        if p3_pos >=100:
            break
        input(f"{player4}'s turn. Press enter to roll the dice.")
        p4_pos = dice_roll(player4, p4_pos)
        print(f"{player4} is now at position {p4_pos}")
        
    if p1_pos >=100:
        print(f"{player1} wins!")
    elif p2_pos >=100:
        print(f"{player2} wins!")
    elif p3_pos >=100:
        print(f"{player3} wins!")
    else:
        print(f"{player4} wins!")

play()