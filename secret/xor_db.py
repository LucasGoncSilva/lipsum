from LIPSUM.settings.base import SECRET_KEY


def xor(text: str, key: str, encrypt: bool=True) -> str:
    if text is None:
        return text

    try:
        text = str(text)
    except:
        return text

    SK: str = SECRET_KEY[16:]

    # Set the same and sufficient len() for the key's parent
    keys_cat: list[tuple[str, str]] = list(zip(
        key * (len(text) // len(key) + 1),
        SK * (len(text) // len(SK) + 1)
    ))

    # Define the key
    xor_key: list[int] = [(ord(i[0]) ^ ord(i[1]) + 32) for i in keys_cat]

    # Get the code value for each char in text
    if encrypt:
        text_list: list[int] = [ord(i) for i in text]
    else:
        text_list: list[int] = [(ord(i) - 32) for i in text]

    # Set the same len() for text_list and xor_key
    text_cat: list[tuple[int, int]] = list(zip(text_list, xor_key))

    # XOR the text
    if encrypt:
        chars: list[str] = [chr((i[0] ^ i[1]) + 32) for i in text_cat]
    else:
        chars: list[str] = [chr(i[0] ^ i[1]) for i in text_cat]

    return ''.join(chars)
