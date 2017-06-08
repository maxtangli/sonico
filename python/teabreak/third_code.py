def decode_morse_single(s):
    keys = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    values = [
        "iI", "Iiii", "IiIi", "Iii", "i", "iiIi", "IIi",
        "iiii", "ii", "iIII", "Iii", "iIii", "II", "Ii",
        "III", "iIIi", "IIiI", "iIi", "iii", "I",
        "iiI", "iiiI", "iII", "IiiI", "IiII", "IIii",
        "iIIII", "iiIII", "iiiII", "iiiiI", "iiiii", "Iiiii", "IIiii", "IIIii", "IIIIi", "IIIII"
    ]
    try:
        pos = values.index(s)
        return keys[pos]
    except ValueError:
        return "?"


def decode_morse(s):
    result = ""
    token = ""
    for ch in s:
        if ch != " ":
            token += ch
        else:
            if token != "":
                result += decode_morse_single(token)
                result += " "
                token = ""
            else:
                result += " "
    return result

    # print(decode_morse_single("iIIII"))
    # print(decode_morse("iIIII iIIII  iIIII   iIIII"))
