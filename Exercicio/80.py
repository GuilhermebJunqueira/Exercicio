quant = int(input("Digite a quantidade de fitas: "))

valAluguel = float(input("Digite o valor do aluguel: "))

fatAnual = quant / 3 * valAluguel * 12

print("\nFaturamento anual:", fatAnual)

multas = valAluguel * 0.1 * (quant / 3) / 10

print("\nMultas mensais:", multas)

quantFinal = quant - quant * 0.02 + quant / 10 * quant * 1.08

print("\nQuantidade de fitas no final do ano:", quantFinal)