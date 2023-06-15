def saludo():
    print("hola")

def saludo2(nombre):
    print("hola ",nombre)

def calcularEdad(añoNac,añoActual):
    edad = añoActual - añoNac
    print("Su edad es ",edad," años pp")

def sumar(num1,num2):
    suma = num1 + num2
    return suma

def saludo2(vecino):
    return vecino
    
def calcularIVA(variablePrecio):
    variableIva = variablePrecio * 0.19
    return variableIva

def calculoDescuento(precio,descuento):
    total = precio - (precio * descuento/100)
    return total

def calcularIMC(peso,estatura):
    imc = peso /estatura**2
    if imc < 18.5:
        print("Bajo peso")
    else:
        if imc >= 18.5 and imc < 24.9:
            print("Adecuado")
        else:
            if imc >=25 and imc <= 29.9:
                print("Sobrepeso")
            else:
                if imc >=30 and imc <= 34.9:
                    print("Obesidad grado 1")
                else:
                    if imc >=35 and imc <=39.9:
                        print("Obesidad grado 2")
                    else:
                        if imc >40:
                            print("Obesidad grado 3")
