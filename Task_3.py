n = input()
a_arr = list(map(int, input()))
b_arr = list(map(int, input()))

a_arr.sort()
b_arr.sort()

ans = 0

for i in range(len(a_arr)):
    ans += a_arr[i] * b_arr[i]

print(ans)
