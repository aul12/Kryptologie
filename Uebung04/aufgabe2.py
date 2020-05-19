num2name = {
    0: "alpha",
    1: "beta",
    2: "gamma",
    3: "delta"
}

def op(x, y):
    if x > y:
        y, x = x, y
    # Now y >= x

    if x == y:
        return 0

    # Now y > x
   
    if x == 0:
        return y
    if x == 1:
        if y == 2:
            return 3
        else:
            return 2
    else: #x==2 and y==3
        return 1

print("Op-Table:")
for x in range(4):
    for y in range(4):
        print(num2name[op(x,y)], end=" ")
    print()
print()

for a in range(4):
    for b in range(4):
        for c in range(4): 
            lhs = op(op(a, b), c)
            rhs = op(a, op(b, c))
            print("a = %s\t b = %s\t c = %s\t lhs = %s\t rhs = %s\t check = %s" \
                % (num2name[a], num2name[b], num2name[c], num2name[lhs], \
                    num2name[rhs], "Correct" if lhs == rhs else "Wrong"))

