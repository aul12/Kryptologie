import caesar

bigrams = {"er", "en", "ch", "de", "ei", "nd", "te", "in", "ie"}

key_len = 4
text = "xipytdqgyxomprhanfllmwvlgeigahhqgyxoqgiheaeotqbkulpqpldzxhotfbyhkemdploqgotlzgutnpilplkjzxyakuwfvfzvsqerxtpphnqlklkpqul"

key_probs = []
for k in range(key_len):
    key_probs.append(dict())
    for c in range(26):
        key_probs[k][c] = 1

for index, char in enumerate(text):
    key_index = index % key_len

    if index+1 < len(text):
        for k in range(26):
            decoded_first = caesar.decode(char, k, True)
            next_key_index = (index + 1) % key_len
            for k_next in range(26):
                decoded_next = caesar.decode(text[index+1], k_next, True)

                if decoded_first + decoded_next in bigrams:
                    key_probs[key_index][k] += 1
                    key_probs[next_key_index][k_next] += 1


for index, key_prob in enumerate(key_probs):
    print("%d\t" % index, end='')
    key_probs[index] = list(sorted(key_prob.items(), key=lambda item: item[1], reverse=True))
print()

for k in range(26):
    for c in range(key_len):
        char_num, prob = key_probs[c][k]
        print("%c\t" % chr(char_num + ord("a")), end='')
    print()
