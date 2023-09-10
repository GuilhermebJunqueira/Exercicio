num = int(input("Digite um numero de 3 digitos: "))
centena = num//100 
dez = (num%100)//10
unidade = num%10
print(f'O valor invertido é{unidade} {dez}{centena}')