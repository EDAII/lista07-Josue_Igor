import random

def knapsack_interactive(capacidade, peso, valor, tamanho): 
    K = [[0 for x in range(capacidade+1)] for x in range(tamanho+1)] 
  
    for i in range(tamanho+1): 
        for w in range(capacidade+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif peso[i-1] <= w: 
                K[i][w] = max(valor[i-1] + K[i-1][w-peso[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    
    for j in range(tamanho+1):
        print(K[j])
  
    resultado = K[tamanho][capacidade]
    print("\nO valor maximo que pode ser carregado é: ", resultado)
      
    cap_disponivel = capacidade 
    itens = []
    wt = []
    for i in range(tamanho, 0, -1): 
        if resultado <= 0: 
            break 
        if resultado == K[i - 1][cap_disponivel]: 
            continue
        else:     
            item = i
            itens.append(item)
            p = peso[i - 1]
            wt.append(p)
            resultado = resultado - valor[i - 1] 
            cap_disponivel = cap_disponivel - peso[i - 1] 
    
    print("Com um peso total de: '{}'.\nOs itens a serem levados são: '{}'.\nEspaço disponivel na mochila: '{}'.".format(sum(wt), itens, cap_disponivel))

def main():
    MIN_ITENS = 3
    MAX_ITENS = 17
    CAPACIDADE_MIN = 10
    CAPACIDADE_MAX = 25

    capacidade = int(random.random()*100)%(CAPACIDADE_MAX - CAPACIDADE_MIN) + (CAPACIDADE_MIN)
    tamanho = int(random.random()*100)%(MAX_ITENS - MIN_ITENS) + (MIN_ITENS)
    valor = [int(random.random()*100)+1 for _ in range(tamanho+1)]
    peso = [int(random.random()*100)%40+1 for _ in range(tamanho+1)]
    # valor = [1, 6, 18, 22, 28] 
    # peso = [1, 2, 5, 6, 7] 
    # capacidade = 11
    # tamanho = len(valor)

    print("A capacidade da mochila é: ", capacidade)

    print("\nOs itens disponíveis são:")
    for item in range(0, len(valor)):
        print("Item: {:2d}, Valor: {:02d}, Peso: {:02d}\n".format(item+1, valor[item], peso[item]))
    
    knapsack_interactive(capacidade, peso, valor, tamanho)

if __name__ == '__main__':
    main()
    
