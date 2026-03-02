nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print('Primeira nota: {} \n Segunda nota: {} \n Aluno media: {}'.format(nota1, nota2, media))

if media >= 6: print(' APROVADO')
else:
    print(' REPROVADO')