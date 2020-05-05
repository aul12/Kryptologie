def shift(b : list) -> list:
    new_b = list()
    new_b.append((b[0] != b[1]) != b[3])
    new_b.append(b[0])
    new_b.append(b[1])
    new_b.append(b[2])
    return new_b

def get_len(seed : int):
    initial_state = [seed & 8, seed & 4, seed & 2, seed & 1]
    initial_state = list(map(lambda x: True if x!=0 else 0, initial_state))
    state = initial_state
    count = 0
    print("Initial: ", state)

    while True:
        new_state = shift(state)
        count += 1
        if new_state == initial_state:
            print("\tSame state after %d shifts" % count)
            return count
        else:
            state = new_state

max_shift = 0
for c in range(2**4):
    l = get_len(c)
    if l > max_shift:
        max_shift = l
        max_seed = c

print("Maximum: %d with seed %d" % (max_shift, max_seed))
        
