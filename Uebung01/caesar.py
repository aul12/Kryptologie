def encode(char, key, is_lower=False):
    start_char = ord("a" if is_lower else "A")
    numerical_char = ord(char) - start_char
    numerical_encoded = (numerical_char + key + 26) % 26
    return chr(numerical_encoded + start_char)


def decode(char, key, is_lower=False):
    return encode(char, 26 - key, is_lower)
