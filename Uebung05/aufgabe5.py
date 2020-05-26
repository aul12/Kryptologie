import random

def ggT(a, b):
    return a if b==0 else ggT(b, a % b)

# ax + by = d
def extggT(a, b):
    if b==0:
        return (a, 1, 0)
    
    d, x, y = extggT(b, a % b)
    return (d, y, x - (a//b) * y)

class PHChiffre:
    def __init__(self, n):
        self.n = n
        self.e = random.randint(1+1, n-1-1)
        while ggT(self.e, self.n-1) != 1:
            self.e = random.randint(1+1, n-1-1)
       
        self.d, _, _  = extggT(n-1, self.e)

    def encode(self, m):
        return m**self.e % self.n

    def decode(self, c):
        return c**self.d % self.n

def main():
    ph = PHChiffre(101)
    print(ph.e)
    print(ph.d)
    c = ph.encode(3)
    print(c)
    m_tilde = ph.decode(c)
    print(m_tilde)


if __name__=="__main__":
    main() 
