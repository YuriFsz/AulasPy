# Taboada no numero escolhido

n = int(input("digite um numero para ver sua taboada: "))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))