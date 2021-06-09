def primo(num):
    real = False
    for i in range(2, num+1):
        if(num%2==0  or num%i==0 or num==1)and num!=i:
            break
        else:
            real = True
    return real


def run():
    num= int(input("digite un numero a comprobar: "))
    if(primo(num)):
        print("es primo")
    else:
        print("no es primo")


if __name__=='__main__':
    run()