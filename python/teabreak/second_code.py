class SimpleBars(list):
    def write(self, pos, ch):
        n = len(self)
        i = (pos + n) % n
        # [ ] + i -> i, [ ] + T -> T, i + i -> [ ], else error
        if self[i] == " " and ch == "i":
            self[i] = "i"
        elif self[i] == " " and ch == "T":
            self[i] = "T"
        elif self[i] == "i" and ch == "i":
            self[i] = " "
        else:
            raise Exception()

    def next(self):
        # i -> iTi, T -> i, i + i -> []
        result = SimpleBars(" " * len(self))
        for i in range(len(self)):
            if self[i] == "i":
                result.write(i - 1, "i")
                result.write(i, "T")
                result.write(i + 1, "i")
            elif self[i] == "T":
                result.write(i, "i")
            else:
                pass

        for i in range(len(result)):
            self[i] = result[i]

        return self

    def __str__(self):
        return "".join(self)


class Bars(SimpleBars):
    def write(self, pos, ch):
        n = len(self)
        i = (pos + n) % n
        # [ ] + i -> i, [ ] + T -> T, i + i -> [ ], else error
        maps = [" ii", " TT", " II", "ii ", "TiI", "iTI", "IiT", "iIT"]
        for s in maps:
            if self[i] == s[0] and ch == s[1]:
                self[i] = s[2]
                return
        raise Exception()

    def next(self):
        # i -> iTi, T -> i, i + i -> []
        result = Bars(" " * len(self))
        for i in range(len(self)):
            if self[i] == "i":
                result.write(i - 1, "i")
                result.write(i, "T")
                result.write(i + 1, "i")
            elif self[i] == "I":
                result.write(i - 1, "i")
                result.write(i, "I")
                result.write(i + 1, "i")
            elif self[i] == "T":
                result.write(i, "i")
            else:
                pass

        for i in range(len(result)):
            self[i] = result[i]

        return self

    def __str__(self):
        return "".join(self)
