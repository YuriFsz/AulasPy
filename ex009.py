# Faça um programa que leia quanto dinheiro vc tem na carteira e retorne quantos dolares vc pode comprar

dinheirocarteira = int(input('digite seu saldo: '))

dolar = 5.13

conversao = dinheirocarteira / dolar

print('Saldo R${} Reais \nO dolar está {} \nLogo você pode comprar U${:.2f}'.format(dinheirocarteira,dolar,conversao))