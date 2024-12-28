class Game:
    def __init__(self):
        self.players_names = ['CPU2', 'CPU']
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

    def make_a_move(self, current_player_id: int) -> None:
        chosen_position = input(
            f"{self.players_names[current_player_id]}, please choose a position in the grid above: ")
        while chosen_position not in self.free_positions:
            print("Incorrect selection.")
            chosen_position = input(
                f"{self.players_names[current_player_id]}, please choose a position in the grid above: ")
        self.played_positions[chosen_position] = self.players_symbols[current_player_id]
        index_of_chosen_position = self.free_positions.index(chosen_position)
        del self.free_positions[index_of_chosen_position]
        print(f"Free positions: {self.free_positions}")

    @staticmethod
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

    def greet(self) -> None:
        pass