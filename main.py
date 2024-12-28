import random
import os
from game import Game

game = Game()

def main() -> None:
    current_player_id = random.choice([0, 1])

    # Greet users
    game.greet()

    # Choose 0, 1 or 2 players
    game.nb_players = game.choose_number_of_players()

    # Ask players' names
    for i in range(game.nb_players):
        game.change_player_name(i)
    print(f"\nToday's game: {game.players_names[1]} versus {game.players_names[0]}! May the true TicTacToe Master win!")

    while not game.game_over:
        # Draw grid
        #debug print(game.played_positions)
        layout = f"""
            ╔═══╦═══╦═══╗
            ║¹{game.played_positions['1']} ║²{game.played_positions['2']} ║³{game.played_positions['3']} ║
            ╠═══╬═══╬═══╣
            ║⁴{game.played_positions['4']} ║⁵{game.played_positions['5']} ║⁶{game.played_positions['6']} ║
            ╠═══╬═══╬═══╣
            ║⁷{game.played_positions['7']} ║⁸{game.played_positions['8']} ║⁹{game.played_positions['9']} ║
            ╚═══╩═══╩═══╝
            """
        print(layout)
        game.make_a_move(current_player_id)
        # Detect win, if a player won, go to end screen
        game.detect_win()
        # Detect full grid, if a grid is full, go to end screen
        game.detect_full()

        # Next player's turn
        temp = current_player_id
        current_player_id = game.next_player(temp)
        # Loop back to Draw grid

    layout = f"""
            ╔═══╦═══╦═══╗
            ║¹{game.played_positions['1']} ║²{game.played_positions['2']} ║³{game.played_positions['3']} ║
            ╠═══╬═══╬═══╣
            ║⁴{game.played_positions['4']} ║⁵{game.played_positions['5']} ║⁶{game.played_positions['6']} ║
            ╠═══╬═══╬═══╣
            ║⁷{game.played_positions['7']} ║⁸{game.played_positions['8']} ║⁹{game.played_positions['9']} ║
            ╚═══╩═══╩═══╝
            """
    print(layout)

    #debug print(game.winner)
    if game.winner == None:
        print("Draw game!")
    else:
        #debug print(game.players_names[game.winner])
        print(f"{game.players_names[game.winner]} won with positions: {game.winning_positions}. Congratulations!")


if __name__ == '__main__':
    main()
