# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:53:53 2022

@author: Everton Castro
"""

CPF = input('Digite seu cpf: ')
#CPF = '168.995.350-09'
CPF = CPF.replace('-', '')
CPF = CPF.replace('.','')
CPFLista = CPF
c = - 10
soma = 0
soma2 = 0
for v, p in enumerate(CPFLista[:9], c):
    p = int(p)
    soma += p * (v*(-1))
soma = 11 - (soma % 11)


if soma >= 10:
    penultimo = 0
else:
    penultimo = soma

c = - 11   
for v, p in enumerate(CPFLista[:9], c):
    p = int(p)
    soma2 += p * (v*(-1))        
    if v == -3:
        v -= -1
        soma2 += penultimo * (v*(-1))

soma2 = 11 - (soma2 % 11)

if soma2 >= 10:
    ultimo = 0
else:
    ultimo = soma2
   
CPFNOVO = CPF[:9] + str(penultimo) + str(ultimo)
CPFESTADO = CPFNOVO[8]

CPFEVITASEQUENCIA = str(CPFNOVO[0]) * 11
if CPFNOVO == CPF:
    CPFNOVO = CPFNOVO[:3] + '.' + CPFNOVO[3:6] + '.' + CPFNOVO[6:9] + '-' + CPFNOVO[9:11]
    print('CPF VÁLIDO')
    print(CPFNOVO)
    if int(CPFESTADO) == 5:
        print('O CPF pode ser da Bahia ou Sergipe')
    elif int(CPFESTADO) == 8:
        print('O CPF é de São Paulo')
    elif int(CPFESTADO) == 1:
        print('O CPF pode ser do Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins')
    elif int(CPFESTADO) == 2:
        print('O CPF pode ser do Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima')
    elif int(CPFESTADO) == 3:
        print('O CPF pode ser do Ceará, Maranhão ou Piauí')
    elif int(CPFESTADO) == 4:
        print('O CPF pode ser do Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas')
    elif int(CPFESTADO) == 6:
        print('O CPF é de Minas Gerais')
    elif int(CPFESTADO) == 7:
        print('O CPF pode ser do Rio de Janeiro e Espírito Santo')
    elif int(CPFESTADO) == 9:
        print('O CPF pode ser do Paraná e Santa Catarina')
    elif int(CPFESTADO) == 0:
        print('O CPF é do Rio Grande do Sul')
    
else:
    print('CPF INVALIDO')