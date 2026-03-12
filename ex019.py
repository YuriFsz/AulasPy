# Faça um programa que mostre na tela a contagem regressiva ate o ano novo indo de 10 ate 0 com uma pausa de 1seg

from time import sleep
for c in range(10, -1, -1,):
    sleep(1)
    print(c)
sleep(1.5)
print('FIM ANO NOVO!')