#cadena de caracteres preformateado(respeta las lineas)
#codigo repetido, (Don't repeat yourself) condigo sin funciones
menu= """
Bienvenido al conversor de moneda ❤


1- pesos colombianos
2- pesos argentinos
3- pesos mexicanos

elige una opcion
 """
 # una vez que haya codigo en los bloques se puede quitar el pass
opcion =int(input(menu))
if opcion == 1:
    #bloque de codigo 1
    colombian_pesos = input("¿Cuantos pesos colombianos tienes?")
    colombian_pesos =  float(colombian_pesos)
    valor_dolar=3875
    dolares = colombian_pesos/valor_dolar
    dolares = round(dolares, 2)#funcion para redondear los decimales (el numero flotanto, cuantos decimales tener)
    dolares = str(dolares)
    print("Tienes $"+ dolares +" dolares")
    
elif opcion ==2:
    #bloque de codigo 1
    pesos_argentinos = input("¿Cuantos pesos argentinos tienes?")
    pesos_argentinos =  float(pesos_argentinos)
    valor_dolar=65
    dolares = pesos_argentinos/valor_dolar
    dolares = round(dolares, 2)#funcion para redondear los decimales (el numero flotanto, cuantos decimales tener)
    dolares = str(dolares)
    print("Tienes $"+ dolares +" dolares")
    
elif opcion==3:
    #bloque de codigo 1
    pesos_mexicanos = input("¿Cuantos pesos mexicanos tienes?")
    pesos_mexicanos =  float(pesos_mexicanos)
    valor_dolar=65
    dolares = pesos_mexicanos/valor_dolar
    dolares = round(dolares, 2)#funcion para redondear los decimales (el numero flotanto, cuantos decimales tener)
    dolares = str(dolares)
    print("Tienes $"+ dolares +" dolares")
    
else:
    print("digite una opcion valida")


dolares_2 = input("digite cuantos dolares tiene: ")
cop = str(round(float(dolares_2) * 3875, 2) )
print("usted tiene $"+cop +" pesos colombianos")