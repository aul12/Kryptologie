n = 23
e = 9

for m in range(1, 23):
    c = (m**e) % n
    print("%d & %d \\\\" % (m, c))
