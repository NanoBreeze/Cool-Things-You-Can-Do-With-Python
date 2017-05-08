

'''
This is not an efficient implementation but it's okay if we're not concerned about runtime speed!
'''
def printAllPrimesUpTo(n):
    primes = [2, 3]
    for i in range(4, n):
        isPrime = True
        for j in range(4, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime is True:
            primes.append(i)
    print(primes)


'''
We know that pi/4 = arctan(1)
According to the Taylor series arctan is, we also know that arctan(x) = x - (x^3)/3 + (x^5)/5 - (x^7)/7 + (x^9)/9 - ...
Combining the two statements above, we conclude that:
pi/4 = arctan(1)
     = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
pi   = 4 - 4/3 + 4/5 - 4/7 + 4/9 - ...
We note that we add every odd term and subtract every even term
'''
def computePi(termsInTaylorSeries):
    pi = 0
    for i in range(1, termsInTaylorSeries):
        term = 4/(i*2-1)
        if i % 2 == 0: #even term, so we subtract
            pi -= term
        else: #odd term, so we add
            pi += term

    print("Pi is approximately " + str(pi))



if __name__ == "__main__":
    printAllPrimesUpTo(10000)
    computePi(10000000)