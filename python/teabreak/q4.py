# answer:
# ***************
# ITT TI I T TIii
# T i  I Iii  TTT

from second_code import Bars
from third_code import decode_morse

bs1 = Bars('ITT TI I T TIii')
bs2 = Bars('T i  I Iii  TTT')
bs = bs1
for i in range(30):
    s = decode_morse(str(bs))
    print(s)  # UNTEN -> NETNU
    bs.next()
