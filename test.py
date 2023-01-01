import prime


def findthree(num):
    combination = []
    first = 0
    second = 0
    third = 0
    a = prime.Prime()
    s = a.RangePrimes(1,num)
    for i in range(1,len(s)):
        first = s[i]
        for j in range(1,len(s)):
            second = s[j]
            third = num - first - second
            if third > 0:
                combination.append([first, second, third])
    return combination


print(findthree(20))
        