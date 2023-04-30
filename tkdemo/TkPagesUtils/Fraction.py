class Fraction:
    def __init__(self, top, bottom):
        self.gcdNum = self.gcd(top, bottom)
        self.top = self.integer(int(top / self.gcdNum))
        self.bottom = self.integer(int(bottom / self.gcdNum))

    def __str__(self):
        return str(self.top) + '/' + str(self.bottom)

    def __add__(self, other):
        newnum = self.top * other.bottom + \
                 self.bottom * other.top
        newden = self.bottom * other.bottom
        return Fraction(newnum, newden)

    def __sub__(self, other):
        newnum = self.top * other.bottom - \
                 self.bottom * other.top
        newden = self.bottom * other.bottom
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.top * other.top
        newden = self.bottom * other.bottom
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.top * other.bottom
        newden = self.bottom * other.top
        return Fraction(newnum, newden)

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom

        return first_num == second_num

    def __gt__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom

        return first_num > second_num

    def __ge__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom

        return first_num >= second_num

    def __lt__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom

        return first_num < second_num

    def __le__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom

        return first_num <= second_num

    def __ne__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom

        return first_num != second_num

    def getNum(self):
        return self.top

    def getDen(self):
        return self.bottom

    def gcd(self, m, n):
        m = self.integer(m)
        n = self.integer(n)
        while True:
            m %= n
            if m == 0:
                return n
            else:
                n, m = m, n

    @staticmethod
    def integer(num):
        num = str(int(num * 10))
        if num[-1:] == '0':
            return int(float(num) / 10)
        else:
            raise ValueError("Error: NOT RIGHT NUMBERS")

