I was very interested in prime numbers a couple years back, especially being able to generate them very quickly.  I figured I'd upload my old code anyway.
This is a prime number generator written in Python 3.  It's nowhere near as fast as the fastest generators out there, but it was fun to work on.
I learned a lot from it.  The best generators can produce all primes up to 1 billion in about a second on a mediocre computer.
This algorhithm can produce all primes up to 10 million in about a second on the average PC.

Usage:

engine = PrimeEngine()

engine.Generate(1000) #generate all primes up to 1000

You can access how long it took to complete the calculation through engine.time

The primes are accessed by engine.primes
