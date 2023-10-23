import complexOperation as co
import math
##==========================SEGUNDA_PARTE_VECTORES_y_MATRICES======================

def generateEmptyMatrix(n,m):
    '''Genera una matriz de tamaño nxm con numeros complejos de ceros'''
    colum = []
    for i in range(n):
        fil = []
        for j in range(m):
            fil.append([0,0])
        colum.append(fil)
    return (colum)
#generateEmptyMatrix(3,3)

def generaridentidad(n):
    """Genera una matriz identidad(compuesta de numeros complejos) de tamaño n"""
    ma = []
    for i in range(n):
        l = []
        for j in range(n):
            if i == j:
                l.append([1,0])
            else:
                l.append([0,0])
        ma.append(l)
    return ( ma)
#generaridentidad(3)
        
def sumaVectoresComplejos(a,b):
    """Metodo q suma dos vectores complejos; a y b de tipo array"""
    if(len(a) == len(b)):
        vecRes = []
        for i in range(len(a)):
            res = co.suma_i(a[i],b[i])
            vecRes.append(res)
        return ( vecRes )
            
    else:
        print("Los vectores deben tener la misma longitud")

def inversoAditivo(a):
    """Retorna el inverso aditico de un numero complejo; a= complejo tipo Array"""
    res = [ a[0]*-1,a[1]*-1 ]
    return( res )
        
def real_x_complejo(n,a):
    """Metodo q multiplica un número real por un número complejo; n= Real, a= Complejo tipo Array
        retorna un complejo tipo Array"""    
    c = [n*a[0],n*a[1]]
    return c

def productoVectoresComplejos(vec1,vec2):
    '''retorna un numero complejo siendo el producto entre dos arreglso complejos'''
    res = [0,0]
    if(len(vec1)== len(vec2)):
        for i in range(len(vec1)):
            res = co.suma_i(res,co.product_i(vec1[i],vec2[i]))
    else:
       print("Longitudes de vecetores no son validas")
    return(res)

def producto_deEscalar_porVectorComplejo(n,a):
    """Metodo que multiplica un escalar por un vector complejo; n= escalar, a= vector complejo"""
    vecRes = []
    for i in range(len(a)):
        vecRes.append(real_x_complejo(n,a[i]))
    return (vecRes)

def sumaMatricesComplejas(matrizA,matrizB):
    """metodo q retorna la suma entre dos matrices"""
    matRes = []
    for i in range( len(matrizA) ):
        fila = []
        for j in range( len(matrizA[i]) ):            
            c = co.suma_i(matrizA[i][j], matrizB[i][j])
            fila.append(c)
        matRes.append( fila )
    return(matRes)

def restaMatriz(matriz1,matriz2):
    """Recibe dos matrices o vectores y los resta, estos deben tener
    el mismo tamaño m x n y deben contener arreglos"""
    res = generateEmptyMatrix(len(matriz1),len(matriz1[0]))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            res[i][j] = co.resta_i(matriz1[i][j],matriz2[i][j])
    return res

def inversoAditivoMatriz(matriz):
    """Recibe una matriz o un vector y halla el inverso aditiva de este(a)"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = inversoAditivo(matriz[i][j])
    return ( matriz)

def escalarXmatrizCompl(e,matriz):
    '''Retorna una matriz multiplicada por un escalar; e= int; matriz= array[array]'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = real_x_complejo(e,matriz[i][j])
    return(matriz)

def transpuestaMatriz(matriz):
    '''Retorna la transpuesta de una matriz ingresada'''
    ret = generateEmptyMatrix(len(matriz),len(matriz[0]))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            ret[i][j] = matriz[j][i]
    return (ret)

def conjugadoVector(vector):
    '''Retorna el vector conjugado'''
    v = []
    for i in vector:
        v.append(co.conjugado(i))
    return (v)

def conjugadaMatriz(matriz):
    '''Retorna la matriz conjugada de una ingresada'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = co.conjugado(matriz[i][j])

    return (matriz)

def adjuntaMatriz(matriz):
    '''Halla la adjunta de una matriz calculando la conjugada y luego la transpuesta'''
    ret = transpuestaMatriz(conjugadaMatriz(matriz))
    return( ret )

def multiplicarMatrices(matrizA,matrizB):
    '''Retorna la multiplicación entre matrices'''
    if len(matrizA[0]) == len(matrizB):
        ret = generateEmptyMatrix(len(matrizA), len(matrizB[0]))
        #ret = [0,0]
        for i in range(len(matrizA)):
            for j in range(len(matrizB[0])):
                ret[i][j] = [0,0]
                for k in range(len(matrizA[0])):
                    ret[i][j] = co.suma_i(ret[i][j], co.product_i(matrizA[i][k],matrizB[k][j]))
        if len(ret) == 1:
            return (ret[i][j])
        return ( ret)
    else:
        return( 0)

def productinterno(vector1,vector2):
    """Halla el producto interno de dos vectores compuesto de complejos"""
    daga = adjuntaMatriz(vector1)
    res = multiplicarMatrices(daga,vector2)
    if res[1] == 0:
        return res[0]
    return res

def normavector(vector1):
    """Halla la norma de un vector compuesto de complejos"""
    ret = productinterno(vector1,vector1)
    ret = ret ** 0.5
    return ret

def distanciavectores(vector1,vector2):
    """Halla la distancia entre dos vectores compuesto de complejos"""
    resta = restaMatriz(vector1,vector2)
    res = normavector(resta)
    return res

def truncar(matriz):
    """Trunca los valores reales en la matriz, sean de la parte real o de la
    parte imaginaria"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(2):
                matriz[i][j][k] = math.ceil(matriz[i][j][k])
    return matriz

def matrizUnitaria(matriz):
    """Comprueba si una matriz es unitaria"""
    daga = adjuntaMatriz(matriz)
    res = multiplicarMatrices(matriz,daga)
    res = truncar(res)
    identidad = generaridentidad(len(matriz))
    if res == identidad:
        return True
    return False

def matrizhermitiana(matriz):
    """Comprueba si una matriz es hermitiana"""    
    if adjuntaMatriz(matriz) == matriz:
        return True
    return False

def productotensor(matriz1,matriz2):
    """Halla el producto tensor de dos matrices compuestas de complejos"""
    res = generateEmptyMatrix(len(matriz1)*len(matriz2),len(matriz1[0])*len(matriz2[0]))
    m = len(matriz2)
    n = len(matriz2[0])
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j] = producto_i(matriz1[i//m][j//n],matriz2[i%m][j%n])
    return res

def moduleKet(ket):
    '''Retorna la longitud del ket o el modulo '''
    s = 0
    for stateBase in ket:
        s += math.pow(co.module_i(stateBase),2)
    s = round( math.sqrt(s),5)
    return (s)
    
def normalizeket(ket):
    '''Retorna el vector(ket) normalizado |Y>/||Y>| '''
    if(moduleKet(ket) != 1):
        normalKet = []
        for stateBase in ket:
            normalKet.append(co.div_i(stateBase,[moduleKet(ket),0]))
        return (normalKet)
    else:
        return (ket)


def braket(ket):
    '''Retorna el Bra del estado ket (ket->array de complejos)'''
    bra = conjugadoVector(ket)
    return (bra)

def main():
    print("Suma de vectores: ",sumaVectoresComplejos([[3,2],[4,1]],[[1,3],[2,-5]]))
    print("Inverso aditivo de un comlejo",inversoAditivo([3,2]))
    print("Producto entre real y complejo",real_x_complejo(3,[3,2]))
    print("Producto entre dos vectores complejos",productoVectoresComplejos([[3,0],[-6,0],[2,0]],[[3,0],[-6,0],[2,0]]))
    print()
    print("Multiplicar escalar por vector complejo",producto_deEscalar_porVectorComplejo(3,[[3,2],[4,1]]))
    print("Multiplicar escalar por vector complejo",producto_deEscalar_porVectorComplejo(math.sqrt(2)/2,[[0,1],[-1,0]]))
    print()
    print("Suma de matrices complejas",sumaMatricesComplejas([ [[3,2],[4,1]],[[1,3],[2,5]] ], [ [[3,2],[4,1]],[[1,3],[2,5]] ]))
    print("Inverso aditivo de una matriz",inversoAditivoMatriz([[[3,4],[1,2]],[[3,6],[7,6]]]))
    print("Producto de un escalar a una matriz compleja",escalarXmatrizCompl(2,[[[3,4],[1,2]],[[3,6],[7,6]]]))

    print("Transpueste de una matriz",transpuestaMatriz([[[3,4],[1,2]],[[3,6],[7,6]]]))
    print("Conjugado de un vector",conjugadoVector([[3,0],[1,-2]]))
    print("Matriz conjugada",conjugadaMatriz([[[3,-4],[1,2]],[[3,6],[-7,-6]],[[8,-9],[9,2]]]))
    print("Adjunta de una matriz",adjuntaMatriz([[[3,4],[1,2]],[[3,6],[7,6]]]))
    print()
    print("Producto entre matrices ",multiplicarMatrices([[[4,0],[3,0]],[[1,0],[2,0]]], [[[2,0]],[[3,0]]]))
    print("Producto entre matrices complejas",multiplicarMatrices([[[2,0],[3,0],[4,0]],[[3,0],[4,0],[2,0]],[[2,0],[5,0],[6,0]]],[[[1,0],[5,0],[4,0]],[[2,0],[6,0],[7,0]],[[7,0],[8,0],[3,0]]]))
    print()
    print("Modulo o longitud de un estado Ket",moduleKet([[3,-4],[7,2]]))
    print("Modulo o longitud de un estado Ket",moduleKet([[math.sqrt(2)/2,math.sqrt(2)/2],[math.sqrt(2)/2,-math.sqrt(2)/2]]))
    print()
    print("Retorna estado Ket normalizado",normalizeket([[2,-3],[1,2]]))
    print()
    print("Bra de un stado",braket([[3,1]]))
    print("Bra de un stado",braket([[-1,-4],[2,-3],[-7,6],[-1,1],[-5,-3],[5,0],[5,8],[4,-4],[8,-7],[2,-7]]))

#main()