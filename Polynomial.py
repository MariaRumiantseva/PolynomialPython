# Model class for a polynomial

class Polynomial (object):

    # Constructor
    def __init__(self, cf):
        # Create a polynomial from a list or array of coefficients
        # Polynomial ([])          -> P = 0
        # Polynomial ([0])         -> P = 0
        # Polynomial ([1])         -> P = 1
        # Polynomial ([4, 3])      -> P = 4x+3
        # Polynomial ([4.2, 3, 4]) -> P = 4.2x^2+3x+4

        self.coeffs = []
        self.degree = 0
        if isinstance(cf, list): # Polynomial([0]) Polynomial([1]) Polynomial([1,2,3])
            if not cf: # Polynomial([])
                self.coeffs = [0]
            else:
                for el in cf:
                    if not isinstance(el, (int, float)):
                        raise ValueError('Incorrect polynomial parameters', el, cf)
                        break;
                else: #no break
                    self.coeffs = cf
        elif isinstance(cf, Polynomial):
            self.coeffs = cf.coeffs[:]
        elif isinstance(cf, (int, float)): # creation of polynomials from scalars: Polynomial(10)
            self.coeffs.append(cf)
        else:
            raise ValueError('Incorrect polynomial parameters', cf, cf)

        if self.coeffs:
            self.degree = len(self.coeffs) - 1
        else:
            self.degree = 0

        # deleting NULL values from list of coeffs
        if self.coeffs:
            while len(self.coeffs) > 1 and self.coeffs[0] == 0:
                self.coeffs.pop(0)
        self.degree = len(self.coeffs) - 1 if len(self.coeffs) >= 1 else 0

    # Adding: polynom_1 + const & polynom_1 + polynom_2
    def __add__(self, arg):
        res = []
        if isinstance(arg, (int, float)):
            if self.coeffs: # non-empty list of polynomial coeffs
                res = self.coeffs[:]
                res[-1] += arg
            else: # zero polynomial
                res = arg
        elif isinstance(arg, Polynomial):
            if self.degree > arg.degree:
                res = self.coeffs[:]
                for i in range(0, arg.degree + 1, 1):
                    res[self.degree - arg.degree + i] += arg.coeffs[i]
            else:
                res = arg.coeffs[:]
                for i in range(0, self.degree + 1, 1):
                    res[arg.degree - self.degree + i] += self.coeffs[i]
        else:
            raise TypeError('Adding: Incorrect functional arguments (must be polynomial or const (int or float))', arg)
        return Polynomial(res)

    # Adding (with reflected operands): const + polynom_1
    def __radd__(self, other):
        return self + other

    # Negation: -polynom_1
    def __neg__(self):
        return Polynomial([-coeff for coeff in self.coeffs])

    # Subtracting: polynom_1 - const & polynom_1 - polynom_2
    def __sub__(self, arg):
        if isinstance(arg, (int, float, Polynomial)):
            return self.__add__(-arg)
        else:
            raise TypeError('Subtracting: Incorrect functional arguments (must be polynomial or const (int or float))', arg)

    # Subtracting (with reflected operands): const - polynom_1
    def __rsub__(self, arg):
        return (self.__neg__()).__add__(arg)

    # Multiplication: polynom_1 * const & polynom_1 * polynom_2
    def __mul__(self, arg):
        if isinstance(arg, (int, float)):
            return Polynomial([coeff * arg for coeff in self.coeffs])
        elif isinstance(arg, Polynomial):
            res = [0] * (self.degree + arg.degree + 1)
            for self_pow, self_coeff in enumerate(self.coeffs):
                for arg_pow, arg_coeff in enumerate(arg.coeffs):
                    res[self_pow + arg_pow] += self_coeff * arg_coeff
        else:
            raise TypeError('Multiplication: Incorrect functional arguments (must be polynomial or const (int or float))', arg)
        return Polynomial(res)

    # Multiplication (with reflected operands): const * polynom_1
    def __rmul__(self, other):
        return self * other

    # Equality: polynom_1 == const & polynom_1 == polynom_2 & polynom_1 == str
    def __eq__(self, arg):
        if isinstance(arg, (int, float)) and self.degree == 0:
            return self.coeffs[0] == arg
        elif isinstance(arg, Polynomial):
            return self.coeffs == arg.coeffs
        elif isinstance(arg, str):
            return str(self) == arg
        else:
            return False

    # Inequality: polynom_1 != const & polynom_1 != polynom_2 & polynom_1 != str
    def __ne__(self, arg):
        return not self == arg

    # To string
    def __str__(self):
        #  [4.2, 3, 4] -> 4.2x^2 + 3x + 4
        res = ""
        for pow, coeff in enumerate(self.coeffs):
            if coeff:
                if self.degree == 0:
                    res += str(coeff)
                else:
                    if abs(coeff) == 1:
                        if not (self.degree == pow):
                            res += ("+x" if coeff > 0 else "-x") + (("^" + str(self.degree - pow)) if not (self.degree - pow) == 1 else "")
                        else:
                            res += ("+" if coeff > 0 else "-") + str(abs(coeff))
                    else:
                        res += ("+" if coeff > 0 else "-") + str(abs(coeff))
                        if not (self.degree == pow):
                            res += "x" + (("^" + str(self.degree - pow)) if not (self.degree - pow) == 1 else "")
        if res:
            return res.lstrip("+")
        else:
            return "0"
