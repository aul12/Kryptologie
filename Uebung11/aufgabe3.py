import math

n = 2923

x = math.ceil(math.sqrt(n))
z = x**2 - n

while x!=n:
    if math.sqrt(z).is_integer():
        print(f"Result: x={x}, y={math.sqrt(z)}")
        break
    x += 1
    z += 2*x + 1
    print(f"x={x}, z={z}")
