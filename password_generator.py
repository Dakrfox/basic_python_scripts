import random

def generador():
    upperc=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'L' ]
    lowerc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l']
    simbols=['!', '%']
    number=['1','2','3']
    charts= upperc + lowerc + simbols + number
    pwd = []
    for i in range(15):
        charts_random = random.choice(charts)
        #elige dentro de una lista un caracter aleatorio
        pwd.append(charts_random)

    pwd = ''.join(pwd)
    #''.join() genera que una lista se convierta en string
    return pwd

def run():
    pwd_new = generador()
    print("tu nueva contraseña es: " + pwd_new)


if __name__ == '__main__':
    run()