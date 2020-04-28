# Source: https://de.wikipedia.org/wiki/Buchstabenh%C3%A4ufigkeit
probabilities = {
    "E":  17.40/100,
    "N":  9.78/100,
    "I":  7.55/100,
    "S":  7.27/100,
    "R":  7.00/100,
    "A":  6.51/100,
    "T":  6.15/100,
    "D":  5.08/100,
    "H":  4.76/100,
    "U":  4.35/100,
    "L":  3.44/100,
    "C":  3.06/100,
    "G":  3.01/100,
    "M":  2.53/100,
    "O":  2.51/100,
    "B":  1.89/100,
    "W":  1.89/100,
    "F":  1.66/100,
    "K":  1.21/100,
    "Z":  1.13/100,
    "P":  0.79/100,
    "V":  0.67/100,
    "J":  0.27/100,
    "Y":  0.04/100,
    "X":  0.03/100,
    "Q":  0.02/100
}

code="NRJ"

decodeWithProb = []

for k in range(26):
    decoded = list(map(lambda x: \
        chr((((ord(x)-ord("A")) + (26-k)) % 26) + ord("A")), code))
    prob = 1
    for d in decoded:
        prob = prob * probabilities[d]
    decodeWithProb.append(("".join(decoded), prob, k))

decodeWithProb.sort(key=lambda x: x[1], reverse=True)

probSum = 0
for _, p, _ in decodeWithProb:
    probSum += p

for d, p, k in decodeWithProb:
    print("%s\t(%f%%), Key: %c" % (d, (p*100)/probSum, chr(k + ord("A"))))
