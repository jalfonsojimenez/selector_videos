import json
f = open('repertorio.json')
canciones = json.load(f)

def printa(f):
    def pregunta():
        print( 'Que quieres de evento? \n 0: todo \n 1: boda \n 2: funeral')
        x = int(input() or 0)
        if x < 0 or x >5:
            print('no existe esa opcion')
        if x == 1:
            x = 'boda'
        if x == 2:
            x = 'funeral'
        if x == 0:
            x = 'todo'
        lista = []
        lista.append(x)
        print('cuantos musicos, 0 si no importa')
        y = int(input() or 3) 
        lista.append(y)
        f(lista)
        return lista 
    return pregunta 

@printa
def imprimeLista(evento):
    cagada = evento
    if not cagada[1] == 0:
        for v in canciones:
            #if cagada[0] in canciones[v]['tags'] and cagada[1] in canciones[v]['tags']:
            if cagada[0] in canciones[v]['tags'] and cagada[1] == canciones[v]['integrantes']:
                imprime_con_valor(v)
    else:
            for v in canciones:
                if cagada[0] in canciones[v]['tags']:
                    imprime_con_valor(v)

    return cagada

def imprime_con_valor(valor):
    print('titulo: ', canciones[valor]['titulo'])
    print( 'integrantes', canciones[valor]['integrantes'])
    url = canciones[valor]['video']
    print( f"video: http://youtube.com/watch?v={ url}")
    print( canciones[valor]['tags'])
    print("")

#print(imprimeLista())

imprimeLista()
