def largest_number(numbers):
    answer = ''
    boster = len(str(max(map(int, numbers))))

    while numbers:
        max_numbes = numbers[0]
        for number in numbers:
            if preparete_number(number, boster) > preparete_number(max_numbes, boster):
                max_numbes = number
        answer += max_numbes
        numbers.remove(max_numbes)
    return answer


def preparete_number(num, boster):
    num += '9' * (boster - len(num))
    return int(num)


n = input()

arr = list(input().split())

print(arr)
