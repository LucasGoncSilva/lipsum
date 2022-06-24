from LIPSUM.settings.base import SECRET_KEY


def cover(text: str, key: str) -> str:
    if text is None:
        return text

    try:
        text = str(text)
    except:
        return text

    text_len = len(text)
    chars = []
    keys_cat = list(zip(
        key * (text_len // len(key) + 1),
        SECRET_KEY * (text_len // len(SECRET_KEY) + 1)
    ))
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
    if text is None:
        return text

    try:
        text = str(text)
    except:
        return text

    text_len = len(text)
    chars = []
    keys_cat = list(zip(
        key * (text_len // len(key) + 1),
        SECRET_KEY * (text_len // len(SECRET_KEY) + 1)
    ))
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