def knapsack_recursive(capacidade, peso, valor, tamanho): 
    if tamanho == 0 or capacidade == 0 : 
        return 0
  
    if (peso[tamanho-1] > capacidade): 
        resultado = knapsack_recursive(capacidade, peso, valor, tamanho-1) 
        return resultado
    else: 
        resultado = max(valor[tamanho-1] + knapsack_recursive(capacidade-peso[tamanho-1], peso , valor , tamanho-1), 
                   knapsack_recursive(capacidade, peso, valor, tamanho-1)) 
        # print("oi", tamanho)
        return resultado
  
# valor = [100, 20, 60, 40] 
# peso = [3, 2, 4, 1] 
# capacidade = 5
# tamanho = len(valor) 
valor = [1, 6, 18, 22, 28] 
peso = [1, 2, 5, 6, 7] 
capacidade = 11
tamanho = len(valor) 

print(knapsack_recursive(capacidade, peso, valor, tamanho))

 
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
  
    return K[tamanho][capacidade] 
  
# valor = [60, 100, 120] 
# peso = [10, 20, 30] 
# capacidade = 50
# tamanho = len(valor) 
valor = [100, 20, 60, 40] 
peso = [3, 2, 4, 1] 
capacidade = 5
tamanho = len(valor) 
# valor = [1, 6, 18, 22, 28] 
# peso = [1, 2, 5, 6, 7] 
# capacidade = 11
# tamanho = len(valor) 
print(knapsack_interactive(capacidade, peso, valor, tamanho)) 