from math import sqrt, atan, log
class ComplexNumber:
    """
    The class of complex numbers.
    """
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary part.
        """
        self.real = real_part
        self.imaginary = imaginary_part
    def __repr__(self):
        """
        Return the string representation of self.
        """
        return "%s + %s i"%(self.real, self.imaginary)
    def __eq__(self, other):
        """
        Test if ``self`` equals ``other``.
        
        Two complex numbers are equal if their real parts are equal and
        their imaginary parts are equal.
        """
        return self.real == other.real and self.imaginary == other.imaginary
    def modulus(self):
        """
        Return the modulus of self.
        
        The modulus (or absolute value) of a complex number is the square
        root of the sum of squares of its real and imaginary parts.
        """
        return sqrt(self.real**2 + self.imaginary**2)
    def sum(self, other):
        """
        Return the sum of ``self`` and ``other``.
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    def product(self,other):
        """
        Return the product of other with self.
        """
        return ComplexNumber(self.real*other.real - self.imaginary*other.imaginary, self.real*other.imaginary + self.imaginary*other.real)
    def complex_conjugate(self):
        """
        An in-place complex conjugate of self.
        """
        self.imaginary *= -1

class NonZeroComplexNumber(ComplexNumber):
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary parts after checking validity.
        """
        if real_part == 0 and imaginary_part == 0:
            raise ValueError("Real or imaginary part should be nonzero.")
        return ComplexNumber.__init__(self, real_part, imaginary_part)
    def inverse(self):
        """
        Return the multiplicative inverse of ``self``.
        """
        den = self.real**2 + self.imaginary**2
        return NonZeroComplexNumber(self.real/den, -self.imaginary/den)
    def polar_coordinates(self):
        """
        Returns polar coordinates of a complex number.
        """
        r = self.modulus()
        theta = atan(self.imaginary/self.real)
        return (r, theta)
    def logarithm(self):
        """
        Returns logarithm of a complex number.
        """
        p = self.polar_coordinates()
        return NonZeroComplexNumber(log(p[0]), p[1])

## Test
## z1 = ComplexNumber(1,2)
## z2 = ComplexNumber(2,3)
## print z1.product(z2)
## z1.complex_conjugate()
## print "conjugate",z1
## z = NonZeroComplexNumber(2,-3)
## print z.polar_coordinates()
## print z.logarithm()