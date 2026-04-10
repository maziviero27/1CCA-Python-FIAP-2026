# ESTRUTURAS CONDICIONAIS

nota_final = 7

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")

#OPERADORES RELACIONAIS
print()
print(6 >= 6)

idade = 20
print(idade == 20)

maior_idade = idade >= 18
print(maior_idade)

verificar_email = True
verificar_senha = True

login = verificar_email and verificar_senha
print(login)

nota_final = 5
if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
        print("Recuperaçâo")
else:
        print("Aprovado")
