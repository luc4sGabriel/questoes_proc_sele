# Escreva uma função que gere os primeiros 15 números da sequência de Fibonacci e imprima o resultado.

def fibonacci():

    # Vetor com os 2 primeiros numeros da sequencia , necessarios pra somar os proximos numeros
    vector = [0, 1]
    
    # Loop para gerar os próximos números da sequência comecando do indice 2
    for i in range(2, 15):

        # Acesso o ultimo valor e somo com o penultimo da sequencia para ter o proximo numero , jogo numa variavel e adiciono na lista  
        nxt_nmbr = vector[-1] + vector[-2]
        vector.append(nxt_nmbr)
        
    return vector

print(fibonacci())

