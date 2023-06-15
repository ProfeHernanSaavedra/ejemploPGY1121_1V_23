import funciones as fn

op = 0
while op != 4:
    print("1. Calcular IVA")
    print("2. Calcular Descuento")
    print("3. Calcular IMC")
    print("4. Salir")
    op = int(input("Ingrese su opción: "))
    
    if op == 1 :
        precio = int(input("Ingrese precio: "))
        iva = fn.calcularIVA(precio)
        print("El IVA del producto es: ",iva)
    else:
        if op == 2:
            precio = int(input("Ingrese precio: "))
            descuento = float(input("Ingrese tasa de descuento: "))
            total = fn.calculoDescuento(precio,descuento)
            print("El total del producto con descuento es: ",total)
        else:
            if op == 3:
                peso = int(input("Ingrese su peso: "))
                estatura = float(input("Ingrese su estatura: "))
                fn.calcularIMC(peso,estatura)
                

