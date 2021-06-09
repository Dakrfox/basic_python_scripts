def run():
    diccionario={
        'llave1':1,
        'llave2':2,
        'llave3':3
    }
    #acceder a una llave
    # print(diccionario['llave1'])
    pob ={
        'argentina': 44938712,
        'brasil': 21047125,
        'colombia': 50372424
    }
    # print(pob['colombia'])
    #recorrer diccionarios
    #devuelve la llave
    for pais in pob.keys():
        print(pais)
    #devuelve el valor
    for value in pob.values():
        print(value)
    #devuelve todo
    for pais, poblacion in pob.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes ')


if __name__ == '__main__':#entry point
    run()