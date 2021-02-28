"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck

class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_straightflush(self):
        def recur_straight(t, n):
            '''
            t : list
            n : length of straight number
            '''
            t = list(t)
            t.sort()
            if len(t) < n:
                return False
            elif t[n-1] - t[0] == n-1:
                return True
            else:
                return recur_straight(t[1:], n)

        if not self.has_flush():
            return False
        else:
            self.cards_by_suits={}
            for card in self.cards:
                self.cards_by_suits[card.suit] = self.cards_by_suits.get(card.suit, [card]) + [card]

            for cards in self.cards_by_suits.values():
                if len(cards) >= 5:
                    recur_straight(cards, 5)
            return False

            
    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
    
    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_twopair(self):
        self.rank_hist()
        twopair_key = []
        for val in self.ranks.values():
            if val >= 2:
                twopair_key += [val]
        if len(twopair_key) >= 2:
            return True
        else:
            return False
    
    def has_fullhouse(self):
        self.rank_hist()
        twomore_key = []
        for val in self.ranks.values():
            if val >= 2:
                twomore_key += [val]
        two = 2
        three = 3
        if two in twomore_key and three in twomore_key:
            return True
        else: 
            return False

    

    def has_three_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
    
    def has_straight(self):
        def recur_straight(t, n):
            '''
            t : list
            n : length of straight number
            '''
            t = list(t)
            t.sort()
            if len(t) < n:
                return False
            elif t[n-1] - t[0] == n-1:
                return True
            else:
                return recur_straight(t[1:], n)
        
        self.rank_hist()
        rank_list = self.ranks.keys()
        n = 5
        return recur_straight(rank_list, n)


    def has_four_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

        







if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        #print(hand.has_flush())
        #print(hand.has_pair())
        #print(hand.has_twopair())
        print(hand.has_straight())
        print('')



