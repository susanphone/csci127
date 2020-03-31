# ---------------------------------------------
# Object Oriented Example: Fractions
# ---------------------------------------------
# This example is based on the Interactive Textbook.
# ---------------------------------------------


# -------- Fraction Class ---------------------

def gcd(m, n):
    while m % n != 0:  #algorithm to get greatest common denominator
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n


class Fraction:         # this is mutable

    def __init__(self, top, bottom):      #Constructor method

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common


myfraction = Fraction(12, 16)

print(myfraction)           #12/16
myfraction.simplify()       # divide top and bottom by 4
print(myfraction)           # 3/4
