def table(base, func):
    print("\\begin{table}[H]")
    print("\\centering")
    align = "".join(["c"]*base)
    print("\\begin{tabular}{c|%s}" % align)
    print("\\toprule")
    for c in range(base):
        print(" & %d" % c, end="") 
    print("\\\\")
    print("\\midrule")

    for y in range(base):
        print("%d" % y, end="") 
        for x in range(base):
            res = func(x, y) % base
            print(" & %d" % res, end="") 
        print("\\\\")
    print("\\bottomrule")
    print("\\end{tabular}")
    print("\\caption{$\\mathbb{Z}_%d$}" % base)
    print("\\end{table}")
    print()
            
print("6, add")
table(6, lambda x, y: x + y)

print("6, mul")
table(6, lambda x, y: x * y)

print("7, add")
table(7, lambda x, y: x + y)

print("7, mul")
table(7, lambda x, y: x * y)
