#CONVERSAO DE TIPOS

#INT PARA FLOAT
preco = 15
preco = float(preco) #float esta servindo nesta linha como funcao de conversao/construtora
print(f'\nRESULTADO INT P/FLOAT: {preco}')

#FLOAT PARA INT
preco = 16.14
preco = int(preco)
print(f'\nRESULTADO FLOAT P/INT: {preco}\n')

#NUMERO PARA STRING
preco = 17
preco = str(preco)
print(f'RESULTADO NUMERO P/STRING: {preco}')
print(type(preco)) #type revela o tipo/classe da variavel

#STRING PARA NUMERO
preco = "27"
preco = float(preco)
print(f'\nRESULTADO STRING P/NUMERO: {preco}')
print(type(preco))

