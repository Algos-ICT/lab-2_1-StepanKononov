import random
import sys
sys.stdout = open('INPUT.TXT', 'w')

suits = ['S', 'C', 'D', 'H']

values = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
N, M = random.randint(1, 35), random.randint(1, 35)
suit = suits[random.randint(0, len(suits)-1)]

line_1 = ''
line_2 = ''

for i in range(N):
    line_1 += values[random.randint(0,len(values)-1)] + suits[random.randint(0, len(suits)-1)] + ' '
for i in range(M):
    line_2 += values[random.randint(0, len(values)-1)] + suits[random.randint(0, len(suits)-1)] + ' '

print(N, M, suit)
print(line_1)
print(line_2)
sys.stdout.close()
