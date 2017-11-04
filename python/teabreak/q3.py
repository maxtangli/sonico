from second_code import Bars
from third_code import decode_morse

bs = Bars('I    IT ii  i I   I i   i   I  T')
for i in range(26):
    print(bs)
    bs.next()

print(bs)

print('answer: ' + decode_morse(str(bs)))  # answer:   I   N  V   E R S   E -> INVERSE -> ESREVNI

# # invalid
# bs = Bars('I    IT ii  i I   I i   i   I  T'[::-1])
# for i in range(26):
#     print(bs)
#     bs.next()
#
# print(bs)
#
# print('answer: ' + decode_morse(str(bs)))  # answer:  E   S R E   B  A   I -> ESREBAI -> IABERSE
