#in this script we use functions and manipulated strings
#dejar dos espacion entre funciones y no se que point
def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    if palabra[::]== palabra[::-1]:
        return True
    else:
        return False


#estandar de codigo 
def run():
    palabra = input("escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo ==True:
        print("es palindromo")
    else:
        print("no es palindromo")


#cuando vea la sintaxis siguiente, pytho lo recnoocera y correra todo lo que este debajo de esa linea
if __name__ == '__main__':
    run()