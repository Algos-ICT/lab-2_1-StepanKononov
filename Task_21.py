import sys

sys.stdin = open('INPUT.TXT')
sys.stdout = open('OUTPUT1.TXT', 'w')
n, m, trump = input().split()
card_values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
all_close = True

def scan_input():
    cads = input().split()
    temp_dict = dict()
    for card in cads:
        value = int(convert_value(card[0]))
        suit = card[1]
        if suit not in temp_dict:
            temp_dict[suit] = [value]
        else:
            temp_dict[suit].append(value)
    return temp_dict


def convert_value(val):
    if val in card_values:
        return card_values[val]
    return int(val)


def sort_cards(array):
    for elem in array:
        array[elem] = sorted(array[elem])


player_hand = scan_input()
opponent_hand = scan_input()
import sys

sys.stdin = open('INPUT.TXT')
sys.stdout = open('OUTPUT.TXT', 'w')
n, m, trump = input().split()
card_values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
all_close = True

def scan_input():
    cads = input().split()
    temp_dict = dict()
    for card in cads:
        value = int(convert_value(card[0]))
        suit = card[1]
        if suit not in temp_dict:
            temp_dict[suit] = [value]
        else:
            temp_dict[suit].append(value)
    return temp_dict


def convert_value(val):
    if val in card_values:
        return card_values[val]
    return int(val)


def sort_cards(array):
    for elem in array:
        array[elem] = sorted(array[elem])


player_hand = scan_input()
opponent_hand = scan_input()

sort_cards(player_hand)
sort_cards(opponent_hand)

for cur_card_suit in opponent_hand:
    if cur_card_suit not in player_hand:
        if trump in player_hand:
            while opponent_hand[cur_card_suit] and player_hand[trump]:
                opponent_hand[cur_card_suit].pop(0)
                player_hand[trump].pop(0)
        continue
    op_index = 0
    while op_index < len(opponent_hand[cur_card_suit]) and player_hand[cur_card_suit] and cur_card_suit != trump:
        op_card_value = opponent_hand[cur_card_suit][0]
        index = 0
        while index < (len(player_hand[cur_card_suit])-1) and player_hand[cur_card_suit][index] <= op_card_value:
            index += 1
        if player_hand[cur_card_suit][index] > op_card_value:
            player_hand[cur_card_suit].pop(index)
            opponent_hand[cur_card_suit].pop(0)
            op_index = 0
        elif trump in player_hand and player_hand[trump]:
            player_hand[trump].pop(0)
            opponent_hand[cur_card_suit].pop(0)
            op_index = 0
        op_index += 1

    op_index = 0
    while cur_card_suit == trump and   op_index < len(opponent_hand[trump]) and trump in player_hand and len(player_hand[trump]) > 0:
        op_card_value = opponent_hand[trump][0]
        index = 0
        while index < (len(player_hand[trump]) - 1) and player_hand[trump][index] <= op_card_value:
            index += 1
        if player_hand[trump][index] > op_card_value:
            player_hand[trump].pop(index)
            opponent_hand[trump].pop(0)
            op_index = 0
        op_index += 1

flag = True
for cur_card_suit in opponent_hand:
    if len(opponent_hand[cur_card_suit]) > 0:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
sys.stdout.close()
