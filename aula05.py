n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma soma é {}, \n o produto é {} e a divisão é {:.2f}'.format(s, m, d), end=' ')
print(' A Divisão inteira {} e potência {}'.format(di, e))

# //end='' para nao ter quebra de linha mesmo tendo dois prints

# {:.2f} para limitar quantos caracteres vao restornar em caso de numeros decimais

# \n para quebrar linha // mesma coisa que <br/>