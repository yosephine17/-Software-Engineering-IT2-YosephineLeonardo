#VARIABLE

#INTEGER
a = 5
b = 6
c = a+b

#STRING
kampus = "President University"

#BOOLEAN
D = True
E = False

#FLOAT
F = 8.1

#LIST/ARRAY
G = []

#DICTIONARY
H = {}

#TUPLE
I = ()

#PRINT
print(kampus)
print("Yosephine")
print(5)
print(1+2)
print(True)

#PRINT02
print("Saya kuliah di : " + kampus)
print("Adik saya ada: " + str(a))
print("Adik saya ada: ".format(b))
print("Nama saya: {}, Asal: {}, Umur: {}".format("Yosephine", "Banda Aceh", 21))

#LIST/ARRAY
Bunga = ["Mawar", "Melati", "Tulip", "Bougenville"]

#PRINT LIST
print(Bunga[0])
print(Bunga[1])
print(Bunga[2])
print(Bunga[3])

ulang = ["3 kali"] * 3
ulang

print(Bunga[0:2]) #print list 0 dan 1
Bunga[-2] #print list urutan ke 2 dari belakang
Bunga[-2:] #print 2 list terakhir

#APPEND
Bunga.append("Lily")
print(Bunga)
