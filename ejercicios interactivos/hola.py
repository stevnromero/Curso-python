
"""lista_personajes = ["spider-man", "iron man", "hulk"]
nueva = []


nueva.append("capital america")
nueva.extend(lista_personajes)
for marvel in nueva:
    print(f"los personajes de marvel son: {marvel}")
    
    if marvel in nueva[0]:
        print("esta en la nueva lista")
  

longitudes = tuple(map(lambda heroes: len(heroes), nueva))
print(longitudes)"""


"""lista_personajes = ["spider-man", "iron man", "hulk"]
lista2 = ["mr fantastico"]
nueva = lista_personajes + lista2
print(nueva)


def comic(name):
    if name in nueva:
        print("he is here")
    else:
        print("no esta en la lista")

heroes = filter(comic,nueva)

for name in heroes:
    print(name)

def comic(hero):
    return "s" in hero

name = tuple(filter(lambda x: "s" in x, nueva))
print(name)
"""

"""couple = ["steven"]
couple2 = ["juanita"]

for pareja in couple:
    fusion= []
    fusion.append(pareja)
    for pareja2 in couple2:
        fusion.append(pareja2)
        print(fusion)


love = tuple(map(lambda amor: len(amor), fusion))
print(love)"""


"""lista = ["alejandra", "sergio", "ricardo"]
lista2 = "emanuel"


for aprendiz in (lista2, lista):
    nueva = []
    nueva.append(lista2)
    nueva.extend(lista)
    nueva.sort()
    pass

for i, nuevaLista in enumerate(nueva, start= 1):
    print(f"los aprendices son {nuevaLista}. es el numero {i}")"""


"""def multiplicacion(numero1):
    numero2= 5
    mayor = max(numero1,numero2)
    print("el numero mayor es:", mayor)
    return numero2 * numero1
print("el resultado de la multiplicacion es:",multiplicacion(2))
"""

    







