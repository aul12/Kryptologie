import math
import random


def isPrime(x):
    for c in range(2, int(math.sqrt(x))+1):
        if x % c == 0:
            return False
    return True

def getPrime(minNum, maxNum):
    primes = [i for i in range(minNum, maxNum) if isPrime(i)]
    return random.choice(primes)

class Prover:
    def __init__(self):
        self.p = getPrime(3, 20) 
        self.q = getPrime(3, 20) 
        self.n = self.p * self.q 
        self.x = getPrime(1, self.n)
        self.y = getPrime(1, self.n)
        
    def commit(self):
        x_tilde = self.x**2 % self.n
        y_tilde = self.y**2 % self.n
        
        return self.n, x_tilde, y_tilde

    def prove(self, b):
        if b == 0:
            return self.y   
        else:
            return (self.x * self.y) % self.n

class Verifier:
    def __init__(self):
        pass

    def challenge(self, n, x_tilde, y_tilde):
        self.n = n
        self.x_tilde = x_tilde
        self.y_tilde = y_tilde
        self.b = random.randint(0, 1)
        return self.b

    def check(self, prove):
        if self.b == 0:
            return prove**2 % self.n == self.y_tilde
        else:
            return prove**2 % self.n == self.x_tilde * self.y_tilde % self.n

def main():
    p = Prover()
    v = Verifier()
    c = p.commit()
    print(f"Commit: n={c[0]}, x_tilde={c[1]}, y_tilde={c[2]}")
    b = v.challenge(*c)
    print(f"Challenge: b={b}")
    prove = p.prove(b)
    print(f"Prove: {prove}")
    result = v.check(prove)
    print(f"Result: {result}")    


if __name__ == "__main__":
    main()
