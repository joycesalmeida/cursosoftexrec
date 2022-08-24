import datetime

print('='*30)
print('Calcula Idade  - Joyce Almeida')
print('='*30)
nome = input ("Qual o seu nome? ")
ano = eval (input ("Você nasceu em que ano? "))
mes = eval (input ("Você nasceu em que mês? "))
dia = eval (input ("Você nasceu em que dia? "))
ano_atual = eval (input ("Digite o ano atual? "))
mes_atual = eval (input ("Digite o mês atual? "))
dia_atual = eval (input ("Digite o dia atual? "))
dataNasc = datetime.date(ano, mes, dia)
dataAtual = datetime.date(ano_atual, mes_atual, dia_atual)

diferenca = (dataAtual - dataNasc)
rslt = (diferenca.days / 365.25)


if (dia == dia_atual and mes == mes_atual):
    print ("O %s tem %d anos!" %(nome, rslt))
else:
    ((dia > dia_atual and mes == mes_atual) or mes < mes_atual)
    print ("O %s tem %d anos!" %(nome, rslt))
