base = float(input("Digite o valor da base: "))
altura = float (input("Digite o valor da altura: "))

perimetro = 2*(base + altura)
area = base * altura
diagonal = (1/2)**(base**2 + altura**2)

print("Perimetro: ",perimetro)
print("Area: ",area)
print("Diagonal ",diagonal)