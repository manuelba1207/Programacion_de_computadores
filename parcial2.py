#desarrollar un programa que determine si en una lista no existen elementos repetidos 
lista = [1,2,3,4,5,6,7,8,8,8,9]
listab = [2,3,4,5,6,7,0]

def andres (lista):
    a = 0

    for i in lista :
       if lista.count(i)> 1 :
          a = 1
        
    if a == 1 :
      print ("La lista tiene valores repetidos")
    else : 
     print ("la lista no tiene valores repetidos") 
     
andres(lista)
andres(listab)
      
# Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o mas vocales. 
# Si la cadena existe debe imprimirla y si no existe debe imprimir no existe

l = ["Andreaaas", "Pez", "Alfonso","Eduardo","audio"]
n = ["Jorge","perro","na"]

def segundo (lista):
    listar = []
    listanr = []
    s = len(lista) 

    for i in range (0,s) :
        if ((l[i].count("A")) + (l[i].count("E"))+(l[i].count("I"))+(l[i].count("O"))+(l[i].count("U"))
            +(l[i].count("a"))+(l[i].count("e"))+(l[i].count("i"))+(l[i].count("o"))+(l[i].count("u"))) > 1 :
            listar.append(l[i])
        else : 
            listanr.append (l[i])
        
    print ("las palabras con mas de dos vocales son : " , listar)
    print ("las palabras con una sola vocal son : " , listanr)

segundo(l)
segundo(n)    
        
#desarrollar un programa que dadas dos listas determine que elementos tiene la primera lista que no tenga la segunda lista

lista1 = ["a",1,3,5,7,"Manuel"]
lista2 = ["a",2,"bola","nanuel"]
listaf = []

numero = len(lista1)

lista1.extend(lista2)

for i in range (0,numero) :
    if lista1.count(lista1[i]) == 1 :
        listaf.append(lista1[i])
    else: None
    

print ("los elementos que solo estan en la lista 1 son :" ,listaf)
     
#desarrollar un algoritmo que calcule el promedio de un arreglo de reales

reales = [1.5,2.760,3.6]
reales2 = [4.54,4.760,3.8]

a = 0
def promedio (x,y):
     return x/y
for i in reales:
    a = a+i

print (promedio (a,len(reales)))

a = 0
def promedio (x,y):
     return x/y
for i in reales2:
    a = a+i

print (promedio (a,len(reales2)))



#desarrollar un algoritmo que determine la mediana de un arreglo de enteros. la mediana es el numero que queda en la mitad del arreglo despues de ser ordenado

enteros = [1,2,3,4,2,6,7,0]
enteros2 = [3,6,9,4,2,5]

enteros.sort()
a = ((len(enteros))//2)
print (enteros[int(a)])

enteros.sort()
a = ((len(enteros2))//2)
print (enteros2[int(a)])