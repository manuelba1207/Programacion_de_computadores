lista = ["radar", "hola", "nivel", "mundo", "somos","manuel","1","2"]

print (lista)

#ejercicio 1
def repetidos(lista):
    return len(lista) == len(set(lista))

repetidos(lista)
if repetidos(lista) == True : 
    print ("Lista sin elementos repetidos:")
else: 
    print ("Lista con elementos repetidos:")

#ejercicio 2 
def palindroma(lista):
    for i in lista:
        if isinstance(i, str) and i == i[::-1]:
            print(i)
            return
    print("No existe")

palindroma(lista)

#ejercicio 3

def vocales(lista):
    vocales = set("aeiouAEIOU")
    for i in lista:
        if isinstance(i, str) and sum(1 for c in i if c in vocales) >= 2:
            print(i)
            return
    print("No existe")

vocales(lista)

#ejercicio 4

def lista_palindroma(lista):
    return lista == lista[::-1]

print("La lista es palíndrome:", lista_palindroma(lista))


## EJERCICIOS BLACKBOX

#Verificar si Todos los Elementos son Números 

def tnumeros(lista):
    return all(isinstance(x, (int, float)) for x in lista)


if tnumeros(lista) == True : 
    print ("Todos los elementos son numeros")
else: 
    print ("No todos los elementos son numeros")
   

#Encontrar la Cadena Más Larga

def larga(lista):
    if not lista:
        print("La lista está vacía")
    else:
        print(max((s for s in lista if isinstance(s, str)), key=len, default=""))

larga(lista)        

#Contar Cadenas que Empiezan con Vocal

def vocal(lista):
    vocales = "aeiouAEIOU"
    print(sum(1 for s in lista if isinstance(s, str) and s[0] in vocales))

vocal(lista)

#Verificar si una Lista Contiene Números Primos

def hayPrimos(lista):
    def primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    if any(primo(x) for x in lista if isinstance(x, int)):
        print("La lista contiene números primos")
    else:
        print("No hay números primos en la lista")

hayPrimos(lista)        
