# CNYT-Libreria-Complejos 
## Libreia complejos
Esta libreria consiste de una implementación propia de los numeros complejos, y matrices de nuemros complejos con sus respectivas operaciones.
Para usar vectores creelos como una matriz nx1 o 1xn y aplique transpuesta.


## Complejos
Los numeros complejos consisten de 2 numeros reales, uno representa la parte real y otro la imaginaria.
Estos complejos estan implementados como 2 reales que representan la aprte real y la imaginaria.
En esta libreria los complejos cuentan con las siguientes operaciones: 
 - sumar
 - restar
 - multiplicar
 - dividir
 - conversion a polar
 - fase
 - modulo
 - inversion
 - multiplicacion y division escalar

## Matriz/Vector de complejos
Las matrices de complejos (o los vectoresque son matrices nx1) son matrices cuyas entradas son numeros complejos de esta libreria. Estas matrices pueden realizar las operaciones corrientes de las matrices con las operaciones internas alteradas para usar las operacion de los complejos implementadas en esta libreria.
En esta libreria las matrices cuentan con las siguientes operaciones: 
 - sumar
 - restar
 - multiplicacion entre matrices
 - inversa
 - transpuesta
 - conjugada
 - adjunta
 - traza
 - norma
 - distancia
 - verificacion si es unitaria
 - verificacion si es hermitiana
 - multiplicacion escalar
 - producto tensor
 - Vectores Propios
 - Valores Propios
 - Comparacion de valores propios
## De lo clasico a lo cuantico
La libreria tambien permite usar funciones para realizar simulaciones cuanticas en un computador clasico, estas funciones son:
 - Cambio en base a click de tiempo
 - Creacion de matrices con valores booleanos
 - Imprimir vector resultado como grafica
## Uso de libreria
Para correr esta libreria se necesita tener instalado python 3.8, numpy, SymPy, Scipy, matplotlib

Para instalar python se va a la pagina princiapl de python 
> https://www.python.org/downloads/
Y se descarga la version especificada

luego se clona la libreria de github:
>https://github.com/AnVillab99/ComplexPy

Dentro del repositorio clonado se debe ejecutar los comandos:

> pip install sympy
<br>

> python -m pip install numpy
<br>


> python -m pip install scipy

<br>

> python -m pip install matplotlib


Para ejecutar se emplea el IDLE de python, o IDE de eleccion y se ejecuta: 

>py parteDeLalibreiaAEjecutar.py


## Pruebas
Para ejecutar las pruebas se necesita dirigir al directorio src y en comando ejecutar:

> py MatrixTest.py
![testMatrices](https://github.com/AnVillab99/ComplexPy/blob/master/resources/images/testMatriz.PNG)
<br>

>py ComplexTest.py
![testComplejos](https://github.com/AnVillab99/ComplexPy/blob/master/resources/images/testComplejos.PNG)
<br>

>py LeapTests.py
![testLeap](https://github.com/AnVillab99/ComplexPy/blob/master/resources/images/leapTest.PNG)

> grafica
![graph](https://github.com/AnVillab99/ComplexPy/blob/master/resources/images/graph.PNG)


## Built With

* [Python](https://maven.apache.org/) - Language
* [SymPy](https://www.sympy.org/en/index.html) - Library

## Versioning

For the versions available, see the [tags on this repository](https://github.com/AnVillab99/ComplexPy). 

## Authors

* **Andres Villamil**  [AnVillab99](https://github.com/AnVillab99)


## License

This project is under GNU General Public License - see [LICENSE](https://github.com/AnVillab99/AREP-Lab1/blob/master/LICENSE) to more info.

## Acknowledgments

* StackOverflow

