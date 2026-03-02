# Faça um exercicio que leia o preço de um produto e o novo preço com 5% de desconto

preco = float(input('Digite o preço do produto: R$ '))

desconto = float(input('Digite o valor do desconto: R$ '))

precodescontado = preco * desconto/100

print('O valor do produto é R${}Reais \nO valor do desconto é de {}% \nApós o desconto o valor vai ser de: R${:.2f}Reais'.format(preco, desconto, preco - precodescontado))