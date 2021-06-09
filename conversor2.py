#in this script we use functions for better practices
def conversor(pais, valor):
    pesos = float(input("digite el valor en pesos "+ pais + ": "))
    total= str(round(pesos/valor,2))
    print("tienes $" + total +" dolares")
menu="""
Bienvenidos al conversor mejorado 😊

1- pesos colombianos
2- psos argentinos
3- pesos mexicanos

elige un opcion:
"""
opcion =int(input(menu))
if opcion ==1:
    conversor("colombianos",3785)
    
elif opcion==2:
    conversor("argentinos",65)
    
elif opcion ==3:
    conversor("mexicanos",40)
    
else:
    print("opcion no valida... cerrando")