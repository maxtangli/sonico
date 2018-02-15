class BaseBars(list):
    def __init__(self, iterable, rules_trans, rules_write):
        super().__init__(iterable)
        self._rules_trans = rules_trans
        self._rules_write = rules_write

    def __str__(self):
        return ''.join(self)

    def next(self):
        rules = self._rules_trans

        result = Bars(' ' * len(self))
        for i in range(len(self)):
            if self[i] == ' ':
                continue
            offset, s = next([offset, s] for old, offset, s in rules if old == self[i])
            result.write(i + offset, s)

        self.clear()
        self.extend(result)
        return self

    def write(self, pos, s):
        for i, ch in enumerate(s):
            self.write_ch(pos + i, ch)

    def write_ch(self, pos, ch):
        n = len(self)
        i = (pos + n) % n

        rules = self._rules_write
        result = next(result for origin, plus, result in rules if origin == self[i] and plus == ch)
        self[i] = result


class SimpleBars(BaseBars):
    def __init__(self, iterable):
        rules_trans = [['i', -1, 'iTi'], ['T', 0, 'i']]
        rules_write = [' ii', ' TT', 'ii ']
        super().__init__(iterable, rules_trans, rules_write)


class Bars(BaseBars):
    def __init__(self, iterable):
        rules_trans = [['i', -1, 'iTi'], ['I', -1, 'iIi'], ['T', 0, 'i']]
        rules_write = [' ii', ' TT', ' II', 'ii ', 'TiI', 'iTI', 'IiT', 'iIT']
        super().__init__(iterable, rules_trans, rules_write)
