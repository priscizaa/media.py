# Média aritmética com três notas. (CARLA PRISCILA)
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))

media = (nota1 + nota2 + nota3) / 3
print('A média do aluno é: ', media)

if media < 0 or media > 10:
    print('Número inválido')
elif media >= 6:
    print('Aprovado')
else: 
    print('Reprovado')