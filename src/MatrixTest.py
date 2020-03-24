import unittest
import Complex as com
import Matrix as m
import math



class TestComplexMatrix(unittest.TestCase):

    def testSumaMatriz(self):
        m1 = m.Matrix([[com.Complex(1, 1), com.Complex(1, 1)], [com.Complex(1, 2), com.Complex(1, 1)]])
        m2 = m.Matrix([[com.Complex(1, 1), com.Complex(1, 1)], [com.Complex(1, 2), com.Complex(1, 1)]])
        s  = m.Matrix([[com.Complex(2, 2), com.Complex(2, 2)], [com.Complex(2, 4), com.Complex(2, 2)]])
        p = m1.suma(m2)
        
        self.assertTrue(s.equals(p))

    def testInversaMatriz(self):
        m1 = m.Matrix([[com.Complex(1.5, 1), com.Complex(10, -11)], [com.Complex(1, 2.3), com.Complex(-1, 1)]])

        s = m.Matrix([[com.Complex(-1.5, -1), com.Complex(-10, 11)], [com.Complex(-1, -2.3), com.Complex(1, -1)]])
        p = m1.inverse()
        self.assertTrue(p.equals(s))


    
    def testMultiplicacionMatrices(self):
        try:
            m1 = m.Matrix([[com.Complex(1, 1),com.Complex(-2,1.6)], [com.Complex(-4.8,5),com.Complex(1, 5)]])
            m2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
            c = m.Matrix([[com.Complex(-8.8,1.2)],[com.Complex(-32.6,13.4)]])
            s = m1.multiply(m2)
            self.assertTrue(c.equals(s))
            m1 = m.Matrix([[com.Complex(1, 1),com.Complex(-2,1.6)], [com.Complex(-4.8,5),com.Complex(1, 5)]])
            m2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
            s = m1.multiply(m2)

        except ValueError as e:
            self.assertEqual(e,"Error en dimensiones de las matrices")

    def testMatrizTranspuesta(self):
        m2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
        m1  = m.Matrix([[com.Complex(2, 2), com.Complex(2,3)]])
        s =m2.transpuesta()
        self.assertTrue(s.equals(m1))
    
    def testMatrizConjugada(self):
        m2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
        m1  = m.Matrix([[com.Complex(2, -2)],[ com.Complex(2,-3)]])
        s =m2.conjugada()
        self.assertTrue(s.equals(m1))
    
    def testMatrizAdjunta(self):
        m2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
        m1  = m.Matrix([[com.Complex(2, -2), com.Complex(2,-3)]])
        s =m2.adjunta()
        self.assertTrue(s.equals(m1))

    def testAccionMatriz(self):
        m1 = m.Matrix([[com.Complex(1, 1),com.Complex(-2,1.6)], [com.Complex(-4.8,5),com.Complex(1, 5)]])
        m2  = m.Matrix([[com.Complex(2, 2)], [com.Complex(2,3)]])
        c = m.Matrix([[com.Complex(-8.8,1.2)],[com.Complex(-32.6,13.4)]])
        s = m1.multiply(m2)
        self.assertTrue(c.equals(s))

    
    def testNormaMatrix(self):
        M = m.Matrix([[com.Complex(3, 0), com.Complex(5, 0)], [com.Complex(2, 0), com.Complex(3, 0)]])
        s = 6.8557
        p = round(M.norma(),4)
        self.assertEqual(s, p)
        M = m.Matrix([[com.Complex(3, 8), com.Complex(5, 6)], [com.Complex(2, -1), com.Complex(3, -3)]])
        s = 12.53
        p = round(M.norma(),2)
        self.assertEqual(s, p)

    def testDistanciaMatriz(self):
        m1 = m.Matrix( [[com.Complex(3, 9), com.Complex(5, 6)], [com.Complex(2, -10), com.Complex(3, 0.5)]])
        m2 = m.Matrix([[com.Complex(0, 9), com.Complex(1, 3)], [com.Complex(-1, -1), com.Complex(0, 0)]])
        s= 11.5434
        p= round(m1.distancia(m2),4)
        self.assertEqual(p,s)

    def testMatrizUnitaria(self):
        m1 = m.Matrix( [[com.Complex(0.5, 0.5), com.Complex(0.5, -0.5)], [com.Complex(0.5, -0.5), com.Complex(0.5, 0.5)]])
        self.assertTrue(m1.unitaria())

    def testMatrizHermitiana(self):
        m1 = m.Matrix([[com.Complex(5, 0), com.Complex(3, 6), com.Complex(8, -15)], [
            com.Complex(3, -6), com.Complex(13, 0), com.Complex(2, -1)], [
            com.Complex(8, 15), com.Complex(2, 1), com.Complex(-2, 0)]])
        self.assertTrue(m1.hermetian())
        m1 = m.Matrix([[com.Complex(5, 0), com.Complex(3, 6), com.Complex(8, -15)], [
            com.Complex(3, -6), com.Complex(13, 1), com.Complex(2, -1)], [
            com.Complex(8, 15), com.Complex(2, 1), com.Complex(-2, 0)]])
        
        self.assertTrue(not m1.hermetian())

    def testProductoTensor(self):
        m1 = m.Matrix([[com.Complex(1, 0), com.Complex(2, 0)],[com.Complex(3, 0), com.Complex(4, 0)]])
        m2 = m.Matrix([[com.Complex(5, 0), com.Complex(6, 0)], [com.Complex(7, 0), com.Complex(8, 0)]])
        
        mr = m.Matrix([[com.Complex(5, 0), com.Complex(6, 0), com.Complex(10, 0), com.Complex(12, 0)],
        [com.Complex(7, 0), com.Complex(8, 0), com.Complex(14, 0), com.Complex(16, 0)],
        [com.Complex(15, 0), com.Complex(18, 0), com.Complex(20, 0), com.Complex(24, 0)],
        [com.Complex(21, 0), com.Complex(24, 0), com.Complex(28, 0), com.Complex(32, 0)]])

        r=m1.productoTensor(m2)
        
        self.assertTrue(mr.equals(r))
    
    def testQuantum1(self):
        H = m.Matrix([[com.Complex(1, 0), com.Complex(1, 0)],[com.Complex(1, 0), com.Complex(-1, 0)]])
        X = m.Matrix([[com.Complex(0, 0), com.Complex(1, 0)], [com.Complex(1, 0), com.Complex(0, 0)]])
        H=H.multiplyS((1/(math.sqrt(2))))
        HX=H.productoTensor(X)
        HH=H.productoTensor(H)
        v=m.Matrix([[com.Complex(1,0),com.Complex(0,0),com.Complex(0,0),com.Complex(0,0)]])
        r=v.multiply(HX)
        r2=r.multiply(HH)
        res = m.Matrix([[com.Complex(0.707,0),com.Complex(-0.707,0),com.Complex(0,0),com.Complex(0,0)]])
        r2=r2.round(3)
        self.assertTrue(res.equals(r2))
    
    def testVectoresPropios(self):
        m1 = m.Matrix([[com.Complex(1, 0), com.Complex(-3, 0),com.Complex(3, 0)],
        [com.Complex(3, 0), com.Complex(-5, 0), com.Complex(3, 0),],
        [com.Complex(6, 0), com.Complex(-6, 0), com.Complex(4, 0)]])
        m2 = m.Matrix([[com.Complex(1, 1), com.Complex(-3, -1),com.Complex(3, 1)],
        [com.Complex(3, 1), com.Complex(-5, -1), com.Complex(3, 1),],
        [com.Complex(6, 1), com.Complex(-6, -1), com.Complex(4, 0)]])
        R1 = [m.Matrix([[com.Complex(-1,0)],[com.Complex(0,0)],[com.Complex(1,0)]]),
        m.Matrix([[com.Complex(0.5,0)],[com.Complex(0.5,0)],[com.Complex(1,0)]])]
        R2 = [m.Matrix([[com.Complex(1,0)],[com.Complex(1,0)],[com.Complex(0,0)]]),
        m.Matrix([[com.Complex(0.5, 0.1667)],[com.Complex(0.5, 0.1667)],[com.Complex(1,0)]])]
        r1 =m1.vectoresPropios()
        r2 = m2.vectoresPropios()
        iguales =True
        for i in range(len(R1)):
            if(not (R1[i].round(4).equals(r1[i].round(4)))):
                iguales=False
        for i in range(len(R2)):
            if(not (R2[i].round(4).equals(r2[i].round(4)))):
                iguales=False
        self.assertTrue(iguales)

    
    def testValoresPropios(self):
        m1 = m.Matrix([[com.Complex(1, 0), com.Complex(-3, 0),com.Complex(3, 0)],
        [com.Complex(3, 0), com.Complex(-5, 0), com.Complex(3, 0),],
        [com.Complex(6, 0), com.Complex(-6, 0), com.Complex(4, 0)]])
        m2 = m.Matrix([[com.Complex(1, 1), com.Complex(-3, -1),com.Complex(3, 1)],
        [com.Complex(3, 1), com.Complex(-5, -1), com.Complex(3, 1),],
        [com.Complex(6, 1), com.Complex(-6, -1), com.Complex(4, 0)]])
        r1 =m1.valoresPropios()
        r2 = m2.valoresPropios()
        R1 =[com.Complex(4, 0), com.Complex(-2, 0), com.Complex(-2, 0),]
        R2 = [com.Complex(4, 0), com.Complex(-2, 0), com.Complex(-2, 0),]
        self.assertTrue(m.equalsEigenV(r1,R1))
        self.assertTrue(m.equalsEigenV(r2,R2))

    
        

if __name__ == '__main__':
    unittest.main()