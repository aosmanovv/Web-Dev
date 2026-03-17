class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        r = self.real * no.real - self.imaginary * no.imaginary
        i = self.real * no.imaginary + self.imaginary * no.real
        return Complex(r, i)

    def __truediv__(self, no):
        conjugate = no.conjugate()
        numerator = self * conjugate
        denominator = (no * conjugate).real
        return Complex(numerator.real / denominator, numerator.imaginary / denominator)

    def mod(self):
        return Complex((self.real ** 2 + self.imaginary ** 2) ** 0.5, 0)

    def conjugate(self):
        return Complex(self.real, -self.imaginary)

    def __str__(self):
        r = "{:.2f}".format(self.real)
        i = "{:.2f}".format(abs(self.imaginary))

        if self.real == 0 and self.imaginary == 0:
            return "0.00"

        if self.imaginary == 0:
            return r

        if self.real == 0:
            sign = "-" if self.imaginary < 0 else ""
            return f"{sign}{i}i"

        sign = "+" if self.imaginary > 0 else "-"
        return f"{r}{sign}{i}i"


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x.mod())
    print(y.mod())