# Crie uma função que ordene uma lista de números inteiros em ordem crescente. Utilize qualquer algoritmo de ordenação de sua escolha.



# Antes de fazer o algoritmo de ordenacao , criei uma funcao que gera numeros aleatorios em uma lista de tamanho customizavel para o algoritmo de ordenacao fazer seu trabalho .

import random

def gerar_numeros_aleatorios(tamanho, valor_minimo, valor_maximo):
    numeros_aleatorios = [random.randint(valor_minimo, valor_maximo) for _ in range(tamanho)]
    return numeros_aleatorios

lista_aleatoria = gerar_numeros_aleatorios(10, 1, 50)


#Algoritmo de ordenacao
def bubble_sort(arr):
    # Variavel para guardar o tamanho da lista de numeros 
    n = len(arr)

    # For para varrer todos os numeros da lista
    for i in range(n):

        # Outro for auxiliar para ter o valor do elemento visitado anterior ao que esta no laco(i) para ser comparado
        for j in range(0, n - i - 1):

            # Compara o valor dos elementos
            if arr[j] > arr[j + 1]:

                # Se for maior , ele troca as posicoes dos elementos , sempre jogando o maior valor para o fim da lista e o menor para o comeco dela .
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sort(lista_aleatoria)

print("Lista Bonitinha:", lista_aleatoria)
