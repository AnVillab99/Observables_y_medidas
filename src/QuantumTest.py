import unittest
import Complex as com
import Matrix as m
import Quantum as q
import math

class QuantumTest(unittest.TestCase):

    
    def testNormalizar(self):
        v1 = m.Matrix([[com.Complex(2, -3), com.Complex(1, 2)]])
        v2 = v1.normalize()

    def testHallarParticulaProb(self):
        v=m.crearR(10,1,[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)])
        prob1=round(q.probParticle(v,7),4)
        prob2 = 0.1087
        self.assertTrue(prob2==prob1)
    
    def testMediaYVarianza(self):
        m1 = m.crearR(2,2,[(2,0),(1,1),(1,-1),(3,0)])
        v3 = m.crearR(2,1,[(1/math.sqrt(2),0),(0,1/math.sqrt(2))])
        esp =round(q.vEsperado(v3,m1),4)
        ans1 = 1.5
        self.assertTrue(esp==ans1)
        var =round(q.varianza(v3,m1),4)
        ans2=1.25
        self.assertTrue(var==ans2)


    


    def testAmplitudDeTransicion(self):
        #v=m.crearR(10,1,[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)])
        # print(q.probParticle(v,7))
        # for i in range(10):
        #     print(" p"+str(i)+" :"+str(q.probParticle(v,i)))
        #v2 =m.crearR(10,1,[(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)])
        #print("------")
        #print("amp trans : "+str(q.amplitudDeTransicion(v,v2).printS()))
        
        m1 = m.crearR(2,2,[(0,0),(1,0),(1,0),(0,0)])
        k = m1.vectoresPropios()
        ans =True
        for i in range(len(k)):
            prob = q.amplitudDeTransicion(m1,k[i])
            if(not round(prob.modulo(),1)==0.5):
                ans=False
        self.assertTrue(ans)



        
            
        
        

        






if __name__ == '__main__':
    unittest.main()