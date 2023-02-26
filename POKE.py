'''def anadir():
    nom = input("Nombre: ")
    locali = input("Localización de captura: ")
    tip = input("Tipo: ")
    evolu = input("Nivel de evolución: ")
    nive = input("Nivel: ")
    elemento = input("¿Tiene un elemento específico? ¿si o no?")

    if elemento.lower() == "si" or elemento.lower() == "sí":
        ele = input("Elemento principal: ")
        secu = input("¿Tiene más de un elemento específico? ¿si o no? ")
        if secu.lower() == "si" or secu.lower() == "sí":
            sele = input("Elemento secundario: ")
            cant = "2"
            mipoke = Elementos(sele, ele, nom, locali, tip, evolu, nive, cant)
        else:
            cant = "1"
            mipoke = Elementop(ele, nom, locali, tip, evolu, nive, cant)
    else:
        cant = "0"
        mipoke = Pokemon(nom, locali, tip, evolu, nive, cant)

    pokedex.append(mipoke) # Agregar el nuevo objeto a la lista'''


''' def info():
    busca=input("Qué pokemon busca? ")
    
    if busca in pokedex:
        if pokedex[posi].get_cantidad()=="1":
            print (pokedex[posi].get_elemento())
        elif pokedex[posi].get_cantidad()=="2":
            print(pokedex[posi].get_elemento())
            print(pokedex[posi].get_secundario())
        print(pokedex[posi].get_nombre())
        print(pokedex[posi].get_localizacion())
        print(pokedex[posi].get_tipo())
        print(pokedex[posi].get_evolucion())
        print(pokedex[posi].get_nivel())
    else:
        print("Este pokemon no está registrado en la pokedex.")'''



class Pokemon:
    def __init__(self,nom,locali,tip,evolu,nive,cant):
        self.__nombre=nom
        self.__localizacion=locali
        self.__tipo=tip
        self.__evolucion=evolu
        self.__nivel=nive
        self.__cantidad=cant
        
    def set_nombre(self,nom):
        self.__nombre=nom
    def get_nombre(self):
        return self.__nombre
    
    def set_localizacion(self,locali):
        self.__localizacion=locali
    def get_localizacion(self):
        return self.__localizacion
    
    def set_tipo(self,tip):
        self.__tipo=tip
    def get_tipo(self):
        return self.__tipo
    
    def set_evolucion(self,evolu):
        self.__evolucion=evolu
    def get_evolucion(self):
        return self.__evolucion
    
    def set_nivel(self,nive):
        self.__nivel=nive
    def get_nivel(self):
        return self.__nivel
    
    def set_cantidad(self,cant):
        self.__cantidad=cant
    def get_cantidad(self):
        return self.__cantidad
    
    
class Elementop(Pokemon):
    def __init__(self,ele,nom,locali,tip,evolu,nive,cant):
        super().__init__(nom,locali,tip,evolu,nive,cant)
        self.__elemento=ele
    def set_elemento(self,ele):
        self.__elemento=ele
    def get_elemento(self):
        return self.__elemento
class Elementos(Elementop):
     def __init__(self,sele,ele,nom,locali,tip,evolu,nive,cant):
        super().__init__(ele,nom,locali,tip,evolu,nive,cant)
        self.__secundario=sele
     def set_secundario(self,sele):
        self.__secundario=sele
     def get_secundario(self):
        return self.__secundario


def agregar_pokemon():
    nom = input("Nombre: ")
    locali = input("Localización de captura: ")
    tip = input("Tipo: ")
    evolu = input("Nivel de evolución: ")
    nive = input("Nivel: ")
    elemento = input("¿Tiene un elemento específico? ¿si o no?")

    if elemento.lower() == "si" or elemento.lower() == "sí":
        ele = input("Elemento principal: ")
        secu = input("¿Tiene más de un elemento específico? ¿si o no? ")
        if secu.lower() == "si" or secu.lower() == "sí":
            sele = input("Elemento secundario: ")
            cant = "2"
            nuevo_pokemon = Elementos(sele, ele, nom, locali, tip, evolu, nive, cant)
        else:
            cant = "1"
            nuevo_pokemon = Elementop(ele, nom, locali, tip, evolu, nive, cant)
    else:
        cant = "0"
        nuevo_pokemon = Pokemon(nom, locali, tip, evolu, nive, cant)
        
    pokedex.append(nuevo_pokemon)
    
    
def mostrar_pokemon():
    for pokemon in pokedex:
        print("Nombre:", pokemon.get_nombre())
        print("Localización:", pokemon.get_localizacion())
        print("Tipo:", pokemon.get_tipo())
        print("Evolución:", pokemon.get_evolucion())
        print("Nivel:", pokemon.get_nivel())
        if pokemon.get_cantidad() == '1':
            print("Elemento:", pokemon.get_elemento())
            if pokemon.get_cantidad() == '2':
                print("Elemento secundario:", pokemon.get_secundario())

        print("------------------------------")
        
        
    
def buscador():
    nombre_pokemon = input("Ingrese el nombre del pokemon que desea buscar: ")
    for pokemon in pokedex:
        if pokemon.get_nombre() == nombre_pokemon:
            print("Nombre:", pokemon.get_nombre())
            print("Localización:", pokemon.get_localizacion())
            print("Tipo:", pokemon.get_tipo())
            print("Evolución:", pokemon.get_evolucion())
            print("Nivel:", pokemon.get_nivel())
            if pokemon.get_cantidad() == '1':
                print("Elemento:", pokemon.get_elemento())
                if pokemon.get_cantidad() == '2':
                    print("Elemento secundario:", pokemon.get_secundario())
        else:
            print("Pokemon no encontrado en la pokedex.")
    print("------------------------------")      
        
def eliminar():
    nombre_pokemon = input("Ingrese el nombre del pokemon que desea eliminar: ")
    for pokemon in pokedex:
        if pokemon.get_nombre() == nombre_pokemon:
            pokedex.remove(pokemon)
            print('Pokemon eliminado')
        else:
            print("Pokemon no encontrado en la pokedex.")
    print("------------------------------")
        
        
if __name__=="__main__":
    pokedex=[]
    x="o"
    while x!="5" :
         print("Si quiere añadir un pokemon pulse 1")
         print("Si quiere buscar la información de un pokemon pulse 2")
         print("Si quiere eliminar un pokemon pulse 3")
         print("Para ver todos mis pokemon pulse 4")
         print("Para salir de la Pokedex pulse 5")
         x=input("Introduce: ")
         if x=="1":
             agregar_pokemon()
         elif x=="2":
             buscador()
         elif x=="3":
             eliminar()
         elif x=="4":
             mostrar_pokemon()
             
     