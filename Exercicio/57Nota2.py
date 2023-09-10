num1 = float(input("Entre com uma nota: "))

num2 = float(input("Entre com outra nota: "))

mf = (num1 + num2)/2

print(f'Media truncada : {((mf-0.5)+0.0001)}')
print(f'Media arredondada: {(mf)}')