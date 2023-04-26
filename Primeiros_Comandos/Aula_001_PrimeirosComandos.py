#-------------------------------------------------------#
# COMANDO PARA IMPRIMIR NA TELA 
#-------------------------------------------------------#

print('Olá, Mundo!') # PRINT PARA IMPRIME NA TELA 
print(7+4)           ## PRINT PARA REALIZA O CALCULA
print('7'+'4')       ### PRINT PARA CONCATENAR 
print('Olá', 5)      #### PRINT PARA CONTATENAR STRING + NUMERO   

#---------------------------------------------------------#

#TODA VARIAVEL EM PYTHON SÀO OBJETOS
nome = 'Michel'
idade = 34
peso  = 67.8

#print(nome + idade + peso) NÃO É POSSIVEL CONCATENAR TIPO DE VÁRIAVEIS DIFERENTES UTILIZANDO O +.
print(nome, idade, peso) #FORMA CORREAT PARA CONTATENAR TIPOS DIFERENTES UTILIZANDO A VIRGULA ,.

#--------------------------------------------------------------------------------------#
# INTERATIVIDADE COM ENTRADA DE DADOS

nome = input('Qual é o seu nome: ')
idade = input('Qual a sua idade: ')
peso = input('Qual o seu peso: ')
print(nome, idade, peso)
# FOI CRIADO UM SCRIPT PARA SER EXECUTADOS aula01