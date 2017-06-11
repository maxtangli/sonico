def decode_morse(s):
    result = ''
    token = ''
    for ch in s:
        if ch != ' ':
            token += ch
        else:
            if token != '':
                result += decode_morse_single(token)
                result += ' '
                token = ''
            else:
                result += ' '
    return result


def decode_morse_single(s):
    chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    codes = [
        'iI', 'Iiii', 'IiIi', 'Iii', 'i', 'iiIi', 'IIi',
        'iiii', 'ii', 'iIII', 'Iii', 'iIii', 'II', 'Ii',
        'III', 'iIIi', 'IIiI', 'iIi', 'iii', 'I',
        'iiI', 'iiiI', 'iII', 'IiiI', 'IiII', 'IIii',
        'iIIII', 'iiIII', 'iiiII', 'iiiiI', 'iiiii', 'Iiiii', 'IIiii', 'IIIii', 'IIIIi', 'IIIII'
    ]
    d = dict(zip(codes, chars))
    return d.get(s, '?')
