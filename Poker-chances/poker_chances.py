# -*- coding: utf-8 -*-

import itertools
from copy import deepcopy

# hearts, clubs, spades, diamonds
SUITS = ['H', 'C', 'S', 'D']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
DECK = [(s, v) for s in SUITS for v in VALUES]


def generate_setup():
    # helper function for generating test cases
    from random import sample
    deck = deepcopy(DECK)
    player1_hand = sample(deck, 2)
    for card in player1_hand:
        deck.remove(card)
    player2_hand = sample(deck, 2)
    for card in player2_hand:
        deck.remove(card)
    flop = sample(deck, 3)
    for card in flop:
        deck.remove(card)
    turn = sample(deck, 1)
    for card in turn:
        deck.remove(card)

    return player1_hand, player2_hand, flop, turn


def is_royal_flush(hand):
    if hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0]:
        lst = [10,11,12,13,14]
        list_ = [True for i in range(len(hand)) if hand[i][1] in lst]
        if len(list_) == len(lst):
            return True, (max([i[1] for i in hand]),)
    return False, None
    


#print(is_royal_flush([('S', 10), ('S', 11), ('S', 12), ('S',13) ,('S',14)]))


def is_straight_flush(hand):
    if hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0]:
        lst = [hand[i][1] for i in range(len(hand))]
        if min(lst) <= 10:
            lst_ex = [i for i in range(min(lst),min(lst)+5)]
            list_of_elem = [[i for i in lst if i == a]for a in lst_ex]
            list_idk = [len(i) for i in list_of_elem]
            if max(list_idk) == 1 and min(list_idk) == 1:

                return True, (max([i[1] for i in hand]),)
        return False, None
    return False, None

#print(is_straight_flush([('S', 9), ('S', 10), ('S', 11), ('S',12) ,('S',13)]))

def is_four_of_a_kind(hand):
    lst = [hand[i][1] for i in range(len(hand))]
    list_of_true = [[i for i in lst if i == a]for a in lst]
    list_of_len = [len(i) for i in [[True for i in lst if i == a]for a in lst]]
    list_ = [i for i in list_of_true if len(i) == 4]
    if max(list_of_len) == 4:
        return True, (list_[1][1],)
    return False, None

#print(is_four_of_a_kind([('S', 9), ('S', 9), ('S', 1), ('S',9) ,('S',9)]))

def is_full_house(hand):
    lst = [hand[i][1] for i in range(len(hand))]
    list_of_elem = [[i for i in lst if i == a]for a in lst]
    list_of_trio = [i for i in list_of_elem if len(i) == 3]
    list_of_duo = [i for i in list_of_elem if len(i) == 2]
    if len(list_of_trio) == 3 and len(list_of_duo) == 2:
        return True, (list_of_trio[1][1],list_of_duo[1][1])
    return False, None    

#print(is_full_house([('S', 2), ('S', 2), ('S', 9), ('S',9) ,('S',9)]))

def is_flush(hand):
    if hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0]:
        return True, (max([i[1] for i in hand]),)

    return False, None

#print(is_flush([('S', 2), ('S', 2), ('S', 9), ('S',9) ,('S',9)]))

def is_straight(hand):
    lst = [hand[i][1] for i in range(len(hand))]
    if min(lst) <= 10:
        lst_ex = [i for i in range(min(lst),min(lst)+5)]
        list_of_elem = [[i for i in lst if i == a]for a in lst_ex]
        list_idk = [len(i) for i in list_of_elem]
        if max(list_idk) == 1 and min(list_idk) == 1:

            #print(list_idk)
            #print(list_of_elem)
            return True, (max([i[1] for i in hand]),)
    return False, None

#print(is_straight([('S', 9), ('D', 12), ('H', 8), ('H', 11), ('C', 2)]))

def is_three_of_a_kind(hand):
    lst = [hand[i][1] for i in range(len(hand))]
    list_of_true = [[i for i in lst if i == a]for a in lst]
    list_of_len = [len(i) for i in [[True for i in lst if i == a]for a in lst]]
    list_ = [i for i in list_of_true if len(i) == 3]
    if max(list_of_len) == 3:
        return True, (list_[1][1],)
    return False, None

#print(is_three_of_a_kind([('S', 12), ('D', 12), ('H', 2), ('H', 5), ('C', 2)]))

def is_two_pairs(hand):
    lst = [hand[i][1] for i in range(len(hand))]
    list_of_duo = [i for i in [[x for x in lst if x == a]for a in lst] if len(i) == 2]
    list_idk = [i[1] for i in list_of_duo]
    if len(list_idk) == 4:
        return True, (max(list_idk),min(list_idk))
    return False, None

#print(is_two_pairs([('S', 2), ('D', 11), ('H', 2), ('H', 2), ('C', 2)]))


def is_pair(hand):
    lst = [hand[i][1] for i in range(len(hand))]
    list_of_duo = [i for i in [[x for x in lst if x == a]for a in lst] if len(i) == 2]
    list_idk = [i[1] for i in list_of_duo]
    if len(list_idk) == 2:
        return True, (list_idk[1],)
    return False, None

#print(is_pair([('S', 2), ('D', 11), ('H', 2), ('H', 3), ('C', 8)]))

def evaluate_hand(hand):
    res = is_royal_flush(hand)
    if res[0]:
        return 9, res[1]

    res = is_straight_flush(hand)
    if res[0]:
        return 8, res[1]

    res = is_four_of_a_kind(hand)
    if res[0]:
        return 7, res[1]

    res = is_full_house(hand)
    if res[0]:
        return 6, res[1]

    res = is_flush(hand)
    if res[0]:
        return 5, res[1]

    res = is_straight(hand)
    if res[0]:
        return 4, res[1]

    res = is_three_of_a_kind(hand)
    if res[0]:
        return 3, res[1]

    res = is_two_pairs(hand)
    if res[0]:
        return 2, res[1]

    res = is_pair(hand)
    if res[0]:
        return 1, res[1]

    return 0, None

#print(evaluate_hand([('S', 10), ('S', 11), ('S', 12), ('S',13) ,('S',14)]))

def compare_highest_card(hand_1, hand_2): # 
    def sort(lst): 
        for repeater in range(len(lst)):
            for index in range(len(lst)-1):
                if lst[index] < lst[index+1]:
                    lst[index],lst[index+1]=lst[index+1],lst[index]
        return lst

    lst_1 = sort([hand_1[i][1] for i in range(len(hand_1))])
    lst_2 = sort([hand_2[i][1] for i in range(len(hand_2))])

    for i in range(5):
        if lst_1[i] != lst_2[i]:
            #print(lst_1[i],lst_2[i])
            if lst_1[i] > lst_2[i]:
                return hand_1
            elif lst_1[i] < lst_2[i]:
                return hand_2
    return None

#print(compare_highest_card([('S', 10), ('S', 14), ('S', 12), ('S',13) ,('S',13)],[('S', 10), ('S', 10), ('S', 12), ('S',13) ,('S',13)]))

def get_all_combinations(hand, flop, turn, river):
    cards = hand + flop + turn + river 
    lst = list()
    for e in range(0, len(cards)+1):
        for i in itertools.combinations(cards, e):
            if len(i) == 5:
                lst.append(i)
    return lst

#print(get_all_combinations([('D', 9), ('S', 6)], [('C', 7), ('D', 14)], [('D', 4), ('D', 3)], [('S', 9)]))


def find_better(hand_1, hand_2): 
    if evaluate_hand(hand_1) > evaluate_hand(hand_2):
        return hand_1
    elif evaluate_hand(hand_1) < evaluate_hand(hand_2):
        return hand_2
    else:
        return compare_highest_card(hand_1,hand_2)
    return None

#print(find_better([('S', 10), ('S', 11), ('S', 12), ('S',13) ,('S',14)],[('S', 10), ('S', 11), ('S', 12), ('S',13) ,('S',14)]))
    
def select_best(hand, flop, turn, river): # p
    lst = get_all_combinations(hand,flop,turn,river)
    best = lst[0]
    for i in range(1,len(lst)):
        if find_better(best,lst[i]) != None:            
            best = find_better(best,lst[i])                
    return list(best)

#print(select_best([('D', 9), ('S', 6)], [('C', 7), ('D', 14)], [('D', 4), ('D', 3)], [('S', 9)]))
#[('D', 9), ('S', 6), ('C', 7), ('D', 14), ('S', 9)]

def calculate_chances(player1_hand, player2_hand, flop, turn): # 
    lst_of_use = player1_hand + player2_hand + flop + turn
    lst_suits = ['H','C','S','D']
    lst_of = []
    for suit in lst_suits:                              
        for num in range(2,15):
            lst = []
            lst.append(str(suit))
            lst.append(int(num))
            if tuple(lst) not in lst_of_use:
                lst_of.append(tuple(lst))

    player_1 = 0
    player_2 = 0
    draw = 0    

    for river in lst_of:
        lst_help = [river]
        p1 = select_best(player1_hand,flop,turn,lst_help)
        p2 = select_best(player2_hand,flop,turn,lst_help)
        if find_better(p1,p2) == p1:
            player_1 += 1
        elif find_better(p1,p2) == p2:
            player_2 += 1
        elif find_better(p1,p2) == None:
            draw += 1        
    
    return player_1/44, player_2/44,draw/44


if __name__ == '__main__':
    player1_hand, player2_hand, flop, turn = generate_setup()

    print("PLAYER 1:", player1_hand)
    print("PLAYER 2:", player2_hand)
    print("FLOP:", flop)
    print("TURN:", turn)

    p1_win, p2_win, draw = calculate_chances(
        player1_hand, player2_hand, flop, turn)

    print("PLAYER 1 has a {} chance of winning".format(p1_win))
    print("PLAYER 2 has a {} chance of winning".format(p2_win))
    print('There\'s a {} chance of a draw'.format(draw))

