class main:

    def __init__(self, deck_size=40, starter=0, breaker=0, turn_player="First"):
        self.deck_size = deck_size
        self.starter = starter
        self.breaker = breaker
        self.turn_player = turn_player
    
    def Turn_Priority(self):
        starting_hand = 5
        if self.turn_player == "Second":
            starting_hand = 6
        return starting_hand
    
    def Check_Deck(self):
        if self.deck_size == 60 or self.deck_size < 60:
            return self.deck_size
        else:
            while self.deck_size
            user_input = int(input(Please Insert a valid Deck Size: ))





    

    
