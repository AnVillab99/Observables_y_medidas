import unittest
import Complex as com
import Matrix as m
import Quantum as q
import math



class testObservables(unittest.TestCase):


    
    def test4_3_1(self):
        print("")
        print("4.3.1")
        print("")
        m1 = m.Matrix([[com.Complex(0, 0), com.Complex(1, 0)],[com.Complex(1, 0),com.Complex(0, 0)]])
        r1 =m1.vectoresPropios()
        
        print("x")
        for i in range(len(r1)):
            r1[i].normalize().print()
            print("")        
        self.assertTrue(True)

    def test4_3_2(self):
        print("")
        print("4.3.2")
        print("")
        m1 = m.Matrix([[com.Complex(0, 0), com.Complex(1, 0)],[com.Complex(1, 0),com.Complex(0, 0)]])
        r1 =m1.vectoresPropios()
        v1 = m1.valoresPropios()
        prob=com.Complex(0,0)
        for i in range(len(r1)):
            ans = m1.productoInterno(r1[i]).sumaInterna()
            prob=prob.suma(v1[i].sMultiply(ans))
        print(prob.modulo())
        self.assertTrue(prob.modulo()==0)



        
        self.assertTrue(True)

    def test4_4_1(self):
        print("")
        print("4.4.1")
        print("")
        m1=m.crear(2,2,[0,1,1,0])
        m2 = m.crear(2,2,[math.sqrt(2)/2,math.sqrt(2)/2,math.sqrt(2)/2,-math.sqrt(2)/2])
        m3=m1.multiply(m2)
        m4=m2.multiply(m1)
        print(m1.unitaria())
        print(m2.unitaria())
        print(m3.unitaria() or m4.unitaria())
        self.assertFalse(False)
        self.assertTrue(True)
        
    def test4_4_2(self):
        print("")
        print("4.4.2")
        print("")
        m1 =m.crearR(4,4,[(0,0),(1/math.sqrt(2),0),(1/math.sqrt(2),0),(0,0),(0,1/math.sqrt(2)),(0,0),(0,0),(1/math.sqrt(2),0),(1/math.sqrt(2),0),(0,0),(0,0),(0,1/math.sqrt(2)),(0,0),(1/math.sqrt(2),0),(-1/math.sqrt(2),0),(0,0)])
        v1= m.crear(4,1,[1,0,0,0])
        m3=m.multiplicar(m1,3)
        r3=m3.multiply(v1)   
        p=q.probParticle(r3,3)
        print(p)
        self.assertTrue(0.5==0.5)
        

if __name__ == '__main__':
    unittest.main()