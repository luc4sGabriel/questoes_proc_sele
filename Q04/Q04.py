# Escreva uma função que determine se uma palavra é um palíndromo. A função deve
# retornar True se for um palíndromo e False caso contrário.

"""
import array as arr 

numbers = arr.array('i', [1, 2, 3, 4, 5])

copy = numbers[::-1]

print(copy)
# array('i', [5, 4, 3, 2, 1])
"""

def funcao(palavra):
    # Array com a palavra sem espaços e minúscula
    palavra = palavra.replace(" ", "").lower()

    # Verifica a igualdade do array com a palavra original e compara com o novo array usando o slice negativo , onde ele copia o que esta no vetor ao contrario . Ainda bem que o python ajuda nisso kkkkkkk 
    return palavra == palavra[::-1]

# palavra1 = "A base do teto desaba"
# palavra2 = "teste"

print(funcao("A base do teto desaba"))
print(funcao("teste"))

