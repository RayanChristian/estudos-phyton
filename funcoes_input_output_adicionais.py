#FUNCOES INPUT, OUTPUT/PRINT, END E SEP

#INPUT - funcao para receber dados (entre aspas: mensagem mostrada em tela para solicitar os dados do usuario)
nome = input("Informe seu primeiro nome: ") 
sobrenome = input("Informe seu sobrenome: ")

#PRINT - funcao para mostrar os dados em tela
print(nome, sobrenome)

#END - funcao que determina o que aparecera no final da linha
print(nome, sobrenome, end = "..\n") #Obs: Por padrao a funcao print quando terminada, realiza a quebra de linha, sendo necessario o \n somente em ocasioes especificas como no uso da funcao end

#SEP - funcao que determina o que aparecera nos espacos "vazios" entre os valores
print(nome, sobrenome, sep = "#") 

