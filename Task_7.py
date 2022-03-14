S, n = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)

i = 0
cur_sum = 0

while i < len(A) and cur_sum + A[i] <= S:
    cur_sum += A[i]
    i += 1

print(i)