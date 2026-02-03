# Ler nome do usuário
nome = input('Informe seu nome completo: ')
print(f'Olá, {nome}!')

# Receber informações do salário e gastos
renda_mensal = float(input('Qual é o valor líquido de seu salário? '))
total_agua = float(input('Qual é o valor total da conta de água esse mês? '))
total_energia = float(input('Qual é o valor total da conta de energia esse mês? '))
total_aluguel = float(input('Qual é o valor do aluguel? '))
total_cartao = float(input('Qual é o valor da fatura de seu cartão esse mês? '))

# Soma das despesas
gastos_total = total_agua + total_energia + total_aluguel + total_cartao
print(f'O valor total de seus gastos nesse mês é de R$ {gastos_total:.2f}.')

# Cálculo do saldo final
saldo_final = renda_mensal - gastos_total

if saldo_final >= 0:
    print(f"Parabéns! Seu orçamento está positivo. Você tem R$ {saldo_final:.2f} sobrando.")
else:
    valor_que_falta = abs(saldo_final) 
    print(f"Atenção! Seu orçamento estourou. Você precisa de mais R$ {valor_que_falta:.2f} para quitar suas contas.")

# Aprendizado
# Aprendi a utilizar a função nativa abs() para obter o valor absoluto (módulo) de um número.
# Compreendi como utilizar especificadores de formato dentro de f-strings para controlar a exibição de números de ponto flutuante (float).
# Manipulação de variáveis e tipos de dados em Python.
# Aplicação de estruturas condicionais (if/else) para tomada de decisão.
# Documentação de projetos e criação de fluxogramas para planejar a lógica antes do código.
