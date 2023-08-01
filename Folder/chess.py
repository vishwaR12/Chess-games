chessboard = {
    "a8": "B_R", "b8": "B_N", "c8": "B_B", "d8": "B_Q", "e8": "B_K", "f8": "B_B", "g8": "B_N", "h8": "B_R",
    "a7": "B_P", "b7": "B_P", "c7": "B_P", "d7": "B_P", "e7": "B_P", "f7": "B_P", "g7": "B_P", "h7": "B_P",
    "a6": "",    "b6": "",    "c6": "",    "d6": "",    "e6": "",    "f6": "",    "g6": "",    "h6": "",
    "a5": "",    "b5": "",    "c5": "",    "d5": "",    "e5": "",    "f5": "",    "g5": "",    "h5": "",
    "a4": "",    "b4": "",    "c4": "",    "d4": "",    "e4": "",    "f4": "",    "g4": "",    "h4": "",
    "a3": "",    "b3": "",    "c3": "",    "d3": "",    "e3": "",    "f3": "",    "g3": "",    "h3": "",
    "a2": "W_P", "b2": "W_P", "c2": "W_P", "d2": "W_P", "e2": "W_P", "f2": "W_P", "g2": "W_P", "h2": "W_P",
    "a1": "W_R", "b1": "W_N", "c1": "W_B", "d1": "W_Q", "e1": "W_K", "f1": "W_B", "g1": "W_N", "h1": "W_R",
}

def get_row_col(position):
    col = position[0]
    row = int(position[1:])
    return row, col

def is_valid_position(position):
    row, col = get_row_col(position)
    return 1 <= row <= 8 and 'a' <= col <= 'h'

def is_empty(position):
    return chessboard.get(position) is None or chessboard[position] == ""

def is_opponent_coin(position, player):
    if player == "W":
        return chessboard.get(position, "").startswith("B")
    elif player == "B":
        return chessboard.get(position, "").startswith("W")
    return False

def print_board():
    print("\n   a   b   c   d   e   f   g  h")
    for row in range(8, 0, -1):
        line = f"{row} "
        for col in "abcdefgh":
            line += chessboard.get(col + str(row), "").ljust(2) + " "
        print(line)

def get_possible_moves(position, player):
    coin_type = chessboard[position][2:]
    row, col = get_row_col(position)
    possible_moves = []

    if coin_type == "R":
        # Add horizontal moves
        for i in range(ord(col)+1, ord('h')+1):
            move = chr(i) + str(row)
            if is_valid_position(move):
                if is_empty(move):
                    possible_moves.append(move)
                elif is_opponent_coin(move, player):
                    possible_moves.append(move)
                    break
                else:
                    break

        for i in range(ord(col)-1, ord('a')-1, -1):
            move = chr(i) + str(row)
            if is_valid_position(move):
                if is_empty(move):
                    possible_moves.append(move)
                elif is_opponent_coin(move, player):
                    possible_moves.append(move)
                    break
                else:
                    break

        # Add vertical moves for Rook
        for i in range(row+1, 9):
            move = col + str(i)
            if is_valid_position(move):
                if is_empty(move):
                    possible_moves.append(move)
                elif is_opponent_coin(move, player):
                    possible_moves.append(move)
                    break
                else:
                    break

        for i in range(row-1, 0, -1):
            move = col + str(i)
            if is_valid_position(move):
                if is_empty(move):
                    possible_moves.append(move)
                elif is_opponent_coin(move, player):
                    possible_moves.append(move)
                    break
                else:
                    break

    elif coin_type == "N":
        # Knight moves
        knight_moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        for dx, dy in knight_moves:
            move = chr(ord(col) + dx) + str(row + dy)
            if is_valid_position(move) and (is_empty(move) or is_opponent_coin(move, player)):
                possible_moves.append(move)

    elif coin_type == "B":
        # Add diagonal moves for Bishop
        for i in range(1, 9):
            move = chr(ord(col)+i) + str(row+i)
            if is_valid_position(move):
                if is_empty(move):
                    possible_moves.append(move)
                elif is_opponent_coin(move, player):
                    possible_moves.append(move)
                    break
                else:
                    break

        for i in range(1, 9):
            move = chr(ord(col)+i) + str(row-i)
            if is_valid_position(move):
                if is_empty(move):
                    possible_moves.append(move)
                elif is_opponent_coin(move, player):
                    possible_moves.append(move)
                    break
                else:
                    break

        for i in range(1, 9):
            move = chr(ord(col)-i) + str(row+i)
            if is_valid_position(move):
                if is_empty(move):
                    possible_moves.append(move)
                elif is_opponent_coin(move, player):
                    possible_moves.append(move)
                    break
                else:
                    break

        for i in range(1, 9):
            move = chr(ord(col)-i) + str(row-i)
            if is_valid_position(move):
                if is_empty(move):
                    possible_moves.append(move)
                elif is_opponent_coin(move, player):
                    possible_moves.append(move)
                    break
                else:
                    break

    elif coin_type == "Q":
        # Add Queen moves (combining Rook and Bishop moves)
        possible_moves = get_possible_moves(position, player, "R") + get_possible_moves(position, player, "B")

    elif coin_type == "K":
        # King moves
        king_moves = [
            (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)
        ]
        for dx, dy in king_moves:
            move = chr(ord(col) + dx) + str(row + dy)
            if is_valid_position(move) and (is_empty(move) or is_opponent_coin(move, player)):
                possible_moves.append(move)

    elif coin_type == "P":
        # Pawn moves
        if player == "W":
            # Pawn moves for white
            move1 = col + str(row + 1)
            move2 = col + str(row + 2) if row == 2 and is_empty(col + str(row + 1)) and is_empty(col + str(row + 2)) else None
            capture1 = chr(ord(col) - 1) + str(row + 1)
            capture2 = chr(ord(col) + 1) + str(row + 1)
        else:
            # Pawn moves for black
            move1 = col + str(row - 1)
            move2 = col + str(row - 2) if row == 7 and is_empty(col + str(row - 1)) and is_empty(col + str(row - 2)) else None
            capture1 = chr(ord(col) - 1) + str(row - 1)
            capture2 = chr(ord(col) + 1) + str(row - 1)

        if is_valid_position(move1) and is_empty(move1):
            possible_moves.append(move1)
        if move2 and is_valid_position(move2) and is_empty(move2):
            possible_moves.append(move2)
        if is_valid_position(capture1) and is_opponent_coin(capture1, player):
            possible_moves.append(capture1)
        if is_valid_position(capture2) and is_opponent_coin(capture2, player):
            possible_moves.append(capture2)

    return possible_moves

def record_move(player, coin_type, from_position, to_position):
    with open("Steps_record.txt", "a") as f:
        f.write(f"{player} {coin_type} at {from_position} has been moved to {to_position}\n")

def is_checkmate(player):
    for position in chessboard:
        if chessboard.get(position, "").startswith(player):
            possible_moves = get_possible_moves(position, player)
            if possible_moves:
                return False
    return True

def play_chess_game():
    current_player = "W"

    while True:
        print_board()

      
        chosen_position = input(f"\nPlayer {current_player}: Choose a coin (e.g., b1): ")

        if chosen_position.lower() == "exit":
            print("Exiting the game.")
            break
        elif chosen_position.lower() == "print":
            continue

        if is_valid_position(chosen_position) and chessboard.get(chosen_position, "").startswith(current_player):
            coin_type = chessboard[chosen_position]
            possible_moves = get_possible_moves(chosen_position, current_player)
            print(f"\nThe current coin is {coin_type}.")
            print(f"The next set of positions the {coin_type} will be able to move: {possible_moves}")

            # Get user input for the new position to move the coin
            new_position = input("Enter the new position to move the coin: ")

            # Check if the new position is valid and move the coin if it's a valid move
            if is_valid_position(new_position):
                if new_position in possible_moves:
                    record_move(current_player, coin_type, chosen_position, new_position)
                    if not is_empty(new_position) and is_opponent_coin(new_position, current_player):
                        print(f"{coin_type} captured {chessboard[new_position]} at {new_position}.")
                    chessboard[new_position] = chessboard[chosen_position]
                    chessboard[chosen_position] = ""
                    print(f"{coin_type} moved to {new_position}.")
                    if is_checkmate("W"):
                        print("Checkmate! Player B wins!") # Update this for player names if needed
                        break
                    elif is_checkmate("B"):
                        print("Checkmate! Player W wins!") # Update this for player names if needed
                        break
                    current_player = "B" if current_player == "W" else "W"
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid position. Try again.")
        else:
            print("Invalid choice. Try again.")


play_chess_game()

