<<<<<<< HEAD
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    print('------ {} PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
        if sexo in 'Ff' and idade < 20:
            totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
=======
# Faça uma simulacção de venda a vista, parcelado e carnê

iphone = 4500
iphonecartao10x = iphone  + (iphone * 10/100)
iphonecarne = iphone + (iphone * 20/100)

colchao = 2300
colchaocartao10x = colchao  + (colchao * 10/100)
colchaocarne = colchao + (colchao * 20/100)

tv = 4999.90
tvcartao10x = tv  + (tv * 10/100)
tvcarne = tv + (tv * 20/100)

for i in range(10):
    produto = input('produto voce quer ?')
    if produto == 'iphone':
        print('O aparelho iphone esta custando R${} Reais'.format(iphone))
        print('Preço no cartão {:.2f}'.format(iphonecartao10x))
        print('Preço no carne {:.2f}'.format(iphonecarne))

    if produto == 'tv':
        print('O aparelho TV Samsumg esta custando R${} Reais'.format(tv))
        print('Preço no cartão {:.2f}'.format(tvcartao10x))
        print('Preço no carne {:.2f}'.format(tvcarne))

    if produto == 'colchao':
        print('O aparelho colchao esta custando R${} Reais'.format(colchao))
        print('Preço no cartão {:.2f}'.format(colchaocartao10x))
        print('Preço no carne {:.2f}'.format(colchaocarne))
else:
    print('Produto nao encontrado')
>>>>>>> 9d874b58e36976f1288044f9005925ad34e28844
