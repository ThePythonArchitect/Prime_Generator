"""Usage:
engine = PrimeEngine()
sievelimit = 5000000
engine.Generate(sievelimit)
print(engine.time)
"""


#imports
from time import time
from bitarray import bitarray


class PrimeEngine:

    def __init__(self):
        self.sieve_array = []
        self.primes = [2]
        self.percent_complete1 = 0
        self.percent_complete2 = 0
        self.time = 0.0
        return None

    def SuperFastSieveSize(self, Limit):
        x = int(Limit)
        x = x - 5
        x = x // 2
        y = (int(Limit) - 3) // 6
        x = x - y
        return x

    def Generator(self, Limit):
        """This is a generator object that creates a sieve the length of self.Limit
        (this is a bitarray sieve, each bit represents a potential prime
        It adds 2 and 3 to self.primes since it cannot calculate primes that small
        It then follows the formula (((IndexValue*2)+5)+((IndexValue//2)*2)) to represent
        each potential primes (this will show all numbers not divisible by 2 or 3) to each bit.
        I.E. the first eight bits will represent 5, 7, 11, 13, 17, 19, 23, 25.  Only numbers divisible by
        primes higher than 3.  When the next prime is found by default, it yields it, then it marks
        all later bits in the sieve divisible by that prime following the same formula listed above.
        """
        self.primes = [2, 3]
        self.sieve_array = bitarray(self.SuperFastSieveSize(Limit))
        #(((IndexValue*2)+5)+((IndexValue//2)*2))
        IndexValue = 0
        SieveLength = len(self.sieve_array)
        while IndexValue < SieveLength:
            if self.sieve_array[IndexValue] == 0:
                yield (((IndexValue*2)+5)+((IndexValue//2)*2))
                for Multiple in range((IndexValue*3)+5, SieveLength, (((IndexValue*2)+5)+((IndexValue//2)*2))):
                    self.sieve_array[Multiple] = 1
            IndexValue += 1
        return None

    def Generate(self, Limit):
        Limit = int(Limit)
        self.sieve_array = []
        Generator = self.Generator(Limit)
        print(f'Calculating all primes up to {Limit}...')
        StartTime = time()
        self.primes = [PrimeNumber for PrimeNumber in Generator]
        self.time = time() - StartTime
        print(f'Done in {str(self.time)} seconds.')
        print(f'Last 5 primes calculated are: {self.primes[-5:]}')
        return None
        

if __name__ == "__main__":
    engine = PrimeEngine()
    engine.Generate(10000000)





    
