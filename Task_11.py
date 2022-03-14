S, n = map(int, input().split())
A = list(map(int, input().split()))

F = [1] + [0] * S
F_new = F[:]

for j in range(len(A)):
    for i in range(A[j], S + 1):
        if F[i - A[j]] == 1:
            F_new[i] = 1
    F = F_new[:]

i = S
while F[i] == 0:
    i -= 1
print(i)
