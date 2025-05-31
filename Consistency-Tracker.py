import os, time, random
# importing sys, sys.argv[1]

class Deck:

    def __init__(self, deck_size=40, starter=0, breaker=0, turn_player="First"):
        self.deck_size = deck_size
        self.starter = starter
        self.breaker = breaker
        self.turn_player = turn_player
    
    def get_handsize(self):
        starting_hand = 5
        if self.turn_player == "Second":
            starting_hand = 6
        return starting_hand
    
    def is_valid_deck(self):
        if self.deck_size >= 40 and self.deck_size <= 60:
            return True
        return False
    
    
    def get_conistency(self):
        if self.is_valid_deck() == True:
            one_card_prob = self.starter/self.deck_size
            return "The chances of you opening a starter from one draw is:{one_draw}".format(one_draw=one_card_prob)
        return "Please insert a valid deck size between 40-60 cards"

#Constant Variables
filenames = []

def animator(filenames, delay=0.2, repeat=5):
    #Cycles through the frames for animation
    frames = []
    for name in filenames:
        with open(name, "r", encoding="utf8") as f:
            frames.append(f.readlines())

    # Each frame is a list of rows, joins row with a "" and prints one large string
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system("cls")


print("Welcome to the simple Yu-Gi-Oh Consistency Deck Tracker! \n" "This is a program where you insert your deck size, starters, breakers and lastly your turn priority.\n" "Based on your input the output will provide your chances of opening a start on your first draw.")
user_deck = int(input("Please insert your deck size: "))
user_starters = int(input("Please insert your starter count: "))
user_breakers = int(input("Please insert your breaker count: "))
user_turn_priority = input("Please insert your turn priority: ").capitalize()

first_deck = Deck(user_deck, user_starters, user_breakers, user_turn_priority)

