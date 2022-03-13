import math

s = input()
n = len(s)
dp = [[0 for l in range(n)] for k in range(n)]
ep = [[0 for l in range(n)] for k in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 1

for right in range(n):
    for left in range(right, -1, -1):
        if left == right:
            # База динамики
            dp[left][right] = 1
        else:
            min = math.inf
            mink = -1
            if s[left] == '(' and s[right] == ')' \
                    or s[left] == '[' and s[right] == ']' \
                    or s[left] == '{' and s[right] == '}':
                # Случай соответствующих скобок
                min = dp[left + 1][right - 1]

            # Общий случай правила перехода динамики
            for k in range(left, right):
                if min > dp[left][k] + dp[k + 1][right]:
                    min = dp[left][k] + dp[k + 1][right]
                    # Поиск оптимального разбиения строки
                    mink = k
            dp[left][right] = min
            ep[left][right] = mink


# Восстановление ответа
def restoring_response(left, right):
    temp = right - left + 1
    if dp[left][right] == temp:
        return

    if dp[left][right] == 0:
        print(s[left:right + 1], end="")
        return

    if ep[left][right] == -1:
        # Если подстрока имеет в начале и конце соответствующего типа правильные скобки,
        # то печатаем левую скобку
        print(s[left], end="")
        # Вызов рекурсию вложенной подстроки
        restoring_response(left + 1, right - 1)
        # Печатаем правую скобку
        print(s[right], end="")
        return
    # Вызов рекурсии от левой и правой подстроки соответсвенно
    restoring_response(left, ep[left][right])
    restoring_response(ep[left][right] + 1, right)


restoring_response(0, n - 1)
