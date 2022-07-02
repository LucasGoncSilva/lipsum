from LIPSUM.settings.base import SECRET_KEY


def cover(text: str, key: str) -> str:
    if text is None:
        return text

    try:
        text = str(text)
    except:
        return text

    text_len = len(text)
    xor_key, text_list = [], []
    func_secret_key: str = SECRET_KEY[16:]

    keys_cat: list[tuple[str, str]] = list(zip(
        key * (text_len // len(key) + 1),
        func_secret_key * (text_len // len(func_secret_key) + 1)
    ))

    # define the key
    for i in keys_cat:
        char_code = ord(i[0]) ^ ord(i[1])
        xor_key.append(char_code)

    for i in text:
        text_list.append(ord(i))

    text_cat = list(zip(text_list, xor_key))

    # encrypt the text
    chars = [chr(i[0] ^ i[1]) for i in text_cat]

    return ''.join(chars)


def uncover(text: str, key: str) -> str:
    if text is None:
        return text

    try:
        text = str(text)
    except:
        return text

    text_len = len(text)
    xor_key, text_list = [], []
    func_secret_key: str = SECRET_KEY[16:]

    keys_cat: list[tuple[str, str]] = list(zip(
        key * (text_len // len(key) + 1),
        func_secret_key * (text_len // len(func_secret_key) + 1)
    ))

    # define the key
    for i in keys_cat:
        char_code = ord(i[0]) ^ ord(i[1])
        xor_key.append(char_code)

    for i in text:
        text_list.append(ord(i))

    text_cat = list(zip(text_list, xor_key))

    # encrypt the text
    chars = [chr(i[0] ^ i[1]) for i in text_cat]

    return ''.join(chars)
