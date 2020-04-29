import caesar

text = "treffenmittwochneunuhrbahnhoffriedrichstrasse"
key = "plan"

encrypted = ""

for i, c in enumerate(text):
    if i < len(key):
        k = key[i]
    else:
        k = text[i - len(key)]
    e = caesar.encode(c, ord(k) - ord("a"), True)
    encrypted += e
    print("%c & %c & %c \\\\" % (c, k, e))

print(encrypted)
