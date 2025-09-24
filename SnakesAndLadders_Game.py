#This File contains code for Snake and Ladder game.
import random

#Positiona of snakes and ladders on the board.
snakes_pos = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders_pos = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

players_pos = [0, 0]  # Initial positions of Player 1 and Player 2

def roll_the_dice():
    return random.randint(1, 6)

def move_player(player, Number_rolled):
    current_player_pos = players_pos[player-1] + Number_rolled
    if current_player_pos > 100:
        print(f"player {player} rolled {Number_rolled} as it exceeds 100, player {player} stays at {players_pos[player-1]}" )
        return players_pos[player-1]  # Player stays in the same position if Number_rolled exceeds 100
    if current_player_pos in snakes_pos:
        print(f"Player {player} is  bitten by a snake! So, Slid down from {current_player_pos} to {snakes_pos[current_player_pos]}")
        current_player_pos = snakes_pos[current_player_pos]
    elif current_player_pos in ladders_pos:
        print(f"WoW!! player {player} has found a ladder! So, Climb up to the position {ladders_pos[current_player_pos]}")
        current_player_pos = ladders_pos[current_player_pos]
    return current_player_pos

def play_game():
    Game_Winner = None
    while not Game_Winner:
        for player in range(1,3): # Game for 2 players
            input(f"This is player{player}'s turn. press Enter to roll the dice...")
            Number_on_dice = roll_the_dice()
            print(f"player {player} has rolled a {Number_on_dice}")
            players_pos[player-1] = move_player(player, Number_on_dice)
            print(f"player {player}'s position is at {players_pos[player-1]}")

            if players_pos[player-1] == 100:
                Game_Winner = player
                break
    print(f"Congratulations!!!!! player {player} has won the game!!!!!")

play_game()
