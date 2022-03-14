n = int(input())

ans = []
cur_sum = 0
i = 1

while cur_sum + i <= n:
    ans.append(i)
    cur_sum += i
    i+=1

if cur_sum != n:
    ans[-1] += n - cur_sum

print(len(ans))
print(*ans)