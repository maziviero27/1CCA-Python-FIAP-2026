peca1 = (input("Digite o nome da primeira peça: "))
qt_peca1 = float(input("Digite a quantidade da primeira peça: "))
vl_peca1 = float(input("Digite o valor em R$ da primeira peça: "))
total1 = vl_peca1 * qt_peca1
print(f"O valor total de {peca1}(s) é de: R${total1}\n")

peca2 = (input("Digite o nome da segunda peça: "))
qt_peca2 = float(input("Digite a quantidade da segunda peça: "))
vl_peca2 = float(input("Digite o valor em R$ da segunda peça: "))
total2 = vl_peca2 * qt_peca2
print(f"O valor total de {peca2}(s) é de: R${total2}\n")
total_final = total1 + total2

print(f"\nO valor final a pagar é de: R${total_final}")

