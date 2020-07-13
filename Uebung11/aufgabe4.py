N = 5

for x in range(N):
    y_squared = (x**3 + x) % N

    found_sqrt = False
    for y in range(N):
        y_squared_test = y**2 % N
        if y_squared == y_squared_test:
            print(f"x={x}, y={y}")
            found_sqrt = True
            break

    if not found_sqrt:
        print(f"No solution for x={x}")
    
