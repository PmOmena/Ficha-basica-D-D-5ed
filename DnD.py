import random

r1 = 'dwarf'
r2 = 'elfo'
r3 = 'gnomo'
r4 = 'humano'
r5 = 'draconato'
r6 = 'halfling'
r7 = 'meio-elfo'
r8 = 'meio-orc'
r9 = 'tiefling'

lista = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
random.choice(lista)

c1 = 'Barbaro'
c2 = 'Bardo'
c3 = 'Bruxo'
c4 = 'Clérigo'
c5 = 'Druida'
c6 = 'Feiticeiro'
c7 = 'Guerreiro'
c8 = 'Ladino'
c9 = 'Mago'
c10 = 'Monge'
c11 = 'Paladino'
c12 = 'Patruleiro'

listac = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
random.choice(listac)

print(f'A raça de seu personagem será {random.choice(lista)}, e sua classe será {random.choice(listac)},')

t1 = 'Leal e Bom'
t2 = 'Neutro e bom'
t3 = 'Caótico e Bom'
t4 = 'Leal e neutro'
t5 = 'Neutro'
t6 = 'Caótico e Neutro'
t7 = 'Leal e mau'
t8 = 'Neutro e mau'
t9 = 'Caótico e Mau'

listat = [t1,t2,t3,t4,t5,t6,t7,t8,t9]

print(f'A tendencia do seu personagem será {random.choice(listat)},')


a1 = 'Acólito'
a2 = 'Artesão de Guilda'
a3 = 'Artista'
a4 = 'Charlatão'
a5 = 'Criminoso'
a6 = 'Eremita'
a7 = 'Forasteiro'
a8 = 'Marinheiro'
a9 = 'Nobre'
a10 = 'Órfão'
a11 = 'Sábio'
a12 = 'Soldado'
listaa = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12]
print(f'Sua antecedencia é de {random.choice(listaa)}. ')\  