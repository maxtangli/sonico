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
