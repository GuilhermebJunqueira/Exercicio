salariominimo = float(input("Digite o valor do salario minimo"))

quantidadeQW = float(input("digite o valor da quantidade de quilo wats"))

valorQW = (salariominimo /7)/100
valorpago = quantidadeQW * valorQW
desconto = valorpago*(10/100)
novovalor = valorpago - desconto

print("Preço do quilowatt: ",valorQW, " valor a ser pago ",valorpago," valor com desconto",novovalor)