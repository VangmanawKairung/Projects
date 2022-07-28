# Tic-tac-toe 
# X is the sign for player or player one
# O is the sign for computer or player two

import random

# Display the board
# The parameter is the list of positions in the current turn
def print_position (position_list):
    '''  1 | 2 | 3
        ---|---|---
         4 | 5 | 6
        ---|---|---
         7 | 8 | 9  '''
    print("\n %s | %s | %s\n---|---|---\n %s | %s | %s\n---|---|---\n %s | %s | %s\n" %(
            position_list[0], position_list[1], position_list[2],
            position_list[3], position_list[4], position_list[5],
            position_list[6], position_list[7], position_list[8] ))

# Check the win status
def is_win (position_list):
    # Sorting the member in the list of positions
    position_list.sort()

    # List of positions to win
    win_postion = [ [1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9], 
                    [1, 4, 7], 
                    [2, 5, 8], 
                    [3, 6, 9], 
                    [1, 5, 9],
                    [3, 5, 7]]
    
    # Compare the position_list (parameter) with the win positions
    # Go into each list in win positions list
    for list in win_postion:
        # Set the count variable to 0, it uses to count the similar members
        count = 0 

        # Go into each member in the list
        for member in list:
            # Is member equal to the member in position_list
            if member in position_list:
                count += 1
        
        # The player (or computer) wins if the members of both lists are the same as 3 elements
        if (count == 3):
            # If win, the function will return True
            return True
            break
    
    # If not win, the function will return False
    return False

# Function for the last free position
def last_turn(game_position, playyer_position):
    # Set count variable to 0, it uses as the index of the list
    count = 0
    for position in game_position:
        count += 1
        # Is that position still aviable
        if (position != 'X' and position != 'O'):
            # Set that position as X
            game_position[count - 1] = 'X'
            # Display the current board
            print_position(game_position)
            # Stop the loop
            break
    # The function return the position as count
    return count

# Function for one player
def one_player ():
    # The aviable positions
    position = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Store the position that the player chose
    player_position = []

    # Store the position that the computer chose
    computer_position = []

    # The win status of player and computer
    player_win = False
    computer_win = False

    # Count the loop
    count_loop = 0

    while (player_win == False or computer_win == False):
        # The number of loop increases by 1
        count_loop += 1

        # Display the current board
        print_position(position)

        # Player turn
        # Enter the number of position
        number = int(input('Enter the position number: '))

        # Add the chosen position to the player_position list
        player_position.append(number)

        # Change the position number into X
        position[number - 1] = 'X'

        # Check the win status of player by using is_win funtion
        # The argument is player_position
        if is_win(player_position):
            print_position(position)
            # Tell the player that you win
            print("You win!")
            # The player status is True
            player_win = True
            # Out of while loop
            break

        # Computer turn
        # The computer chooses the position by using random from 1 to 9
        computer_number = random.randint(1, 9)

        while (1):
            # If the computer chosen position is the same as player chosen positions
            if (computer_number in player_position) or (computer_number in computer_position):
                # The computer will random the position number again
                computer_number = random.randint(1, 9)
            # If the computer chosen position is not the same as player chosen positions
            else:
                # Set the position as O
                position[computer_number - 1] = 'O'
                # Add the computer chosen position to the computer position list
                computer_position.append(computer_number)
                break
        
        # Check the win status of computer
        if is_win(computer_position):
            print_position(position)
            # If the computer wins, the player is lost
            print("You lose!")
            # The computer win status becomes True
            computer_win = True
            break
            
        # At the last available position
        # This is the turn for the player because the player starts first
        if count_loop == 4:
            # Find the avaible position by last_turn function
            player_position.append(last_turn(position, player_position))
            # Check the win status of player
            if (is_win(player_position)):
                print("You win")
            else:
                print("No one win!")
            player_win = True
            computer_win = True
            break

# Function for two players
def two_player():
    position = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Player one chosen positions list
    player_one_position = []

    # Player two chosen positions List
    player_two_position = []

    # Player one and Player two win status
    player_one_win = False
    player_two_win = False

    count_loop = 0
    
    while (player_one_win == False or player_two_win == False):
        count_loop += 1

        print_position(position)

        # Player one turn
        # Palyer one select the position
        player_one_number = int(input("Player 1: "))

        # Add the selected position to the player one positions list
        player_one_position.append(player_one_number)

        # Change selected position into X
        position[player_one_number - 1] = 'X'

        # Check the win status of player one
        # If the player one wins
        if is_win(player_one_position):
            print_position(position)
            print("Player ONE win!")
            player_one_win = True
            break
        
        print_position(position)

        # Player two turn
        # Player two selects the position
        player_two_number = int(input("Player 2: "))

        # Add the selected position to player two positions list
        player_two_position.append(player_two_number)

        # Change the selected postion number into O
        position[player_two_number - 1] = 'O'

        # Check the player two win status
        # If the player two wins
        if is_win(player_two_position):
            print_position(position)
            print("Playyr TWO win!")
            player_two_win = True
            break
        
        # At the last avaible position
        # This is the turn of the player one because the player one starts first
        if count_loop == 4:
            player_one_position.append(last_turn(position, player_one_position))
            if (is_win(player_one_position)):
                print("Player ONE win")
            else:
                print("No one win!")
            player_one_win = True
            player_two_win = True
            break


# Select the mode
print("One player => 1")
print("Two player => 2")
# Initial the mode value (any number except 0)
mode = 1
while mode != 0:
    mode = int(input("Enter mode (0 to end): "))
    while (mode < 0 or mode > 2):
        mode = int(input("Enter the mode (0 to end): "))
    if mode == 1:
        one_player()
    elif mode == 2:
        two_player()
        
print("Game Over")

