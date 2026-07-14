#FUNCAO INPUT, OUTPUT/PRINT, END E SEP

nome = input("Informe seu primeiro nome: ") #INPUT - funcao para receber dados (entre aspas: mensagem mostrada em tela para solicitar os dados do usuario)
sobrenome = input("Informe seu sobrenome: ")
print(nome, sobrenome) #PRINT - funcao para mostrar os dados
print(nome, sobrenome, end = "..\n") #END - funcao que determina o que aparecera no final da linha
#Obs: Por padrao a funcao print quando terminada, realiza a quebra de linha, sendo necessario o \n somente em ocasioes especificas como no uso da funcao end
print(nome, sobrenome, sep = "#") #SEP - funcao que determina o que aparecera nos espacos "vazios" entre os valores

