# Teoría cuántica básica, observables y medidas 
Este proyecto presenta una simulación de algunos ejercicios sobre teoría cuantica básica planteados en el libro "Quantum Computing for Computer Scientists"
* SIMULACIÓN PRIMER SISTEMA CUÁNTICO DESCRITO EN LA SECCIÓN 4 
* RETOS DE PROGRAMACIÓN DEL CAPÍTULO 4
* OTROS PROBLEMAS
# Simulación primer sistema cuantico 
El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

+ 1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
  * Persentamos un modelo de algoritmo en python que simula una solución al problema, en donde el parámetro de entrada "p" representa la posición en donde se desea conocer la probabilidad de hallar la particula y el parámetro "ket" representa un vector de estado inicial 
  
#### Python
```python
def probParticleInLine(p,ket):
    '''Probabilidad de encontrar una particula en el estado base p dentro de ket 'ket'
        p = posicion en el ket, ket = array de complejos o estados bases'''
    s = 0    
    for i in range( len(ket)):
        s += (co.module_i(ket[i]))**2
    s = math.sqrt(s);
    prob = co.module_i(ket[p])**2 / s**2
    
    return (round(prob*100,5))
```
### Test 1
Input:
- Dado el estado Ket, |Y> = [-3+i, -2i, i, 2]. Calcular la probabilidad de encontrar la particula en le posición 2
OutPut:
- Ingresamos datos al algoritmo de tal fomra que entienda números complejos. 
  * p = 2 y ket = [[-3,-1],[0,-2],[0,1],[2,0]]
  * R/: la probabilidad de encontrar la particula en la posición 2 es de : 5.26316 %

### Test 2
Input:
- Dado el estado Ket, |Y> = [2+i, -1,2i, i, 1, 3-i, 2, -2i, -2+i, 1-3i, -i]. Calcular la probabilidad de encontrar la particula en le posición 7
OutPut:
- Ingresamos datos al algoritmo de tal fomra que entienda números complejos. 
  * p = 7 y ket =[[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]]
  * R/: la probabilidad de encontrar la particula en la posición 7 es de : 10.86957 %
  * 
  
2. Dados dos vectores Ket1 y ket2 debe buscar la probabilidad de transitar del primer vector al segundo.
-  Modelo de algoritmo en python que simula una solución al problema, parámetros un ket "desde" y un ket "hasta"
```python

def probTransition(ket1, ket2):
    '''Retorna la probabilidad de ir del estado ket1 al estado ket2 (kets arrays)'''
    bra = co.braket(ket2) 
    ret = co.productoVectoresComplejos(bra, ket1)
    print(ret)

```
```python
def braket(ket):
    '''Retorna el Bra del estado ket (ket->array de complejos)'''
    bra = conjugadoVector(ket)
    return (bra)
def productoVectoresComplejos(vec1,vec2):
    '''retorna un numero complejo siendo el producto entre dos arreglso complejos'''
    res = [0,0]
    if(len(vec1)== len(vec2)):
        for i in range(len(vec1)):
            res = suma_i(res,product_i(vec1[i],vec2[i]))
    else:
       print("Longitudes de vecetores no son validas")
    return(res)
 ```
 ### Test
 Input:
 - Dados los vectores ket1 = [2+i,-1+2i, i, 1, 3-i, 2, -i, -2+i, 1-3i, -i ] y ket2 = [-1-4i, 2-3i, -7+6i, -1+i, -5-3i, 5, 5+8i, 4-4i, 8-7i, 2-7i]
OutPut:
- Ingresamos los valores ket1 =  [[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]] y ket2 = [[-1,-4],[2,-3],[-7,6],[-1,1],[-5,-3],[5,0],[5,8],[4,-4],[8,-7],[2,-7]]
* R/ la probabilidad de pasar del ket1 al ket2 es de -3+4i aproximadamente
# Retos de programación 
 Sistema de la posición de la partícula en una recta.
 - 1. Usuario especifica el número de puntos posibles y un vector ket y el sistema calcula las probabilidades de encontrar partícula en una posición.
    * Persentamos un modelo de algoritmo en python que simula una solución al problema, "ps" es una lista de posiciones que se desea conocer la probabilidad de encontrar una particulo , ket estado inicial . 
 ```python
    def probParticulasEnLinea(ps,ket):
      for state in ps:
        print(state,"->",probParticleInLine(state,ket))
 ```
 
 ### Test
 - Input:
   * Dadas un lista de posiciones ps = [0,4,6,7]
   * Dado el Ket = [2+i,-1+2i, i, 1, 3-i, 2, -i, -2+i, 1-3i, -i ]
 - Output:
   * Ingresamos los datos ps y el ket. Obtenemos las siguientes probabilidades:
   * Estado  0 -> 10.86957 %
      Estado  4 -> 21.73913 %
      Estado  6 -> 8.69565 %
      Estado  7 -> 10.86957 %
- 2. Dada una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.
  * Modelado de la solución 
 ```python
 def problema2(observable,ket):
    if(co.matrizhermitiana(observable)):
        print("La media o valor esperado e: ", valorEsperado(observable,ket))
        print("La varianza es: ", varianza(observable,ket))
    else:
        print("La matriz no es Hermitiana")
 ```
  ```python
 def valorEsperado(matriz,ket):
    valor = [0,0]
    ketModule = []
    for state in ket:
        ketModule.append([[pow(co.module_i(state),2),0]])
    
    produMatriz = co.multiplicarMatrices(matriz,ketModule)
    
    for i in produMatriz:
        valor = co.suma_i(valor,i[0])
    return (valor[0])    

def deltha(observable,valorEsperado):
    '''retorna el deltha Y, observable = matriz hermitania , valorEsperado = real'''
    matIdentidad = co.generaidentidad(len(observable))
    matUni = co.escalarXmatrizCompl(valorEsperado,matIdentidad)
    deltha = co.restaMatriz(observable,matUni)
    return(deltha)

def varianza(deltha,stateKet):
    '''Retorna la varianza de un observable y su estado dado; observable = matriz, deltha = arrayEstado inicial'''
    delthaInt = co.multiplicarMatrices(deltha,deltha)
    ret = valorEsperado(delthaInt,stateKet)
    return(ret)
 ```
 ### Test
 - Input:
   * Dada la matriz hermitania O = [[0,-i],[i,0]]
   * Dado el ket = [1/sqrt(2), (1/sqrt(2))i]
 - OutPut:
   * La media o valor esperado es:  0.0
   * La varianza es:  0.9999999999999998
# Otros problemas
# Referencias 📝
- Ejercicion tomados del texto guia "Quantum Computing for Computer Scient
