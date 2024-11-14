#Recebe duas notas
nota_p1=float(input("Digite sua nota da P1:"))
nota_p2=float(input("Digite sua nota da P2:"))

# Calcula a média
media = (nota_p1 + nota_p2) / 2

# Verifica se o aluno foi aprovado
aprovado = media >= 7

# Mostra a média e se o aluno foi aprovado ou não
print(f"Média: {media:.2f}")
print(f"Aprovado: {aprovado}")


