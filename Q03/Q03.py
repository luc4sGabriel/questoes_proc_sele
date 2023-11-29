# Implemente uma função de busca em uma lista ordenada de números inteiros. A
# função deve receber um número como parâmetro e retornar a posição do número na lista, ou
# indicar se não está presente.

def busca_simples(lista, elemento):
    for i in range(len(lista)):

        # Como a lista esta ordenada (levei em conta uma lista ordenada de forma crescente), se o ultimo elemento da lista for menor que o elemento procurado ele ja encerra o laco para poupar recursos ..
        if elemento > lista[-1]:
            break

        # Achou o elemento equivalente , retorna a posicao dele na lista
        elif lista[i] == elemento:
            return i
    
    # Se o elemento não estiver na lista retorna -1
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento = 72

rslt = busca_simples(lista, elemento)

if rslt != -1:
    print(f"O elemento {elemento} esta na posicao {rslt} da lista.")
else:
    print(f"O elemento {elemento} nao esta na lista.")