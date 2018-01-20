from six import integer_types


def int_to_charset(x, charset):
    """ Turn a non-negative integer into a string.
    """
    if not (isinstance(x, integer_types) and x >= 0):
        raise ValueError("x must be a non-negative integer.")
    if x == 0:
        return charset[0]
    output = ""
    while x > 0:
        x, digit = divmod(x, len(charset))
        output += charset[digit]
    return output


def charset_to_int(s, charset):
    """ Turn a string into a non-negative integer.
    """
    if not isinstance(s, (str)):
        raise ValueError("s must be a string.")
    if (set(s) - set(charset)):
        raise ValueError("s has chars that aren't in the charset.")
    return sum(len(charset)**i * charset.index(char) for i, char in enumerate(s))



""" Base16 includes numeric digits and the letters a through f. Here,
    we use the lowecase letters.
"""
base16_chars = '0123456789abcdef'

""" The Base58 character set allows for strings that avoid visual ambiguity
    when typed. It consists of all the alphanumeric characters except for
    "0", "O", "I", and "l", which look similar in some fonts.
    https://en.bitcoin.it/wiki/Base58Check_encoding
"""
base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

""" The Base32 character set allows for accurate transcribing by hand.
    It consists of uppercase letters + numerals, excluding "0", "1", + "8",
    which could look similar to "O", "I", and "B" and so are omitted.
    http://en.wikipedia.org/wiki/Base32
"""
base32_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

""" The z-base-32 character set is similar to the standard Base32 character
    set, except it uses lowercase letters + numerals and chooses to exclude
    "0", "l", "v", + "2". The set is also permuted so that easier chars
    occur more frequently.
    http://philzimmermann.com/docs/human-oriented-base-32-encoding.txt
"""
zbase32_chars = "ybndrfg8ejkmcpqxot1uwisza345h769"

""" The Base64 character set is a popular encoding for transmitting data
    over media that are designed for textual data. It includes all alphanumeric
    characters plus two bonus characters, usually "+" and "/".
    http://en.wikipedia.org/wiki/Base64
"""
base64_chars = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                "0123456789+/")
