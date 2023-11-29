# Crie uma estrutura de árvore binária simples contendo os números de 1 a 5. Escreva
# uma função para percorrer a árvore em ordem e imprimir os valores.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def percorrer_em_ordem(No):
    if No:
        # Percorre a subárvore esquerda
        percorrer_em_ordem(No.esquerda)
        # Imprime o valor do nó atual
        print(No.valor, end=' ')
        # Percorre a subárvore direita
        percorrer_em_ordem(No.direita)

# Criando a árvore binária com os números de 1 a 5
raiz = No(3)#3
raiz.esquerda = No(2)#2
raiz.direita = No(4)#4
raiz.esquerda.esquerda = No(1)#1
raiz.direita.direita = No(5)#5

# Função para percorrer a árvore em ordem e imprimir os valores
print("Percorrendo a arvore em ordem:")
percorrer_em_ordem(raiz)

"""
   3
  / \
 2   4
/     \
1     5
"""

