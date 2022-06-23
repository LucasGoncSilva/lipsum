from LIPSUM.settings.base import SECRET_KEY


def cover(text: str, key: str) -> str:
    chars = []
    keys_cat = list(zip(key*4, SECRET_KEY*4))
    xor_key = []
    text_list = []

    # define the key
    for i in keys_cat:
        char_code = ord(i[0]) ^ ord(i[1])
        xor_key.append(char_code)

    for i in text:
        text_list.append(ord(i))

    text_cat = list(zip(text_list, xor_key))

    # encrypt the text
    for i in text_cat:
        char_code = i[0] ^ i[1]
        chars.append(chr(char_code))

    return ''.join(chars)


def uncover(text: str, key: str) -> str:
    chars = []
    keys_cat = list(zip(key*4, SECRET_KEY*4))
    xor_key = []
    text_list = []

    # define the key
    for i in keys_cat:
        char_code = ord(i[0]) ^ ord(i[1])
        xor_key.append(char_code)

    for i in text:
        text_list.append(ord(i))

    text_cat = list(zip(text_list, xor_key))

    # encrypt the text
    for i in text_cat:
        char_code = i[0] ^ i[1]
        chars.append(chr(char_code))

    return ''.join(chars)
