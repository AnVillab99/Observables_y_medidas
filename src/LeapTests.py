import unittest
import Complex as com
import Matrix as m
import math


class TestComplexVector(unittest.TestCase):

    def testBooleanMatrix(self):
        m1 = m.crear(6,6,[False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,True,False])
        
        v1 = m.crear(6,1,[6,2,1,5,3,10])
        r = m1.multiply(v1)
        R = m.crear(6,1,[0,0,12,5,1,9])
        self.assertTrue(r.equals(R))
    
    def testRendijaProbabilistica(self):
        m1=m.empty(11,11)
        m1.fix(1,0,com.Complex(1/3,0))
        m1.fix(2,0,com.Complex(1/3,0))
        m1.fix(3,0,com.Complex(1/3,0))
        m1.fix(4,1,com.Complex(1/3,0))
        m1.fix(5,1,com.Complex(1/3,0))
        m1.fix(6,1,com.Complex(1/3,0))
        m1.fix(6,2,com.Complex(1/3,0))
        m1.fix(7,2,com.Complex(1/3,0))
        m1.fix(8,2,com.Complex(1/3,0))
        m1.fix(8,3,com.Complex(1/3,0))
        m1.fix(9,3,com.Complex(1/3,0))
        m1.fix(10,3,com.Complex(1/3,0))
        m1.fix(4,4,com.Complex(1,0))
        m1.fix(5,5,com.Complex(1,0))
        m1.fix(6,6,com.Complex(1,0))
        m1.fix(7,7,com.Complex(1,0))
        m1.fix(8,8,com.Complex(1,0))
        m1.fix(9,9,com.Complex(1,0))
        m1.fix(10,10,com.Complex(1,0))
        v = m.crear(11,1,[1,0,0,0,0,0,0,0,0,0,0])
        m4 = m.multiplicar(m1,4)
        v4 = m4.multiply(v)
        v4=v4.round(4)
        r = m.crear(11,1,[0,0,0,0,0.1111,0.1111,0.2222,0.1111,0.2222,0.1111,0.1111])
        self.assertTrue(r.equals(v4))
    
    def testRendijaCuantica(self):
        m1=m.empty(11,11)
        m1.fix(1,0,com.Complex((-math.sqrt(6)/6),(math.sqrt(6)/6)))
        m1.fix(2,0,com.Complex((-math.sqrt(6)/6),(math.sqrt(6)/6)))
        m1.fix(3,0,com.Complex((-math.sqrt(6)/6),(math.sqrt(6)/6)))
        m1.fix(4,1,com.Complex((-math.sqrt(6)/6),(math.sqrt(6)/6)))
        m1.fix(5,1,com.Complex((-math.sqrt(6)/6),(-math.sqrt(6)/6)))
        m1.fix(6,1,com.Complex((math.sqrt(6)/6),(-math.sqrt(6)/6)))
        m1.fix(6,2,com.Complex((-math.sqrt(6)/6),(math.sqrt(6)/6)))
        m1.fix(7,2,com.Complex((-math.sqrt(6)/6),(-math.sqrt(6)/6)))
        m1.fix(8,2,com.Complex((math.sqrt(6)/6),(-math.sqrt(6)/6)))
        m1.fix(8,3,com.Complex((-math.sqrt(6)/6),(math.sqrt(6)/6)))
        m1.fix(9,3,com.Complex((-math.sqrt(6)/6),(-math.sqrt(6)/6)))
        m1.fix(10,3,com.Complex((-math.sqrt(6)/6),(-math.sqrt(6)/6)))
        m1.fix(4,4,com.Complex(1,0))
        m1.fix(5,5,com.Complex(1,0))
        m1.fix(6,6,com.Complex(1,0))
        m1.fix(7,7,com.Complex(1,0))
        m1.fix(8,8,com.Complex(1,0))
        m1.fix(9,9,com.Complex(1,0))
        m1.fix(10,10,com.Complex(1,0))
        v = m.crear(11,1,[1,0,0,0,0,0,0,0,0,0,0])
        m4 = m.multiplicar(m1,4)
        v4 = m4.multiply(v)
        v4=v4.round(4)
        r = m.crearR(11,1,[[0,0],[0,0],[0,0],[0,0],[0,-0.3333],[0.3333,0],[0,0],[0.3333,0],[0,0],[0.3333,0],[0.3333,0]])
        self.assertTrue(r.equals(v4))


    def testGraficar(self):
        #Se crea una matriz de 0
        m1=m.empty(9,9)
        #Se llenan las posiciones de la matriz con las probabilidades de por donde se puede ir el electron
        m1.fix(1,0,com.Complex(1/math.sqrt(2),0))
        m1.fix(2,0,com.Complex(1/math.sqrt(2),0))
        #Se llena la matriz con las probabilidades de a que punto de impacto llegara el electron
        m1.fix(4,1,com.Complex((-math.sqrt(6)/6),(math.sqrt(6)/6)))
        m1.fix(5,1,com.Complex((-math.sqrt(6)/6),(-math.sqrt(6)/6)))
        m1.fix(6,1,com.Complex((math.sqrt(6)/6),(-math.sqrt(6)/6)))
        m1.fix(6,2,com.Complex((-math.sqrt(6)/6),(math.sqrt(6)/6)))
        m1.fix(7,2,com.Complex((-math.sqrt(6)/6),(-math.sqrt(6)/6)))
        m1.fix(8,2,com.Complex((math.sqrt(6)/6),(-math.sqrt(6)/6)))
        #Se llena la matriz asuminedo que una vez ha llegado el electron se quedara en el punto de impacto
        m1.fix(4,4,com.Complex(1,0))
        m1.fix(5,5,com.Complex(1,0))
        m1.fix(6,6,com.Complex(1,0))
        m1.fix(7,7,com.Complex(1,0))
        m1.fix(8,8,com.Complex(1,0))
        #Se genera el vector inicial
        v = m.crear(9,1,[1,0,0,0,0,0,0,0,0])
        #Se realizan 2 clicks a la matriz
        m4 = m.multiplicar(m1,2)
        #Se multiplica el vector inicial por la matriz 
        v4 = m4.multiply(v)
        #Se hallan las probabilidades de que el electron se encuentre en X punto
        prob = v4.prob()
        #Se imprime el resultado
        m.printVector(prob)
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()