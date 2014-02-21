import random

class Pattern():
    Squigly, Oval, Diamond = range(3)


class Fill():
    Solid, Shaded, Empty = range(3)


class Colour():
    Red, Green, Purple = range(3)


class Number():
    One, Two, Three = range(3)


class SetCard():
    """
    Abstraction of the set card. The set card includes a pattern, colour, fill and number of characters
    """
    def __init__(self, pattern, fill, colour, number):
        self.pattern = pattern
        self.fill = fill
        self.colour = colour
        self.number = number

    def __str__(self):
        return str(self.pattern) + str(self.fill) + str(self.colour) + str(self.number)


def generate_initial_deck():
    deck = []
    for pattern in [Pattern.Diamond, Pattern.Oval, Pattern.Squigly]:
        for fill in [Fill.Empty, Fill.Shaded, Fill.Solid]:
            for colour in [Colour.Green, Colour.Purple, Colour.Red]:
                for number in [Number.One, Number.Two, Number.Three]:
                    deck.append(SetCard(pattern, fill, colour, number))
    return deck

def attribute_is_set(c1_att, c2_att, c3_att):
    """
    Check that attribute is a set. Do this check by seeing whether :
        1. all the attributes are the same
        2. all the attributes are different
    """
    all_equals = c1_att == c2_att and c2_att == c3_att
    all_unequals = c1_att != c2_att and c2_att != c3_att and c1_att != c3_att
    return all_equals or all_unequals

class SetException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class SetTableau():
    """
    This class creates the set tableau where we actually play the game. There are a couple of things that can be done:
        1. view tableau configuration
        2. deal 3 more cards onto the tableau
        3. find and return set. Also verifies the set (so if it is not a proper set, throw exception)
        4. return how many cards are left in deck (to let player determine winning condition)
    """

    def __init__(self):
        self.deck = generate_initial_deck()
        random.shuffle(self.deck)
        self.tableau = []
        # deal 12 cards into tableau
        for i in range(12):
            self.tableau.append(self.deck.pop())

    def tableau_config(self):
        return self.tableau

    def deal_cards(self, n = 3):
        """
        Default number of cards dealt is 3. Otherwise specify for different play formats.
        """
        for i in range(n):
            self.tableau.append(self.deck.pop())
            print('add oned')

    def cards_left_in_deck(self):
        return len(self.deck)

    def get_set(self, index1, index2, index3):
        # sort the indices so they don't conflict when we pop
        set_indices = [index1, index2, index3]
        set_indices.sort()
        set_indices.reverse()

        # verify that the indices are not out of range
        for i in set_indices:
            if i > len(self.tableau):
                raise IndexError('Index for set is out of range')

        cards_in_set = [self.tableau.pop(i) for i in set_indices]
        c1 = cards_in_set.pop()
        c2 = cards_in_set.pop()
        c3 = cards_in_set.pop()

        # verify that the selected set is mutually exclusive or all the same
        is_set = True
        if not attribute_is_set(c1.pattern, c2.pattern, c3.pattern):
            is_set = False
        if not attribute_is_set(c1.fill, c2.fill, c3.fill):
            is_set = False
        if not attribute_is_set(c1.colour, c2.colour, c3.colour):
            is_set = False
        if not attribute_is_set(c1.number, c2.number, c3.number):
            is_set = False

        # if set is not correct, then add it back to set
        if not is_set:
            self.tableau.append(c1)
            self.tableau.append(c2)
            self.tableau.append(c3)
            raise SetException('User selected 3 cards which do not make a set!')

        return c1, c2, c3

# for testing purposes...
if __name__ == '__main__':
    set_tableau = SetTableau()
    for card in set_tableau.tableau_config():
        print(card)
    set = set_tableau.get_set(1,2,3)

    print
    print
    for card in set:
        print(card)

