# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:31:11 2022

@author: Everton SSD
"""
from random import randint

CPF = str(randint(100000000, 999999999))
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

CPFNOVO = CPFNOVO[:3] + '.' + CPFNOVO[3:6] + '.' + CPFNOVO[6:9] + '-' + CPFNOVO[9:11]

print(CPFNOVO)
