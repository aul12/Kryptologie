import random

def calc_b_n(p, q):
    n = p * q
    
    tmp = n-1
    u = 0
    while tmp % 2 == 0:
        tmp //= 2
        u += 1
    k = tmp
    
    i = -1
    for i_tmp in range(u-1, -1, -1):
        for b in range(0, n):
            num = pow(b, 2**i_tmp, n)
            if num == n-1:
                i = i_tmp
                break

        if i != -1:
            break

    b_n = []
    for a in range(1, n-1):
        num = pow(a, k * 2**i, n)
        if num == 1  or num == n-1:
            b_n.append(a)

    return n, u, k, i, b_n
             

def main():
    max_pq = 1000
    max_i = 0
    for x in range(1, max_pq):
        for y in range(x, max_pq):
            p = 2*x + 1
            q = 2*y + 1
            n, u, k, i, b_n = calc_b_n(p, q)
            if i > max_i:
                max_i = i
                print(i)

if __name__ == "__main__":
    main()
