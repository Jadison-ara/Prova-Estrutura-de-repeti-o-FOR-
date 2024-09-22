# Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).

# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

# Ao final, exiba a soma dos números pares encontrados.

#Variaveis declaradas para  armazenar os valores de início e fim do intervalo

Inicio = int (input("Digite o primeiro número do intervalo: "))
Fim_intervalo = int (input("Digite o segundo número do intervalo: "))
soma_pares = 0

#laco  for para percorrer todos os números do intervalo

for num in range (Inicio,Fim_intervalo + 1):
    if num % 2 == 0:
        soma_pares += num

#Estrutura de condicao  para verificar se a soma_pares é igual a 0, caso seja exibe a mensagem

if soma_pares == 0:
    print("Não há números pares no intervalo.")
else:
    print("A soma dos números pares no intervalo é:", soma_pares)

    
