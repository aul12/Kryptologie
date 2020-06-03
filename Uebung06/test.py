import random

def z_n_star(n):
    z_n = []
    for a in range(1, n-1):
        if ggT(a, n) == 1:
            z_n.append(a)
    return z_n

def ggT(a, b):
    return a if b == 0 else ggT(b, a % b)

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
    max_pq = 10
    max_i = 0
    for x in range(1, max_pq):
        for y in range(x, max_pq):
            p = 2*x + 1
            q = 2*y + 1
            if ggT(p, q) == 1:
                n, u, k, i, b_n = calc_b_n(p, q)
                z_n = z_n_star(n)

                candidates = []

                for z in z_n:
                    found = False
                    for b in b_n:
                        if b == z:
                            found = True
                    if not found:
                        candidates.append(z) 

                print(f"n={n}\tp={p}\tq={q}\trest={candidates}")

if __name__ == "__main__":
    main()
