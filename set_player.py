from set_tableau import SetTableau, SetException, attribute_is_set

def play_manual():
    """
    This allows user to play by inputting the sets
    """
    tableau = SetTableau()

    while tableau.cards_left_in_deck() > 0:
        # print the tableau
        for i in range(len(tableau.tableau)):
            print(str(i) + ". " + str(tableau.tableau[i]))

        # check to see if user is dealing
        input = raw_input('\nInput indices separated by commas or "d" to deal: ').rstrip()
        while input != 'd' and len(input.split(',')) != 3:
            input = raw_input("input not recognized, please type 'd' or indices separated by comma's : ").rstrip()

        if input == 'd':
            tableau.deal_cards()
        elif len(input.split(',')) == 3:
            i1, i2, i3 = input.split(',')
            try:
                tableau.get_set(int(i1), int(i2), int(i3))
            except SetException:
                print('Does not make a set, please try again!')

if __name__ == '__main__':
    play_manual()
