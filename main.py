import random

players_names = ['CPU2', 'CPU']
players_symbols = ['X', 'O']
played_positions = {
    '1': " ",
    '2': " ",
    '3': " ",
    '4': " ",
    '5': " ",
    '6': " ",
    '7': " ",
    '8': " ",
    '9': " ",
}
free_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
game_over = False


def greet() -> None:
    pass

def choose_number_of_players() -> int:
    nb_players = input("Please indicate the number of players (0, 1 or 2): ")
    while nb_players not in ["0", "1", "2"]:
        print("Incorrect selection.")
        nb_players = input("Please indicate the number of players (0, 1 or 2): ")
    print(f"There will be {nb_players} player(s) in this game.")
    if int(nb_players) < 2:
        print("The other positions will be played by a computer.")
    return int(nb_players)

def change_player_name(player_id: int) -> None:
    players_names[player_id] = input(f"Please enter the name for player {player_id + 1}: ")

def make_a_move(current_player_id: int) -> None:
    chosen_position = input(f"{players_names[current_player_id]}, please choose a position in the grid above: ")
    while chosen_position not in free_positions:
        print("Incorrect selection.")
        chosen_position = input(f"{players_names[current_player_id]}, please choose a position in the grid above: ")
    played_positions[chosen_position] = players_symbols[current_player_id]
    index_of_chosen_position = free_positions.index(chosen_position)
    del free_positions[index_of_chosen_position]
    print(f"Free positions: {free_positions}")

def next_player(previous_player_index: int) -> int:
    if previous_player_index == 0:
        print("Previous player was 0, next player is 1.")
        return 1
    elif previous_player_index == 1:
        print("Previous player was 1, next player is 0.")
        return 0
    else:
        print("There was an error.")
        return 0

def main() -> None:
    current_player_id = random.choice([0, 1])

    # Greet users
    greet()

    # Choose 0, 1 or 2 players
    nb_players = choose_number_of_players()

    # Ask players' names
    for i in range(nb_players):
        change_player_name(i)
    print(f"Today's game: {players_names[1]} versus {players_names[0]}! May the true TicTacToe Master win!")

    while not game_over:
        # Draw grid
        print(played_positions)
        layout = f"""
            ╔═══╦═══╦═══╗
            ║¹{played_positions['1']} ║²{played_positions['2']} ║³{played_positions['3']} ║
            ╠═══╬═══╬═══╣
            ║⁴{played_positions['4']} ║⁵{played_positions['5']} ║⁶{played_positions['6']} ║
            ╠═══╬═══╬═══╣
            ║⁷{played_positions['7']} ║⁸{played_positions['8']} ║⁹{played_positions['9']} ║
            ╚═══╩═══╩═══╝
            """
        print(layout)
        make_a_move(current_player_id)
        # Detect win, if a player won, go to end screen

        # Detect full grid, if a grid is full, go to end screen

        temp = current_player_id
        current_player_id = next_player(temp)
        # Loop back to Draw grid

if __name__ == '__main__':
    main()
