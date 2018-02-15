from second_code import SimpleBars
import re

bs = SimpleBars(' ' * 78)
pos = 0;
acc = 1;
accx = 1;
output = ''

commands = '1(///(1iTiTiTi|||[(1 ])1( [L|[L|[L|[(] |1//)/)1i||1)///)1i||||1(///)1i\
(/////)1iTiTi[L!])|])[L!])])l|])1/( [(1/ ]L!l|[(1 ])1( //(1 ]L[L!|'

for c in commands:
    if c == '1':
        acc = 1
    elif c == '/':
        acc = acc * 2
    elif c == ')':
        pos += acc
        pos %= len(bs)
    elif c == '(':
        pos -= acc
        pos %= len(bs)
    elif c == 'i' or c == 'T' or c == ' ':
        for i in range(acc): bs[pos] = c; pos += 1; pos %= len(bs)
    elif c == ']':
        s = str(bs)[pos:] + str(bs)[:pos + 1]
        m = re.search('^ *[iT]* ', s)
        acc = (m and m.end() - 1) or 0
    elif c == '[':
        t = str(bs)
        s = t[pos - 1] + t[pos:] + t[:pos]
        m = re.search(' [iT]* *$', s)
        acc = (m and len(s) - m.start() - 1) or 0
    elif c == 'l':
        acc, accx = accx, acc
    elif c == 'L':
        acc, accx = accx - acc, accx + acc
    elif c == '|':
        print(bs)
        bs.next()
    elif c == '!':
        output += chr((ord('0') + acc) % 128)

print('answer: ' + output)  # MOON -> NOOM(invalid)
