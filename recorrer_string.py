# para comentar texto seleccionado en windows 
# se plsa CTRL + }
def run():
    # nombre = input('escribe un nombre: ')
    # for letra in nombre:
    #     print(letra)
    frase = input("digita una frase: ")
    for caracter in frase:
        print(caracter.upper())


if __name__ == '__main__':
    run()