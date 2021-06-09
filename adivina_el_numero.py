import random


def run():
    num = random.randint(1,100)
    user_num= int(input("digita un numero del 1 al 100: "))
    while(num!=user_num):
        if(user_num<num):
            print("es un numero mas grande")
        else:
            print("el numero es mas pequeño")
        user_num= int(input("digita un nuevo numero del 1 al 100: "))
        
    print("advinaste")


if __name__ == '__main__':
    run()