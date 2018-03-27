import unittest
from Polynomial import Polynomial

class Tests_Polynomial(unittest.TestCase):

    # Initialization tests
    def test_Constructor(self):
        p0 = Polynomial([1, 2.1, 3, 4.5, 5])
        p1 = Polynomial([1, 3, 5])
        p2 = Polynomial([10])
        p3 = Polynomial([0])

        self.assertEqual(p0.coeffs, [1, 2.1, 3, 4.5, 5])
        self.assertEqual(p0.degree, 4)
        self.assertEqual(p1.coeffs, [1, 3, 5])
        self.assertEqual(p1.degree, 2)
        self.assertEqual(p2.coeffs, [10])
        self.assertEqual(p2.degree, 0)
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_EmptyConstructor(self):
        p0 = Polynomial([])

        self.assertEqual(p0.coeffs, [0])
        self.assertEqual(p0.degree, 0)

    def test_ScalarConstructor(self):
        p0 = Polynomial(0)
        p1 = Polynomial(1.2)
        p2 = Polynomial(15)

        self.assertEqual(p0.coeffs, [0])
        self.assertEqual(p0.degree, 0)
        self.assertEqual(p1.coeffs, [1.2])
        self.assertEqual(p1.degree, 0)
        self.assertEqual(p2.coeffs, [15])
        self.assertEqual(p2.degree, 0)

    def test_ConstructorBadCase(self):
        with self.assertRaises(Exception) as exc:
            p0 = Polynomial([1, 2.1, 3, 'x'])
        self.assertEqual(str(exc.exception), "('Incorrect polynomial parameters', 'x', [1, 2.1, 3, 'x'])")
        with self.assertRaises(Exception) as exc:
            p1 = Polynomial(['x'])
        self.assertEqual(str(exc.exception), "('Incorrect polynomial parameters', 'x', ['x'])")
        with self.assertRaises(Exception) as exc:
            p3 = Polynomial('x')
        self.assertEqual(str(exc.exception), "('Incorrect polynomial parameters', 'x', 'x')")

    def test_PolynomialConstructor(self):
        p0 = Polynomial([5, 4, 3, 2, 1])
        p1 = Polynomial(p0)
        p2 = Polynomial([0])
        p3 = Polynomial(p2)

        self.assertEqual(p1.coeffs, [5, 4, 3, 2, 1])
        self.assertEqual(p1.degree, 4)
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    # Null coefficients tests
    def test_DeletingNullCoeffs(self):
        p0 = Polynomial([0, 1, 2, 3])
        p1 = Polynomial([0, 1, 0, 0])
        p2 = Polynomial([0, 0, 2, 3])
        p3 = Polynomial([0, 0, 0, 3])
        p4 = Polynomial([0, 0, 0, 0])

        self.assertEqual(p0.coeffs, [1, 2, 3])
        self.assertEqual(p0.degree, 2)
        self.assertEqual(p1.coeffs, [1, 0, 0])
        self.assertEqual(p1.degree, 2)
        self.assertEqual(p2.coeffs, [2, 3])
        self.assertEqual(p2.degree, 1)
        self.assertEqual(p3.coeffs, [3])
        self.assertEqual(p3.degree, 0)
        self.assertEqual(p4.coeffs, [0])
        self.assertEqual(p4.degree, 0)

    # Adding tests
    def test_AddPolynomial(self):
        p0 = Polynomial([4, 1])
        p1 = Polynomial([4, 1, 2, 3])
        p2 = Polynomial([4, -1, 2, -3])
        p3 = Polynomial([4.5, -1, 2, -3.1])

        res0 = p0 + p1
        res1 = p0 + p2
        res2 = p0 + p3

        self.assertEqual(res0.coeffs, [4, 1, 6, 4])
        self.assertEqual(res0.degree, 3)
        self.assertEqual(res1.coeffs, [4, -1, 6, -2])
        self.assertEqual(res1.degree, 3)
        self.assertEqual(res2.coeffs, [4.5, -1, 6, -2.1])
        self.assertEqual(res2.degree, 3)

    def test_AddNullResult(self):
        p0 = Polynomial([2, 3])
        p1 = Polynomial([-2, -3])
        p2 = Polynomial([4, 1, -2, -3])
        p3 = Polynomial([4.5, -1.8, -2, -3])

        res0 = p0 + p1
        res1 = p0 + p2
        res2 = p0 + p3

        self.assertEqual(res0.coeffs, [0])
        self.assertEqual(res0.degree, 0)
        self.assertEqual(res1.coeffs, [4, 1, 0, 0])
        self.assertEqual(res1.degree, 3)
        self.assertEqual(res2.coeffs, [4.5, -1.8, 0, 0])
        self.assertEqual(res2.degree, 3)

    def test_AddNullPolynomial(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([])

        res0 = p0 + p1

        self.assertEqual(res0.coeffs, [4, 1, 2, 3])

    def test_AddIntValue(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial(10)
        p2 = Polynomial(-3)
        p3 = 10
        p4 = -3

        res0 = p0 + p1
        res1 = p0 + p2
        res2 = p0 + p3
        res3 = p0 + p4

        self.assertEqual(res0.coeffs, [4, 1, 2, 13])
        self.assertEqual(res1.coeffs, [4, 1, 2, 0])
        self.assertEqual(res2.coeffs, [4, 1, 2, 13])
        self.assertEqual(res3.coeffs, [4, 1, 2, 0])

    def test_AddFloatValue(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial(10.1)
        p2 = Polynomial(-3.0)
        p3 = 10.1
        p4 = -3.5

        res0 = p0 + p1
        res1 = p0 + p2
        res2 = p0 + p3
        res3 = p0 + p4

        self.assertEqual(res0.coeffs, [4, 1, 2, 13.1])
        self.assertEqual(res1.coeffs, [4, 1, 2, 0.0])
        self.assertEqual(res2.coeffs, [4, 1, 2, 13.1])
        self.assertEqual(res3.coeffs, [4, 1, 2, -0.5])

    def test_RAdd(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([3, 2])
        p2 = 10
        p3 = 0

        res0 = p1 + p0
        res1 = p2 + p0
        res2 = p3 + p0

        self.assertEqual(res0.coeffs, [4, 1, 5, 5])
        self.assertEqual(res1.coeffs, [4, 1, 2, 13])
        self.assertEqual(res2.coeffs, [4, 1, 2, 3])

    def test_AddBadCase(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = "4x^3+x^2+2x+3"

        with self.assertRaises(Exception) as context:
            res0 = p0 + p1
        self.assertEqual(str(context.exception),"('Adding: Incorrect functional arguments (must be polynomial or const (int or float))', '4x^3+x^2+2x+3')")

    # Negation tests
    def test_NegPolynomial(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([-4, -1, -2, -3])
        p2 = Polynomial(-p0)
        p3 = Polynomial([3])
        p4 = Polynomial(-p3)
        p5 = Polynomial([])
        p6 = Polynomial(-p5)

        self.assertTrue(p0 == -p1)
        self.assertTrue(-p0 == p1)
        self.assertTrue(p1 == p2)
        self.assertTrue(-p1 == -p2)
        self.assertTrue(-p3 == p4)
        self.assertTrue(p3 == -p4)
        self.assertTrue(p5 == p6)

    # Subtracting tests
    def test_SubPolynomial(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([2, 3])
        p2 = Polynomial([4, -1.8, 2, -1.3])
        p3 = Polynomial([4, 1, 2, 3])
        p4 = Polynomial([4])
        p5 = 4

        res0 = p0 - p1
        res1 = p0 - p2
        res2 = p0 - p3
        res3 = p0 - p4
        res4 = p0 - p5

        self.assertEqual(res0.coeffs, [4, 1, 0, 0])
        self.assertEqual(res0.degree, 3)
        self.assertEqual(res1.coeffs, [2.8, 0, 4.3])
        self.assertEqual(res1.degree, 2)
        self.assertEqual(res2.coeffs, [0])
        self.assertEqual(res2.degree, 0)
        self.assertEqual(res3.coeffs, [4, 1, 2, -1])
        self.assertEqual(res3.degree, 3)
        self.assertEqual(res4.coeffs, [4, 1, 2, -1])
        self.assertEqual(res4.degree, 3)

    def test_SubNullResult(self):
        p0 = Polynomial([2, 3])
        p1 = Polynomial([2, 3])
        p2 = Polynomial([4, 1, 2, 3])
        p3 = Polynomial([4.5, -1.8, 2, 3])

        res0 = p0 - p1
        res1 = p0 - p2
        res2 = p0 - p3

        self.assertEqual(res0.coeffs, [0])
        self.assertEqual(res0.degree, 0)
        self.assertEqual(res1.coeffs, [-4, -1, 0, 0])
        self.assertEqual(res1.degree, 3)
        self.assertEqual(res2.coeffs, [-4.5, 1.8, 0, 0])
        self.assertEqual(res2.degree, 3)

    def test_SubNullPolynomial(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([])

        res0 = p0 - p1

        self.assertEqual(res0.coeffs, [4, 1, 2, 3])
        self.assertEqual(res0.degree, 3)

    def test_SubIntFloatValue(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([4])
        p2 = 4
        p3 = -1.5

        res0 = p0 - p1
        res1 = p0 - p2
        res2 = p0 - p3

        self.assertEqual(res0.coeffs, [4, 1, 2, -1])
        self.assertEqual(res0.degree, 3)
        self.assertEqual(res1.coeffs, [4, 1, 2, -1])
        self.assertEqual(res1.degree, 3)
        self.assertEqual(res2.coeffs, [4, 1, 2, 4.5])
        self.assertEqual(res2.degree, 3)

    def test_RSub(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([2, 3])
        p2 = Polynomial([])
        p3 = 10
        p4 = 0

        res0 = p1 - p0
        res1 = p2 - p0
        res2 = p3 - p0
        res3 = p4 - p0

        self.assertEqual(res0.coeffs, [-4, -1, 0, 0])
        self.assertEqual(res0.degree, 3)
        self.assertEqual(res1.coeffs, [-4, -1, -2, -3])
        self.assertEqual(res1.degree, 3)
        self.assertEqual(res2.coeffs, [-4, -1, -2, 7])
        self.assertEqual(res2.degree, 3)
        self.assertEqual(res3.coeffs, [-4, -1, -2, -3])
        self.assertEqual(res3.degree, 3)

    def test_SubBadCase(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = "4x^3+x^2+2x+3"

        with self.assertRaises(Exception) as context:
            res = p0 - p1
        self.assertEqual(str(context.exception),"('Subtracting: Incorrect functional arguments (must be polynomial or const (int or float))', '4x^3+x^2+2x+3')")

    # Multiplication tests
    def test_MulPolynomial(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([2, 3])
        p2 = Polynomial([-2, -3])
        p3 = Polynomial([-2.5, 3.5])

        res0 = p0 * p1
        res1 = p0 * p2
        res2 = p0 * p3

        self.assertEqual(res0.coeffs, [8, 14, 7, 12, 9])
        self.assertEqual(res0.degree, 4)
        self.assertEqual(res1.coeffs, [-8, -14, -7, -12, -9])
        self.assertEqual(res1.degree, 4)
        self.assertEqual(res2.coeffs, [-10.0, 11.5, -1.5, -0.5, 10.5])
        self.assertEqual(res2.degree, 4)

    def test_MulNull(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([1, 0])
        p2 = Polynomial([0, 1, 0, 1])

        res0 = p0 * p1
        res1 = p0 * p2

        self.assertEqual(res0.coeffs, [4, 1, 2, 3, 0])
        self.assertEqual(res0.degree, 4)
        self.assertEqual(res1.coeffs, [4, 1, 6, 4, 2, 3])
        self.assertEqual(res1.degree, 5)

    def test_MulNullPolynomial(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([])

        res0 = p0 * p1

        self.assertEqual(res0.coeffs, [0])
        self.assertEqual(res0.degree, 0)

    def test_MulOneValue(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([3])
        p2 = Polynomial([0])
        p3 = Polynomial(0)
        p4 = Polynomial(3)
        p5 = 0
        p6 = 3

        res0 = p0 * p1
        res1 = p0 * p2
        res2 = p0 * p3
        res3 = p0 * p4
        res4 = p0 * p5
        res5 = p0 * p6

        self.assertEqual(res0.coeffs, [12, 3, 6, 9])
        self.assertEqual(res1.coeffs, [0])
        self.assertEqual(res2.coeffs, [0])
        self.assertEqual(res3.coeffs, [12, 3, 6, 9])
        self.assertEqual(res4.coeffs, [0])
        self.assertEqual(res5.coeffs, [12, 3, 6, 9])

    def test_RMul(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([])
        p2 = Polynomial([3])
        p3 = Polynomial(0)
        p4 = 3

        res0 = p1 * p0
        res1 = p2 * p0
        res2 = p3 * p0
        res3 = p4 * p0

        self.assertEqual(res0.coeffs, [0])
        self.assertEqual(res0.degree, 0)
        self.assertEqual(res1.coeffs, [12, 3, 6, 9])
        self.assertEqual(res1.degree, 3)
        self.assertEqual(res2.coeffs, [0])
        self.assertEqual(res2.degree, 0)
        self.assertEqual(res3.coeffs, [12, 3, 6, 9])
        self.assertEqual(res3.degree, 3)

    def test_MulStrBadCase(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = "4x^3+x^2+2x+3"

        with self.assertRaises(Exception) as context:
            res = p0 * p1
        self.assertEqual(str(context.exception),"('Multiplication: Incorrect functional arguments (must be polynomial or const (int or float))', '4x^3+x^2+2x+3')")

    # Equality tests
    def test_EqualPolynomial(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([4, 1, 2, 3])
        p2 = Polynomial([-4, -1, -2, -3])
        p3 = Polynomial([4, -1, 2, -3])
        p4 = "4x^3+x^2+2x+3"
        p5 = Polynomial([5])
        p6 = 5
        p7 = Polynomial(-5)
        p8 = -5
        p9 = Polynomial([])
        p10 = 0

        self.assertTrue(p0 == p1)
        self.assertTrue(p0 == p0)
        self.assertFalse(p0 == p2)
        self.assertFalse(p0 == p3)
        self.assertTrue(p0 == p4)
        self.assertTrue(p5 == p6)
        self.assertTrue(p7 == p8)
        self.assertTrue(p9 == p10)

    def test_NotEqualPolynomial(self):
        p0 = Polynomial([4, 1, 2, 3])
        p1 = Polynomial([4, 1, 2, 3])
        p2 = Polynomial([-4, -1, -2, -3])
        p3 = Polynomial([4, -1, 2, -3])
        p4 = "4x^3+x^2+2x+3"
        p5 = Polynomial([5])
        p6 = 5
        p7 = Polynomial(-5)
        p8 = -5
        p9 = Polynomial([])
        p10 = 0

        self.assertFalse(p0 != p1)
        self.assertFalse(p0 != p0)
        self.assertTrue(p0 != p2)
        self.assertTrue(p0 != p3)
        self.assertFalse(p0 != p4)
        self.assertFalse(p5 != p6)
        self.assertFalse(p7 != p8)
        self.assertFalse(p9 != p10)

    # String tests
    def test_StrPolynomial(self):
        p0 = Polynomial([0, 0, 0, 0])
        p1 = Polynomial([1, 1, 1, 1])
        p2 = Polynomial([4, 1, 2, 3])
        p3 = Polynomial([-4, -1, -2, -3])
        p4 = Polynomial([-4, 1.5, -2, 3.1])
        p5 = Polynomial([1, 1])
        p6 = Polynomial([2])
        p7 = Polynomial([0])
        p8 = Polynomial([])

        self.assertEqual(str(p0), "0")
        self.assertEqual(str(p1), "x^3+x^2+x+1")
        self.assertEqual(str(p2), "4x^3+x^2+2x+3")
        self.assertEqual(str(p3), "-4x^3-x^2-2x-3")
        self.assertEqual(str(p4), "-4x^3+1.5x^2-2x+3.1")
        self.assertEqual(str(p5), "x+1")
        self.assertEqual(str(p6), "2")
        self.assertEqual(str(p7), "0")
        self.assertEqual(str(p8), "0")

    def test_StrPosNull(self):
        p0 = Polynomial([4, 1, 2, 0])
        p1 = Polynomial([4, 1, 0, 3])
        p2 = Polynomial([4, 0, 2, 3])
        p3 = Polynomial([4, 0, 0, 0])
        p4 = Polynomial([4, 0, 0, 1])
        p5 = Polynomial([0, 1, 2, 3])
        p6 = Polynomial([0, 0, 2, 3])
        p7 = Polynomial([0, 1, 0, 3])
        p8 = Polynomial([0, 1, 2, 0])
        p9 = Polynomial([0, 0, 0, 1])
        p10 = Polynomial([0, 0, 0, 0])

        self.assertEqual(str(p0), "4x^3+x^2+2x")
        self.assertEqual(str(p1), "4x^3+x^2+3")
        self.assertEqual(str(p2), "4x^3+2x+3")
        self.assertEqual(str(p3), "4x^3")
        self.assertEqual(str(p4), "4x^3+1")
        self.assertEqual(str(p5), "x^2+2x+3")
        self.assertEqual(str(p6), "2x+3")
        self.assertEqual(str(p7), "x^2+3")
        self.assertEqual(str(p8), "x^2+2x")
        self.assertEqual(str(p9), "1")
        self.assertEqual(str(p10), "0")

    def test_StrNegNull(self):
        p0 = Polynomial([-4, -1, -2, 0])
        p1 = Polynomial([-4, -1, 0, -3])
        p2 = Polynomial([-4, 0, -2, -3])
        p3 = Polynomial([-4, 0, 0, 0])
        p4 = Polynomial([-4, 0, 0, -1])
        p5 = Polynomial([0, -1, -2, -3])
        p6 = Polynomial([0, 0, -2, -3])
        p7 = Polynomial([0, -1, 0, -3])
        p8 = Polynomial([0, -1, -2, 0])
        p9 = Polynomial([0, 0, 0, -1])
        p10 = Polynomial([0, 0, 0, 0])

        self.assertEqual(str(p0), "-4x^3-x^2-2x")
        self.assertEqual(str(p1), "-4x^3-x^2-3")
        self.assertEqual(str(p2), "-4x^3-2x-3")
        self.assertEqual(str(p3), "-4x^3")
        self.assertEqual(str(p4), "-4x^3-1")
        self.assertEqual(str(p5), "-x^2-2x-3")
        self.assertEqual(str(p6), "-2x-3")
        self.assertEqual(str(p7), "-x^2-3")
        self.assertEqual(str(p8), "-x^2-2x")
        self.assertEqual(str(p9), "-1")
        self.assertEqual(str(p10), "0")

if __name__ == '__main__':
    unittest.main()
