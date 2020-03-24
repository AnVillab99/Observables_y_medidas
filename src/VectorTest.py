import unittest
import Complex as com
import Matrix as m


class TestComplexVector(unittest.TestCase):

    
    def testSumaVector(self):
        v1 = m.Matrix([[com.Complex(1, 1), com.Complex(1, 1)]])
        v2 = m.Matrix([[com.Complex(1, 1), com.Complex(1, 1)]])
        s  = m.Matrix([[com.Complex(2, 2), com.Complex(2, 2)]])
        p = v1.suma(v2)
        self.assertTrue(s.equals(p))
        try:
            v1 = m.Matrix( [[com.Complex(1, 0), com.Complex(0, 0)]])
            v2 = m.Matrix( [[com.Complex(1, 2), com.Complex(2, 1), com.Complex(1, 3), com.Complex(3, 1)]])
        except ValueError as e:
            self.assertEqual(e,"Error en dimensiones de las matrices")
    def testRestaVector(self):
        v1 = m.Matrix([[com.Complex(1, 1), com.Complex(1, 1)]])
        v2 = m.Matrix([[com.Complex(1, 1), com.Complex(1, 1)]])
        s  = m.Matrix([[com.Complex(0, 0), com.Complex(0, 0)]])
        p = v1.resta(v2)  
        self.assertTrue(s.equals(p))
        try:
            v1 = m.Matrix( [[com.Complex(1, 0), com.Complex(0, 0)]])
            v2 = m.Matrix( [[com.Complex(1, 2), com.Complex(2, 1), com.Complex(1, 3), com.Complex(3, 1)]])
        except ValueError as e:
            self.assertEqual(e,"Error en dimensiones de las matrices")
    
    def testInversaVector(self):
        v1 = m.Matrix([[com.Complex(1, 1), com.Complex(1, 1)]])
        v2 = m.Matrix([[com.Complex(-1,- 1), com.Complex(-1, -1)]])
        s=v1.inverse()
        self.assertTrue(s.equals(v2))


    def testMultiplicacionVectores(self):
        v1 = m.Matrix([[com.Complex(1, 1)], [com.Complex(1, 5)]])
        v2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
        c = com.Complex(-13,17)
        s = v1.multiply(v2)
        print(c.printS())
        s.print()
        self.assertTrue(c.equals(c,s))








if __name__ == '__main__':
    unittest.main()