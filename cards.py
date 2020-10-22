def main():
    pass


class Card:

    def __init__(self, rank, color):
        self.rank = rank
        self.color = color

    def get_rank(self):
        pass

    def get_color(self):
        pass

    def display(self):
        pass


class Deck:

    def __init__(self):
        # generate 16 card deck
        pass

    def shuffle(self):
        # Randomly shuffle the deck of cards
        pass

    def deal(self):
        # Return a value from the top of the deck, remove from deck
        pass

    def display(self):
        pass


class Player:

    def __init__(self):
        # Initializes a player with a way of keeping track of cards in their hand
        pass

    def add(self, card):
        pass

    def colored_card(self, color):
        pass

    def display(self):
        pass
