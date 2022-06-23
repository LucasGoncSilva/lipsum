def cover(text: str, key: str) -> str:
    chars = []
    key_xor = len(key)

    for char in text:
        char_code = ord(char)
        new_char_code = char_code ^ key_xor
        chars.append(chr(new_char_code))

    return ''.join(chars)


def uncover(text: str, key: str) -> str:
    chars = []
    key_xor = len(key)

    for char in text:
        char_code = ord(char)
        new_char_code = char_code ^ key_xor
        chars.append(chr(new_char_code))

    return ''.join(chars)
