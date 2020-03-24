import sys
import math
import Complex as com
import sympy as sp
import fractions
import matplotlib.pyplot as plt
import Matrix as m

"""Dado un ket (vector) v, cual es la probabilidad de hallar una particula en i"""
def probParticle(v,p):
    ket = v.m
    sumatoria = 0
    for i in range(v.I):
        for j in range(v.J):
            sumatoria=sumatoria+(math.pow(ket[i][j].modulo(),2))
    
    if (v.I ==1):
        posc = math.pow(ket[0][p].modulo(),2)
    if (v.J ==1):
        posc = math.pow(ket[p][0].modulo(),2)
    return posc/sumatoria

def amplitudDeTransicion(a,b):
    a = a.normalize()
    b = b.normalize()
    r =b.productoInterno(a).m[0][0]
    d = a.norma()*b.norma()
    return r.sDivide(d)

def identidadEsperada(I,es):
    ide = m.identidad(I)
    for i in range(I):
        ide.m[i][i]=ide.m[i][i].multiply(es)
    return ide

"""Valor esperado al observar el vecotr v, con el observable o """
def vEsperado(v,o):
    if (o.hermetian()):
        v3m= o.multiply(v)
        vEsperado=v3m.productoInterno(v) #media
        return vEsperado.m[0][0].modulo()
    else:
        raise ValueError("matriz no es hermetiana")
        sys.exit()

def media(v,o):
    return vEsperado(v,o)

def varianza(v,o):
    media = vEsperado(v,o)
    identidadMedia = identidadEsperada(o.I,media)
    
    delta = o.resta(identidadMedia)
    dfo=delta.multiply(delta)
    varIzq = dfo.multiply(v)
    var =varIzq.productoInterno(v)
    return var.m[0][0].modulo()


