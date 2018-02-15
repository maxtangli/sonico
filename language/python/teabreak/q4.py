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
    print(bs, s)  # UNTEN -> NETNU
    bs.next()

# # invalid
# # br -> '', T -> ' '
# print(decode_morse('I I I Iii i I Iii ii iiI Ii iii IiI ii I I IIi I I iiiii i II I I I I i I Ii I Ii iiI I Iii IiiiI i I Ii I i I iiii iiIiIi I I IiiI I I I I iIiiI I Ii iii III I I I I II iiIi I IiIi iI II I IIiii i Iii I i ii Ii I iiIiiiII I I I I i I I Ii ii Ii iiI I I II IiI Ii I i ii I Iii iiiiiIIiI I Ii I II I I ii i ii I I IIiiii I I I I iiI Ii I i Ii '))
# # br -> ' ', T -> ' '
# print(decode_morse('I I I Iii i I Iii ii iiI Ii iii IiI ii I I IIi I I i iiii i II I I I I i I Ii I Ii iiI I Iii IiiiI i I Ii I i I iiii iiIi Ii I I IiiI I I I I iIi iI I Ii iii III I I I I II iiIi I IiIi iI II I IIiii i Iii I i ii Ii I ii IiiiII I I I I i I I Ii ii Ii iiI I I II IiI Ii I i ii I I ii iiiiiIIiI I Ii I II I I ii i i i I I IIiiii I I I I iiI Ii I i Ii '))
