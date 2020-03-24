import sys

import math

class Complex:
    def __init__(self,r,i): 
        self.real=r #real
        self.imag=i #imaginaro
        
    

    """ Este metodo devuelve la suma de este complejo y otro proporcionado
    @param b Complex
    @return Complex la suma"""
    def suma(self,b):
        realI = self.real+b.real
        imaginarioI = self.imag+b.imag
        return Complex(realI,imaginarioI)
    
    """Este metodo devuelve la resta de este complejo y otro proporcionado
    # @param b Complex
    # @return Complex la resta"""
    def resta(self,b):
        real = self.real-b.real
        imaginario = self.imag-b.imag
        return Complex(real,imaginario)
    
    """ Este metodo devuelve la multiplicacion este complejo y otro proporcionado
    # @param b Complex
    # @return Complex la multiplicacion"""

    def multiply(self,b):
        real = (self.real*b.real)-(self.imag*b.imag)
        imaginario = (self.real*b.imag)+(b.real*self.imag)
        return Complex(real,imaginario)
    
    """# Este metodo devuelve la divicion este complejo y otro proporcionado
    # @param b Complex
    # @return Complex la divicion"""
    def divide(self,b):
        if(b.real==0 and b.imag==0):
            raise ValueError("Denominador es 0")
            sys.exit()
        
        real = ((self.real*b.real)+(self.imag*b.imag))/(b.real**2+b.imag**2)
        imaginario = ((b.real*self.imag)-(self.real*b.imag))/(b.real**2+b.imag**2)
        return Complex((real),(imaginario))
    
    """# Este metodo devuelve la multiplicacion escalar este complejo y un real
    # @param b real
    # @return Complex la multiplicacion"""
    def sMultiply(self,c):
        real = self.real*c
        imaginario = self.imag*c
        return Complex((real),(imaginario))
    
    """# Este metodo devuelve  la divicion este complejo y un real
    # @param b real
    # @return Complex la divicion"""
    def sDivide(self,c):
        real = self.real/c
        imaginario = self.imag/c
        return Complex((real),(imaginario))
    
    """# Este metodo devuelve el conjugado de este complejo
    # @return Complex el conjugado"""
    def conjugado(self):
        return Complex(self.real,-(self.imag))
    
    """# Este metodo devuelve el modulo de este complejo
    # @return double e modulo"""
    def modulo(self):
        return (math.sqrt(self.real**2+self.imag**2))

    """# Este metodo devuelve el complejo en coordenadas polares
    # @return Complex el real es la fase del vector y el imaginario es el angulo  """
    def convert(self):
        long = (self.modulo())
        fase = (self.phase())
        return Complex((long),(fase))
    """# Este metodo devuelve la fase, el angulo, que se obtinene al pasar el complejo a coordenadas polares
    # @return double el angulo en radianes"""
    def phase(self): #angulo
        return (math.atan2(self.imag,self.real))
    
    """# Este metodo devuelve la inversa del complejo (-real, -imag)
    # @return Complex el inverso"""
    def inversa(self):
        return Complex(-1*self.real,-1*self.imag)
        

    """# Este metodo devuelve un booleano indicando si este complejo y otro dado son iguales
    # @param b Complex
    # @return  boolean son iguales o no"""
    @staticmethod
    def equals(self,b):
        if(-0.00001<abs(b.real-self.real)<0.00001 and -0.00001<abs(b.imag-self.imag)<0.000001):
            return True
        
        else:
            return False
    


    def print(self):
        print("[ "+str(self.real)+" , "+str(self.imag)+" ]")
    def printS(self):
        return ("[ "+str(self.real)+" , "+str(self.imag)+" ]")
        

        
