import unittest
import Complex as Complex
import math

class ComplexTest(unittest.TestCase):

    def testComplexSuma(self):
        a = Complex.Complex(1,-2)
        b = Complex.Complex(5,2)
        s = a.suma(b)
        self.assertTrue(6,s.real)
        self.assertAlmostEqual(0,s.imag)
        a = Complex.Complex(3,0)
        b = Complex.Complex(-5,0)
        s = a.suma(b)
        self.assertAlmostEqual(-2,s.real)
        self.assertAlmostEqual(0,s.imag)

        a = Complex.Complex(0,8)
        b = Complex.Complex(0,-4)
        s = a.suma(b)
        self.assertAlmostEqual(0,s.real)
        self.assertAlmostEqual(4,s.imag)

    def testComplexResta(self):
        a = Complex.Complex(1,-2)
        b = Complex.Complex(5,2)
        s = a.resta(b)
        self.assertTrue(-4,s.real)
        self.assertAlmostEqual(-4,s.imag)
        a = Complex.Complex(3,0)
        b = Complex.Complex(-5,0)
        s = a.resta(b)
        self.assertAlmostEqual(8,s.real)
        self.assertAlmostEqual(0,s.imag)

        a = Complex.Complex(0,8)
        b = Complex.Complex(0,-4)
        s = a.resta(b)
        self.assertAlmostEqual(0,s.real)
        self.assertAlmostEqual(12,s.imag)
    
    def testComplexMultiply(self):
        a = Complex.Complex(2,3)
        b = Complex.Complex(8,1)
        s = Complex.Complex.multiply(a,b)
        self.assertAlmostEqual(13,s.real)
        self.assertAlmostEqual(26,s.imag)
        a = Complex.Complex(2,3)
        b = Complex.Complex(8,1)
        s = Complex.Complex.multiply(a,b)
        self.assertAlmostEqual(13,s.real)
        self.assertAlmostEqual(26,s.imag)
        a = Complex.Complex(2,3)
        b = Complex.Complex(8,1)
        s = Complex.Complex.multiply(a,b)
        self.assertAlmostEqual(13,s.real)
        self.assertAlmostEqual(26,s.imag)
        a = Complex.Complex(2,3)
        b = Complex.Complex(0,0)
        s = Complex.Complex.multiply(a,b)
        self.assertAlmostEqual(0,s.real)
        self.assertAlmostEqual(0,s.imag)

    def testComplexDivide(self):
        try:
            a = Complex.Complex(1,3)
            b = Complex.Complex(5,3)
            s = Complex.Complex.divide(a,b)
            self.assertEqual(0.4118,round(s.real,4))
            self.assertEqual(0.3529,round(s.imag,4))
            a = Complex.Complex(1,3)
            b = Complex.Complex(0,0)
            s = Complex.Complex.divide(a,b)
            self.assertEqual(False,True)
        except ValueError  as e:
            self.assertEqual(str(e), "Denominador es 0")

    def testComplexSMultiply(self):
        a = Complex.Complex(1,3)
        s = a.sMultiply(2)
        self.assertEqual(2,round(s.real,4))
        self.assertEqual(6,round(s.imag,4))
        b = Complex.Complex(5,3)
        s = b.sMultiply(1.3)
        self.assertEqual(6.5,round(s.real,4))
        self.assertEqual(3.9,round(s.imag,4))
    
    def testComplexSDivide(self):
        a = Complex.Complex(3,6)
        s = a.sDivide(2)
        self.assertEqual(1.5,round(s.real,4))
        self.assertEqual(3,round(s.imag,4))
        b = Complex.Complex(5,3)
        s = b.sDivide(-2)
        self.assertEqual(-2.5,round(s.real,4))
        self.assertEqual(-1.5,round(s.imag,4))

    

    
    def testComplexConjugado(self):
        i = Complex.Complex(0,0)
        a = i.conjugado()
        self.assertEqual(0,a.imag)
        i = Complex.Complex(1,8)
        a = i.conjugado()
        self.assertEqual(-8,a.imag)
        i = Complex.Complex(0,-10)
        a = i.conjugado()
        self.assertEqual(10,a.imag)

        
    def testComplexModulo(self):
        i = Complex.Complex(2,2)
        self.assertEqual(2.8284,round(i.modulo(),4))

        i = Complex.Complex(-10,5)
        self.assertEqual(11.1803,round(i.modulo(),4)) 

        i = Complex.Complex(-4,9)
        self.assertEqual(9.8489,round(i.modulo(),4)) 

    def testComplexConvert(self):
        i = Complex.Complex(3,3)
        b = i.convert()
        self.assertEqual(4.2426, b.real)
        self.assertEqual(0.7854,b.imag)
        i = Complex.Complex(-9.8,5.5)
        b = i.convert()
        self.assertEqual(11.2379, b.real)
        self.assertEqual(2.6302 ,b.imag)

    def testComplexPhase(self):
        i = Complex.Complex(-9,81)
        self.assertEqual(1.6815,round(i.phase(),4))
        i = Complex.Complex(-97,16)
        self.assertEqual(2.9781,round(i.phase(),4))
        i = Complex.Complex(0,1)
        self.assertEqual(1.5708,round(i.phase(),4))

if __name__ == '__main__':
        unittest.main()