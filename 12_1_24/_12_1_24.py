from math import * #неправильный порядок
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #изменить переменную
S=a**2
print("Ruudu pindala", round(S,2))
P=4*a
print("Ruudu ümbermõõt:", round(P,2)) #ковычки 
di=a*sqrt(2) #убираем math/ sqr меняем на sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #лишняя скобка
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #добавить float 
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #добавить float 
S=b*c
print("Ristküliku pindala", round(S,2)) #добавить ковычки
P=2*(b+c) # знак *
print("Ristküliku ümbermõõt", round(P,2))
di=sqrt(b**2+c**2) #убираем math/добавляем *
print("Ristküliku diagonaal", round(di,2)) #добавить скобку и *
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus =>")) # добавить float 
d=2*r # *
print("Ringi läbimõõt"+ str(d,2)) #запятая и добавить + str
S=pi*r**2 #лишние  скобки/* 
print("Ringi pindala", round(S,2))
C=2*pi*r #лишние  скобки/* 
print("Ringjoone pikkus", round(C,2)) #добавить скобку
