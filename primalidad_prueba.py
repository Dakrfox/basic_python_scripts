def es_primo(num):
    cont=0
    for i in range(1,num+1):
        if i==1 or i ==num:
            continue
        if(num %i ==0):
            cont+=1
    if cont ==0 and num!=1:
        return True
    else: 
        return False


def run():
    num= int(input("digite el numero a probar: "))
    if es_primo(num):
        print("es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    run()