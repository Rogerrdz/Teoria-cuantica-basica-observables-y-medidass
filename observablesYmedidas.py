import math
from sys import stdin


def suma_i(a,b):
    """Suma dos numeros complejos, a y b de tipo array"""
    c = a[0] + b[0]
    d = a[1] + b[1]
    res = [c,d]
    return res

def resta_i(a,b):
    """Resta dos numeros complejos, a y b de tipo array"""
    c = a[0] - b[0]
    d = a[1] - b[1]
    res = [c,d]
    return res

def product_i(a,b):
    """Producto entre dos números complejos, a y b de tipo array"""
    c = a[0]*b[0] - a[1]*b[1]
    d = a[0]*b[1] + a[1]*b[0]
    res = [c,d]
    return res
#product_i([0,-1],[-1,-1]) #= [-1,1]

def div_i(a,b):
    """Cociente entre dos números complejos, a y b de tipo array"""
    c = a[0]*b[0] + a[1]*b[1]
    d = b[0]*a[1] - a[0]*b[1]
    e = b[0]**2 + b[1]**2
    if(e == 0):
        print("División entre cero es invalida")
    else:
        res = [round(c/e,5),round(d/e,5)]
    return res

def module_i(a):
    """Modulo de un numero complejo, a de tipo arreglo """
    x,y = a[0], a[1]
    c = x**2 + y **2     
    return c**0.5

def conjugado(a):
    """conjugado de un numero complejo, a de tipo array"""
    c = a[1] * -1
    return [a[0],c]

def conversionPolar_Cartesiana(num):
    """Convertir un numero complejo de forma polar a cartesiana r[0]=radio,r[1]=angulo """
    r = num[0]
    theta = num[1]*(math.pi/180)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return [round(x,5), round(y,5)]

def conversionCartesiana_Polar(num):
    """Convertir un numero complejo de forma cartesiana a polar num[0]= x,num[1]= y """
    r = math.sqrt(pow(num[0],2)+pow(num[1],2))
    alpha = abs((math.atan(num[1]/num[0]))*(180/math.pi))
    
    if(num[1]<0 and num[0]<0):
        alpha = 180 + alpha
    elif(num[1]<0 and num[0]>0):
        alpha = 360 - alpha
    elif(num[1]>0 and num[0]<0):
        alpha = 180 - alpha
    r = round(r,5)
    alpha = round(alpha)
    return [r,alpha]
    

def mostrar(n):
    """a es la parte real y b es la parte imaginaria
    muestra el numero complejo en forma a + bi ; n de tipo array """
    a = n[0]
    b = n[1]
    if b > 0:       
        print(a,'+',str(b)+'i')
    elif b == 0:
        print(a)
    elif b < 0:
        print(a,'-',str(abs(b))+'i')

def main1():
    c1 = [3,-1]
    c2 = [1,4]
    c3 = [2,120]
    c4 = [1,math.sqrt(3)]
    print("Sumar",c1,"y",c2,"-->" ,suma_i(c1,c2))
    print("Restar",c1,"y",c2,"-->" ,resta_i(c1,c2))
    print("Multiplicar",c1,"y",c2,"-->" ,product_i(c1,c2))
    print("Dividir",c1,"y",c2,"-->", div_i(c1,c2))
    print("Modulo de c1 --> ",round(module_i(c1),5))
    print("Modulo de c2 --> ",round(module_i(c2),5))
    print("Conjugado de c1 -->",conjugado(c1))
    print("Conjugado de c2 -->",conjugado(c2))
    print("De polar a cartesinas",conversionPolar_Cartesiana(c3))
    print("De cartesinas a polar",conversionCartesiana_Polar(c4))
    
main1()


   
    
    






            
