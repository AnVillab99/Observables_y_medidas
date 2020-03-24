import sys
import math
import Complex as com
import sympy as sp
import fractions
import matplotlib.pyplot as plt
class Matrix:
    def __init__(self,m):
        self.m= m # la matriz
        self.I=len(m) #imaginaro
        self.J=len(m[0])

    """# Este metodo devuelve la suma de esta matriz con la matriz dada
    # @param b Matrix otra matriz
    # @return Matrix la suma de las matrices"""
    def suma(self,b):

        if (self.I!= b.I or self.J != b.J):
            raise ValueError("Error en dimensiones de las matrices")
            sys.exit()

        r=[[com.Complex(0,0) for x in range (self.J)] for y in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                r[i][j]=self.m[i][j].suma(b.m[i][j])
        return Matrix(r)

    """# Este metodo devuelve la resta de esta matriz con la matriz dada
    # @param b Matrix otra matriz
    # @return Matrix la resta de las matrices"""
    def resta(self,b):
        if (self.I!= b.I or self.J != b.J):
            raise ValueError("Error en dimensiones de las matrices")
            sys.exit()
        r=[[com.Complex(0,0) for x in range (self.J)] for y in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                r[i][j]=self.m[i][j].resta(b.m[i][j])
        return Matrix(r)


    """# Este metodo devuelve la multiplicacion (producto cruz) de esta matriz o vector con la matriz o vector dado
    # @param b Matrix/vector otra matriz
    # @return Matrix la multiplicacion de las matrices"""
    def multiply(self,b):
        # if(self.J==1 and b.J==1 and self.I == b.I):
        #     print("1 columna")
        #     r =com.Complex(0,0)
        #     for i in range(self.I):
        #         for j in range(self.J):

        #             r=r.suma(self.m[i][j].multiply(b.m[i][j]))
        #     return r
        if(self.J == b.I):
            p = [[com.Complex(0,0) for i in range(b.J)] for j in range(self.I)]
            for i in range(self.I):
                for j in range(b.J):

                    sum=com.Complex(0,0)
                    for z in range(self.J):
                        
                        sum=sum.suma(self.m[i][z].multiply(b.m[z][j]))

                    p[i][j]=sum
            return Matrix(p)
        else:
            b.print()
            print("col A"+str(self.J))
            print("fil b"+str(b.I))
            raise ValueError("Error en dimensiones de las matrices")
            sys.exit()

    """ Devuelve el complejo que sale del producto interno"""
    def productoInterno(self,b):
        res = self.adjunta().multiply(b)
        return (res)

    """# Este metodo devuelve la matriz inversa de la matriz actual
    # @return matrix la inversa"""
    def inverse(self):
        p = [[com.Complex(0,0) for i in range(self.J)] for j in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                p[i][j] =self.m[i][j].inversa()
        return Matrix(p)

    """# Este metodo devuelve la transpuesta de la la matriz actual
    # @return matrix la transpuesta"""
    def transpuesta(self):
        p = [[com.Complex(0,0) for i in range(self.I)] for j in range(self.J)]
        for i in range(self.I):
            for j in range(self.J):
                p[j][i] =self.m[i][j]
        return Matrix(p)


    """# Este metodo devuelve la matriz conjugada de la matriz actual
    # @return MAtrix la conjugada"""
    def conjugada(self):
        p = [[com.Complex(0,0) for i in range(self.J)] for j in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                p[i][j] =self.m[i][j].conjugado()
        return Matrix(p)

    """# Este metodo devuelve la matriz adjunta (conjugda y transpuesta) de la matriz actual
    # @return MAtrix la adjunta"""
    def adjunta(self):
        return self.transpuesta().conjugada()

    """# Este metodo devuelve la traza de una matriz, la matriz debe ser cuadrada
    # @return Complex la traza de esta matriz"""
    def trace(self):
        if(self.I!=self.J):
            raise ValueError("Matriz no cuadrada")
        r=com.Complex(0,0)
        for i in range (self.I):
            r=r.suma(self.m[i][i])
        return r

    """# Este metodo devuelve la norma de esta matriz sqrt(Traza(At*A))
    # @return double la norma de la matriz"""
    def norma(self):
        c =self.adjunta()
        d = c.multiply(self)
        return (math.sqrt(d.trace().real))

    """# Este metodo devuelve la distancia entre 2 matrices
    # @return double la distancia entre las matrices"""
    def distancia(self,b):
        return (self.resta(b).norma())


    """# Este metodo devuelve un booleano indicando si esta matriz es unitaria (A*At=I)
    # @return boolean Indica si esta matriz es unitaria"""
    def unitaria(self):
        c = self.multiply(self.adjunta())
        for i in range (c.I):
            for j in range(c.J):
                if (i==j and (round(c.m[i][j].real,4)!=1.0000 or round(c.m[i][j].imag,4)!=0.0000 )):
                    return False
                elif(i!=j and (round(c.m[i][j].real,4)!=0.0000 or round(c.m[i][j].imag,4)!=0.0000)):
                    return False
        return True

    """# Este metodo devuelve un booleano indicando si esta matriz es hermetian (A=At)
    # @return boolean Indica si esta matriz es hermetian"""
    def hermetian(self):
        if(self.I!=self.J):
            return False
        d = self.adjunta()
        for i in range(self.I):
            for j in range(self.J):
                if ( self.m[i][j].real!= d.m[i][j].real or self.m[i][j].imag!= d.m[i][j].imag):
                    return False
        return True

    """multiplicacion escalar de la matriz con un real"""
    def multiplyS(self,d):
        k = [[com.Complex(0,0) for i in range(self.J)] for j in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                k[i][j]=self.m[i][j].sMultiply(d)
        return Matrix(k)

    """multiplicacion escalar con un complejo"""
    def escalarMultiply(self,c):
        k = [[com.Complex(0,0) for i in range(self.J)] for j in range(self.I)]
        for i in range(self.I):
            for j in range(self.J):
                k[i][j]=self.m[i][j].multiply(c)
        return Matrix(k)

    """# Este metodo devuelve el producto tensor entre 2 matrices
    # @param la otra matriz
    # @return Matrix el producto tensor"""
    def productoTensor(self,b):
        I2 = b.I
        J2 = b.J
        tpc =  [[com.Complex(0,0) for i in range(self.J*J2)] for j in range(self.I*I2)]
        g=0
        h=0
        for i in range(self.I):
            for j in range(self.J):
                r = b.escalarMultiply(self.m[i][j])
                tpc=self.llenar(tpc,r,g,h)
                h+=1
            h=0
            g+=1
        return Matrix(tpc)

    #filler es matriz, og no
    def llenar(self,og,filler,vecesI,vecesJ):
        iF = filler.I;
        jF = filler.J;
        inicialI = iF*vecesI; #la fila desde donde se comenzara a llenar la og
        inicialJ = jF*vecesJ; # la columna desde donde se comenzara a llenar la og
        itI =0;
        itJ =0;
        for a in range(inicialI,inicialI+iF):
            for b in range(inicialJ,inicialJ+jF):
                og[a][b]=filler.m[itI][itJ]
                itJ=itJ+1
            itJ=0
            itI=itI+1
        return og



    """Este metodo devuelve los vectores propios de la matriz como una lista de Matrices""" 
    def vectoresPropios(self):
        sustituto  = [[0 for i in range(self.J)] for j in range(self.I)]
        for a in range(self.I):
            for b in range(self.J):
                sustituto[a][b] = self.m[a][b].real + self.m[a][b].imag*1j
        sus = sp.Matrix(sustituto)
        eigen=sus.eigenvects()
        result = [Matrix([[]]) for i in range(len(eigen))]    
        for i in range(len(eigen)):
            eigenV = eigen[i][2]
            #sigue cada uno de los eigenvector
            eV = [[com.Complex(0,0)] for j in range (len(eigenV[0]))]
            for v in range(len(eigenV)):
                #rows
                for god in range(len(eigenV[v])):
                    #los valores 
                    VRow = eigenV[v][god]
                    eV[god][0]=com.Complex(sp.re(VRow),sp.im(VRow))
            
            result[i]=Matrix(eV)
        return (result)
    """Este metodo devuelve los valores propios complejos de la matriz en forma de lista de comlpejos"""
    def valoresPropios(self):
        sustituto  = [[0 for i in range(self.J)] for j in range(self.I)]
        for a in range(self.I):
            for b in range(self.J):
                sustituto[a][b] = self.m[a][b].real + self.m[a][b].imag*1j
        sus = sp.Matrix(sustituto)
        eigen=sus.eigenvals()
        result = []
        for key,value in eigen.items():
            for veces in range(value):
                result.append(com.Complex(sp.re(key),sp.im(key)))
        return (result)
    def print(self):
        s = ""
        for i in range(0,self.I):
            for j in range(0,self.J):
                s+=self.m[i][j].printS()
            print(s)
            s=""
    """Print con fraciones"""
    def printF(self):
        s = ""
        for i in range(0,self.I):
            for j in range(0,self.J):
                r = com.Complex(fractions.Fraction.from_float((self.m[i][j].real)).limit_denominator(),fractions.Fraction.from_float((self.m[i][j].imag)).limit_denominator())
                s+=r.printS()
            print(s)
            s=""
    def equals(self,b):
        if (self.I!= b.I or self.J != b.J):
            raise ValueError("Matriz dada es de dimensiones erradas")
            sys.exit()
        for i in range(self.I):
            for j in range(self.J):
                if(not (self.m[i][j].equals(self.m[i][j],b.m[i][j]))):
                    return False
                    sys.exit()
        return True
    def fix(self,i,j,c):
        self.m[i][j] = c
    
    def booleanPrint(self):
        s = ""
        for i in range(0,self.I):
            for j in range(0,self.J):
                r=self.m[i][j].real
                s+=r.printS()
            print(s)
            s=""
    
    """Redondea los complejos de la matriz a N decimales (N param)"""
    def round(self,n):
        k=self.m
        for i in range(self.I):
            for j in range(self.J):
                og = self.m[i][j]
                k[i][j]=com.Complex(round(og.real,n),round(og.imag,n))
        return Matrix(k)

    """Se da un vector con complex y se devulve el vector de probabilidades que representan"""
    def prob(self):
        k=self.m
        for i in range(self.I):
            for j in range(self.J):
                k[i][j] = com.Complex(math.pow(self.m[i][j].modulo(),2),0)
        return Matrix(k)
    
    """Normaliza la matriz"""
    def normalize(self):
        sumatoria = 0
        for i in range(self.I):
            for j in range(self.J):
                sumatoria=sumatoria+(math.pow(self.m[i][j].modulo(),2))
        sumatoria = math.sqrt(sumatoria)
        k = self.m
        for i in range(self.I):
            for j in range(self.J):
                k[i][j] = self.m[i][j].sDivide(sumatoria)
        return Matrix(k)
    def sumaInterna(self):
        sum=0
        for i in range(self.I):
            for j in range(self.J):
                sum=sum+self.m[i][j].modulo()
        return sum





"""-------------------------------------------------------------------------"""
""" Este metodo compara si los eigenvectores dados son iguales, no importa el orden"""
def equalsEigenV(a,b):
        usados =[]
        for c in a:
            esta =False
            est=0
            for i in range(len(b)):
                if(c.equals(c,b[i]) and (not i in usados) and est ==0):
                    usados.append(i)
                    esta=True
                    est=1
            if(esta==False):
                return False
        return True
"""Este metodo recibe el num de fils, columans y un array de enteros para crear una matriz"""
def crear(I,J,v):
    if(not (len(v)==I*J)):
        print(len(v))
        print(I*J)
        return "dimesiones y valores errados"
    
    valores  = [[com.Complex(0,0) for i in range(J)] for j in range(I)]
    a=0
    for i in range(I):
        for j in range(J):
            valores[i][j]=com.Complex(v[a],0)
            a=a+1
    return Matrix(valores)


"""Acepta como entrada de [] tuplas de numeros representado real e imaginario de un complejo"""
def crearR(I,J,v):
    if(not (len(v)==I*J)):
        print(len(v))
        print(I*J)
        return "dimesiones y valores errados"
    
    valores  = [[com.Complex(0,0) for i in range(J)] for j in range(I)]
    a=0
    for i in range(I):
        for j in range(J):
            valores[i][j]=com.Complex(v[a][0],v[a][1])
            a=a+1
    return Matrix(valores)

"""Multiplica la matriz m, x veces (m,x)""" 
def multiplicar(m,veces):
    J = m
    for i in range(veces):
        m=m.multiply(J)
    return m
"""Crea arreglo con 0's de tamaño I,J"""
def empty(I,J):
    valores  = [[com.Complex(0,0) for j in range(J)] for i in range(I)]
    return Matrix(valores)

""" Recibe un 2 enteros (filas y columnas) y un arreglo de booleanos (True=1, False=0)"""
def booleanMatrix(I,J,c):
    valores  = [[com.Complex(0,0) for j in range(J)] for i in range(I)]
    a=0
    for i in range(I):
        for j in range(J):
            if(type(c[a]) is bool):
                valores[i][j]=com.Complex(c[a],0)
            else:
                v=False
                if(c[a] == "T" or c[a]=="t"):
                    v=True
                valores[i][j]=com.Complex(v,0)
            a=a+1
    return Matrix(valores)


"""Muestra grafico del vector dado (solo vector no matriz)"""
def printVector(v):     

    objects=[]
    data=[]
    k=0
    for i in range(v.I):
        objects.append(k)
        data.append(v.m[i][0].real)
        k=k+1
    plt.bar(objects, data, align='center', alpha=0.5)
    plt.xticks(objects, objects)
    plt.ylabel('Probability')
    plt.xlabel("Vector position")
    plt.title('Position probability')

    plt.show()

def identidad(g):
    iden = empty(g,g)
    a=0
    for i in range(g):
        iden.fix(i,i,com.Complex(1,0))
    return iden







    
