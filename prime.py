# Prime module (Mojtaba Ghahri)
__all__ =[
    "Prime","DetectPrime","RangePrimes"
]
class Prime:
    def __init__(self):
        self.flag = 0
        self.prime_list = []

    def DetectPrime(self, number):
        for i in range(2, number):
            self.flag = 0
            if number % i == 0:
                self.flag += 1
                break
        if self.flag == 0:
            return True
        else:
            return False


    def RangePrimes(self, start, stop):
        """accept start point and end point to find prime numbers between them"""
        for i in range(start, stop):
            if self.DetectPrime(i):
                self.prime_list.append(i)
        return self.prime_list

    def __str__(self) -> str:
        return f'{self.prime_list}' 

_inst = Prime()
DetectPrime = _inst.DetectPrime
RangePrimes = _inst.RangePrimes


if __name__ == '__main__':
    print("Wellcome to prime module")

