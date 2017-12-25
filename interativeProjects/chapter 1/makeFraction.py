import sys

def gcd(m, n):
    while m%n != 0:
        oldm =m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction():
    """ has getNum and getDen return numerator and demonminator of a fraction"""
    def __init__(self, top, bottom):
        try:

            common = gcd(top, bottom)
            self.num = top//common
            self.den = bottom//common
        except TypeError:
            print('Number is a type error')
            sys.exit()

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    # returns numerator
    def getNum(self):
        return str(self.num)

    #returns denominator
    def getDen(self):
        return self.den

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num

        return Fraction(newnum, newden)

    # checks if self fractions is greater then
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    #greater than or equal
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    #Less than
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    #Less than or equal
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    # not equal too
    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum

    # 7 class instance (self) is on the right-hand side of the operator and the other object is on the left-hand side.
    # http://hplgit.github.io/primer.html/doc/pub/class/._class-solarized005.html control + f to find answer
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            other = Fraction(other, 1)
        return self.__add__(other)

    # 8 essentially replaces += function
    def __iadd__(self, other):
        self.num += other.num
        return self

    # 9 https://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
    def __repr__(self):
        return '%s(%r)' % (self.__class__, self.__str__())




    # tests errror
# Fraction("5", 43)

x = Fraction(2,4)
y = Fraction(5,12)

print(x+=y)

print(x.getDen())
print(x - y)
print(x * y)
print(x/y)
print(x>y)
print(x<=y)
print(x!=y)
print(x+y)
