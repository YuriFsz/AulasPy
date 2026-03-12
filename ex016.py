# O computador deve escolher um numero aleatorio e o usuario tem que escolher outro, devolva aresposta se o usuario acertou
import random

escolhas = int(input('Digite um numero inteiro: '))
num = random.randint(1, 5)
print('O computador escolheu {}, '.format(num))

if escolhas == num:
    print('O seu numero escolhido foi {}, Parábens você acertou!!!!'.format(escolhas))
else:
    print('O seu número escolhido foi {}, Sinto muito, Você errou :('.format(escolhas))

