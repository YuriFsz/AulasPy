# Um funcionario ganha um valor x de salario, apos um desconto de x% retorne o novo valor do salario

salario = float(input('Digite o salário: '))

aumento = float(input('Digite o percentual de aumento: '))

salarionovo = salario + (salario * aumento/100)

print('O salário antigo era de: R${}Reais, Após o aumento de {}%, o novo salário passará a ser: R${}Reais'.format(salario, aumento, salarionovo))