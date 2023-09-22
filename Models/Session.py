class Session:
    def __init__(self, id, userid):
        self.id = id
        self.userid = userid
        self.games = {1: "rock, paper, scissors", 2: "second game"}
        self.game = None

    def start_game(self):
        print("Welcome to the game!")
        print(self.games)
        
        while True:
            try:
                gamechoice = int(input("Choose a game (1 for Rock, Paper, Scissors, 2 for Second Game): "))
                if gamechoice in self.games:
                    self.game = self.games[gamechoice]
                    print(f"You selected: {self.game}")
                    break
                else:
                    print("Invalid choice. Please choose 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")
