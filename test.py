import prime


def findthree(num):
    combination = []
    first = 0
    second = 0
    third = 0
    s = prime.RangePrimes(1,num)
    print(s)
    for i in range(1,len(s)):
        first = s[i]
        for j in range(1, len(s)):
            second = s[j]
            third = num - first - second
            if third > 0 and prime.DetectPrime(third):
                combination.append([first, second, third])
            
    return combination


print(findthree(100))




        