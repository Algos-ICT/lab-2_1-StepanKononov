n, s = map(int, input().split())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))
n, s = 3, 5
data = [[2, 3], [10, 5], [5, 10]]

ans = []
delete_counter = 0
while delete_counter < len(data):
    cur_appel = 0
    decrease_min = 10 ** 10
    increase_max = -10 ** 10

    for i in range(len(data)):
        if data[i] is not None:
            if data[i][0] <= decrease_min:
                decrease_min = data[i][0]

    for i in range(len(data)):
        if data[i] is not None:
            if data[i][1] >= increase_max and data[i][0] == decrease_min:
                increase_max = data[i][1]
                cur_appel = i

    s -= data[cur_appel][0]
    if s <= 0:
        print(-1)
        break
    s += data[cur_appel][1]

    ans.append(cur_appel + 1)
    data[cur_appel] = None
    delete_counter += 1
else:
    print(*ans)
