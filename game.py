import random
import time

class Game:
    def __init__(self):
        self.players_names = ['CPU2', 'CPU']
        self.players_type = ['CPU', 'CPU']
        self.players_symbols = ['X', 'O']
        self.played_positions = {
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
        self.free_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.game_over = False
        self.nb_players = None
        self.winner = None
        self.winning_positions = None

    def choose_number_of_players(self) -> int:
        self.nb_players = input("Please indicate the number of players (0, 1 or 2): ")
        while self.nb_players not in ["0", "1", "2"]:
            print("Incorrect selection.")
            self.nb_players = input("Please indicate the number of players (0, 1 or 2): ")
        print(f"There will be {self.nb_players} player(s) in this game.")
        if int(self.nb_players) < 2:
            print("The other positions will be played by a computer.")
        return int(self.nb_players)

    def change_player_name(self, player_id: int) -> None:
        self.players_names[player_id] = input(f"Please enter the name for player {player_id + 1}: ")
        self.players_type[player_id] = 'Human'

    def make_a_move(self, current_player_id: int) -> None:
        if self.players_type[current_player_id] == 'Human':
            chosen_position = input(
                f"{self.players_names[current_player_id]}, please choose a position in the grid above: ")
            while chosen_position not in self.free_positions:
                print("Incorrect selection.")
                chosen_position = input(
                    f"{self.players_names[current_player_id]}, please choose a position in the grid above: ")
        else:
            print(f"The computer {self.players_names[current_player_id]} is thinking ...")
            time.sleep(2)
            chosen_position = random.choice(self.free_positions)
        self.played_positions[chosen_position] = self.players_symbols[current_player_id]
        index_of_chosen_position = self.free_positions.index(chosen_position)
        del self.free_positions[index_of_chosen_position]
        #debug print(f"Free positions: {self.free_positions}")

    @staticmethod
    def next_player(previous_player_index: int) -> int:
        if previous_player_index == 0:
            #debug print("Previous player was 0, next player is 1.")
            return 1
        elif previous_player_index == 1:
            #debug print("Previous player was 1, next player is 0.")
            return 0
        else:
            print("There was an error.")
            return 0

    def greet(self) -> None:
        print("""
  _______ _                        
 |__   __(_)                       
    | |   _  ___                   
    | |  | |/ __|                  
    | |  | | (__                   
    |_|  |_|\\___|                  
         |__   __|                 
            | | __ _  ___          
            | |/ _` |/ __|         
            | | (_| | (__          
            |_|\\__,_|\\___|         
                  |__   __|        
                     | | ___   ___ 
                     | |/ _ \\ / _ \\
                     | | (_) |  __/
                     |_|\\___/ \\___|
                                   
                                   """)

    def detect_win(self) -> bool or int:
        # 123 == X
        if self.played_positions['1'] == 'X' and self.played_positions['2'] == 'X' and self.played_positions['3'] == 'X':
            self.winner = 0
            self.winning_positions = "123"
        # 456 == X
        if self.played_positions['4'] == 'X' and self.played_positions['5'] == 'X' and self.played_positions['6'] == 'X':
            self.winner = 0
            self.winning_positions = "456"
        # 789 == X
        if self.played_positions['7'] == 'X' and self.played_positions['8'] == 'X' and self.played_positions['9'] == 'X':
            self.winner = 0
            self.winning_positions = "789"
        # 147 == X
        if self.played_positions['1'] == 'X' and self.played_positions['4'] == 'X' and self.played_positions['7'] == 'X':
            self.winner = 0
            self.winning_positions = "147"
        # 258 == X
        if self.played_positions['2'] == 'X' and self.played_positions['5'] == 'X' and self.played_positions['8'] == 'X':
            self.winner = 0
            self.winning_positions = "258"
        # 369 == X
        if self.played_positions['3'] == 'X' and self.played_positions['6'] == 'X' and self.played_positions['9'] == 'X':
            self.winner = 0
            self.winning_positions = "369"
        # 159 == X
        if self.played_positions['1'] == 'X' and self.played_positions['5'] == 'X' and self.played_positions['9'] == 'X':
            self.winner = 0
            self.winning_positions = "159"
        # 357 == X
        if self.played_positions['3'] == 'X' and self.played_positions['5'] == 'X' and self.played_positions['7'] == 'X':
            self.winner = 0
            self.winning_positions = "357"
        # 123 == O
        if self.played_positions['1'] == 'O' and self.played_positions['2'] == 'O' and self.played_positions[
            '3'] == 'O':
            self.winner = 1
            self.winning_positions = "123"
        # 456 == O
        if self.played_positions['4'] == 'O' and self.played_positions['5'] == 'O' and self.played_positions[
            '6'] == 'O':
            self.winner = 1
            self.winning_positions = "456"
        # 789 == O
        if self.played_positions['7'] == 'O' and self.played_positions['8'] == 'O' and self.played_positions[
            '9'] == 'O':
            self.winner = 1
            self.winning_positions = "789"
        # 147 == O
        if self.played_positions['1'] == 'O' and self.played_positions['4'] == 'O' and self.played_positions[
            '7'] == 'O':
            self.winner = 1
            self.winning_positions = "147"
        # 258 == O
        if self.played_positions['2'] == 'O' and self.played_positions['5'] == 'O' and self.played_positions[
            '8'] == 'O':
            self.winner = 1
            self.winning_positions = "258"
        # 369 == O
        if self.played_positions['3'] == 'O' and self.played_positions['6'] == 'O' and self.played_positions[
            '9'] == 'O':
            self.winner = 1
            self.winning_positions = "369"
        # 159 == O
        if self.played_positions['1'] == 'O' and self.played_positions['5'] == 'O' and self.played_positions[
            '9'] == 'O':
            self.winner = 1
            self.winning_positions = "159"
        # 357 == O
        if self.played_positions['3'] == 'O' and self.played_positions['5'] == 'O' and self.played_positions[
            '7'] == 'O':
            self.winner = 1
            self.winning_positions = "357"

        # if winner
        if self.winner == 0 or self.winner == 1:
            self.game_over = True
            return self.winner
        else:
            return False

    def detect_full(self) -> bool:
        if not self.free_positions:
            self.game_over = True
            return True
        return False

