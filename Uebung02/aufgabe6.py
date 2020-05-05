def list_xor(a : list, b : list) -> list:
    res = []
    for i, j in zip(a,b):
        res.append(i != j) 
    return res

def feistel(l : list, r : list, k : list, f) -> tuple:
    new_l = r
    new_r = list_xor(l, f(r, k))
    return (new_l, new_r)

def fun1(r, k):
    res = list_xor(r, k)
    return [res[1], res[0], res[3], res[2]]

def fun2(r, k):
    res = list_xor(r, k)
    return [res[3], res[1], res[0], res[2]]

def main():
    l = [True, False, True, True]
    r = [True, True, True, False]
    k = [False, False, False, False]

    print(feistel(l, r, k, fun1))

    l = [False, True, False, True]
    r = [True, False, False, True]
    k = [True, True, False, False]

    print(feistel(l, r, k, fun2))

if __name__ == "__main__":
    main()
    
