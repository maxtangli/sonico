def decode_morse(s):
    import re
    tokens = re.split('\s+', s.strip())
    decoded_tokens = [decode_morse_single(token) for token in tokens]
    return ','.join(decoded_tokens)


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
