def calcular_troco(valor_total,dinheiro_recebido):
    troco = dinheiro_recebido - valor_total
    return troco

total = 0 
qtd_itens = 0
print(" Caixa Aberto!")

while True:
    print("Aguardando Item!")
    valoritem = float(input("Valor do item: R$"))
    
    if valoritem <= 0:
        break
    
    total = valoritem + total
    print(total)
    qtd_itens = qtd_itens +1

print(f"Total da compra: R$ {total:.2f}")
print(f"Quantidade de itens: {qtd_itens}")

dinheiro = float(input("Valor recebido: R$ "))
troco = dinheiro - total

if troco >= 0:
    print(f"Troco: R$ {troco:.2f}")
else:
    print("Pagamento insuficiente!")