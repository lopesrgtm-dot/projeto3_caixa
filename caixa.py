total = 0 
print(" Caixa Aberto!")

while True:
    print("Aguardando Item!")
    valoritem = float(input("Valor do item: R$"))
    
    if valoritem <= 0:
        break
    
    total = valoritem + total
    print(total)