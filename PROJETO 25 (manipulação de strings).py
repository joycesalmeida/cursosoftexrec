# QUESTÃO
# Estruture três códigos, os quais devem conter uma função de manipulação de string que obtenha resultado.

# RESPOSTA
# Função: Manipulação de Strings
# Autor(a): Joyce Silva de Almeida
# Curso: SOFTEX - Back-End - UPE/Garanhuns-PE
# Data: 23-08-2022

#código 01 (funçao .split(), onde tem toda vírgula vira um quebra de linha)

texto1 = 'HTML,CSS,JavaScript,Python'
linguagens = texto1.split(',')
for i in linguagens:
    print(i)


#código 02 (função .upper(), onde toda a string fica com letras maiúsculas)

texto2 = 'são as minhas linguagens de programação preferidas'
print(texto2.upper())

#código 03 (função .title(), onde a primeira letra de cada palavra da string fica maiúscula)

texto3 = input("Qual a sua linguagem preferida?")
print('minha linguguem preferida é'.title(), texto3.title())