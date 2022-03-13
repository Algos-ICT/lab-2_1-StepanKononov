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

sort_cards(player_hand)
sort_cards(player_hand)

for card_s in opponent_hand:
    if card_s == trump or card_s not in player_hand:
        continue
    while opponent_hand[card_s] and all_close:
        cur_card = opponent_hand[card_s].pop(0)
        index = 0
        while index < len(player_hand[card_s]) and player_hand[card_s][index] < cur_card:
            index += 1
        if index < len(player_hand[card_s]) and player_hand[card_s][index] > cur_card :
            player_hand[card_s].pop(index)
        elif trump in player_hand and player_hand[trump]:
            player_hand[trump].pop(0)
        else:
            all_close = False
            print("NO")
            break
if all_close and trump in opponent_hand:
    while opponent_hand[trump] and all_close:
        value = opponent_hand[trump].pop(0)
        index = 0
        while index < len(player_hand[trump]) and player_hand[trump][index] < value:
            index += 1
        if trump in player_hand and player_hand[trump] and player_hand[trump][0] > value:
            player_hand[trump].pop(0)
        else:
            all_close = False
            print("NO")
            break

if len(player_hand) == 0 and all_close:
    print("NO")
    all_close = False
if all_close:
    print("YES")
sys.stdout.close()
