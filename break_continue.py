def run():
    #mostrar numeros pares del 1 al 100
    #continue hace que siga a la siguiente iteracion
    #break rompe el ciclo
    for i in range (10):
        if i % 2 != 0:
            continue
        print(i)


    for j in range(10):
        print(j)
        if j==5:
            break;


    texto = input("escribe un texto: ")
    for letra in texto:
        if letra=='o':
            break
        print(letra)


    #desafio usar continue and break en while
    x=0
    while(x<10):
        print(x)
        x=x+1
        if(x==9):
            print("se terminara el ciclo")
            continue
            
        y = "hello world"
        if(x==10):
            print("se termino pero igual no quiero que se escriba el print que viene despues de esto")
            break
            print("este mensaje no se deberia de ver" + y)
if __name__ == '__main__':
    run()