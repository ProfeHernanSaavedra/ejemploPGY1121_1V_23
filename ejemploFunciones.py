import funciones as fn

#programa principal
fn.saludo()
nom = input("Ingrese su nombre: ")
fn.saludo2("Maria")
fn.saludo2(nom)
aActual = 2023
aNac = int(input("Ingrse su año de nacimiento: "))
fn.calcularEdad(aNac,aActual)

print("probando print")

print("probando print y pull")

print("sumando.....")
sumaT = fn.sumar(3,2)
print(sumaT)

print(fn.saludo2("pedro"))


