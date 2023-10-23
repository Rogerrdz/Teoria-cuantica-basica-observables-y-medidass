import complexOperation as co
import math

def probParticleInLine(p,ket):
    '''Probabilidad de encontrar una particula en el estado base p dentro de ket 'ket'
        p = posicion en el ket, ket = array de complejos o estados bases'''
    s = 0    
    for i in range( len(ket)):
        s += (co.module_i(ket[i]))**2
    s = math.sqrt(s);
    prob = co.module_i(ket[p])**2 / s**2
    return (round(prob*100,5))
    
    #print(prob)

##probParticleInLine(2,[[-3,-1],[0,-2],[0,1],[2,0]])
##probParticleInLine(7,[[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]])

def probTransition(ket1, ket2):
    '''Retorna la probabilidad de ir del estado ket1 al estado ket2 (kets arrays)'''
    fromKet = co.normalizeket(ket1)
    toKet = co.normalizeket(ket2)
    bra = co.braket(toKet)
    bra = co.braket(ket2) 
    ret = co.productoVectoresComplejos(bra, fromKet)
    #ret = co.productoVectoresComplejos(bra, ket1)
    print(ret)

##probTransition([[1,0],[0,-1]],[[0,1],[1,0]])
##probTransition(
##[[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]]
##,
##[[-1,-4],[2,-3],[-7,6],[-1,1],[-5,-3],[5,0],[5,8],[4,-4],[8,-7],[2,-7]]
##)
##probTransition(
##[[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
##,
##[[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
##)
def probParticulasEnLinea(ps,ket):
    for state in ps:
        print("Estado ",state,"->",probParticleInLine(state,ket),"%")

#probParticulasEnLinea([0,4,6,7],[[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]])
    
#==========OBSERVABLES====================

def valorEsperado(matriz,ket):
    valor = [0,0]
    ketModule = []
    for state in ket:
        ketModule.append([[pow(co.module_i(state),2),0]])
    
    produMatriz = co.multiplicarMatrices(matriz,ketModule)
    
    for i in produMatriz:
        valor = co.suma_i(valor,i[0])
    return (valor[0])
    #print(co.matrizhermitiana(matriz))

#valorEsperado([[[0,0],[0,-1]],[[0,1],[0,0]]] ,[[1/math.sqrt(2),0],[0,1/math.sqrt(2)]])
#valorEsperado([[[1,0],[0,0]],[[0,0],[1,0]]] ,[[math.sqrt(2)/2,0],[math.sqrt(2)/2,0]])    

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

#varianza([[[0,0],[0,-1]],[[0,1],[0,0]]] ,[[1/math.sqrt(2),0],[0,1/math.sqrt(2)]])


def problema2(observable,ket):

    #if(co.matrizhermitiana(observable)):
        print("La media o valor esperado es: ", valorEsperado(observable,ket))
        print("La varianza es: ", varianza(observable,ket))
    #else:
        #print("La matriz no es Hermitiana")


#problema2([[[0,0],[0,-1]],[[0,1],[0,0]]] ,[[1/math.sqrt(2),0],[0,1/math.sqrt(2)]])










    