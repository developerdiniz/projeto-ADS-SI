def mensagem():
    print('criado no python')

def somLista(lista,listona):
    index = 0
    resultado = []
    for x in lista:
        resul = x + listona[index]
        resultado.append(resul)
        index += 1
    return resultado
    
    
