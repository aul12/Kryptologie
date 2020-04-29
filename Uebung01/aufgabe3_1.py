import caesar

# Source: https://de.wikipedia.org/wiki/Buchstabenh%C3%A4ufigkeit
probabilities = {
    "e": 17.40 / 100,
    "n": 9.78 / 100,
    "i": 7.55 / 100,
    "s": 7.27 / 100,
    "r": 7.00 / 100,
    "a": 6.51 / 100,
    "t": 6.15 / 100,
    "d": 5.08 / 100,
    "h": 4.76 / 100,
    "u": 4.35 / 100,
    "l": 3.44 / 100,
    "c": 3.06 / 100,
    "g": 3.01 / 100,
    "m": 2.53 / 100,
    "o": 2.51 / 100,
    "b": 1.89 / 100,
    "w": 1.89 / 100,
    "f": 1.66 / 100,
    "k": 1.21 / 100,
    "z": 1.13 / 100,
    "p": 0.79 / 100,
    "v": 0.67 / 100,
    "j": 0.27 / 100,
    "y": 0.04 / 100,
    "x": 0.03 / 100,
    "q": 0.02 / 100
}

key_len = 5
text = "xipytdqgyxomprhanfllmwvlgeigahhqgyxoqgiheaeotqbkulpqpldzxhotfbyhkemdploqgotlzgutnpilplkjzxyakuwfvfzvsqerxtpphnqlklkpqul"

for i in range(key_len):
    subtext = text[i::key_len]
    pdf = dict()
    for c in range(ord('a'), ord('z')+1):
        pdf[chr(c)] = 0

    for c in subtext:
        pdf[c] += 1 / len(subtext)

    differences = []
    for key in range(26):
        difference = 0
        for char, prob in pdf.items():
            dec_char = caesar.decode(char, key, True)
            difference += (abs(prob - probabilities[dec_char]))

        differences.append((key, difference))

    differences.sort(key=lambda x: x[1])

    for c, diff in differences:
        print("%c (%f)" % (chr(c + ord('a')), diff), end="\t")
    print()
