import caesar
import sys

text = "xipytdqgyxomprhanfllmwvlgeigahhqgyxoqgiheaeotqbkulpqpldzxhotfbyhkemdploqgotlzgutnpilplkjzxyakuwfvfzvsqerxtpphnqlklkpqul"
if len(sys.argv) < 2:
    print("usage: %s key..." % sys.argv[0])
    exit(1)

for key in sys.argv[1:]:
    print("Key: %s\n\t" % key, end="")
    for index, char in enumerate(text):
        key_index = index % len(key)
        k = key[key_index]
        print(caesar.decode(char, ord(k) - ord("a"), True), end='')
    print()
