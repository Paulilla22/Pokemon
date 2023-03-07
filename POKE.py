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
    elemento = input("¿Tiene un elemento específico? ¿si o no? ")

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
        if pokemon.get_cantidad() == "1":
            print("Elemento:", pokemon.get_elemento())
        elif pokemon.get_cantidad() == "2":
            print("Elemento:", pokemon.get_elemento())
            print("Elemento secundario:", pokemon.get_secundario())

        print("------------------------------")
        
        
    
def buscador():
    nombre_pokemon = input("Ingrese el nombre del pokemon que desea buscar: ")
    comprobar=False
    for pokemon in pokedex:
        if pokemon.get_nombre() == nombre_pokemon:
            comprobar=True
            print("Nombre:", pokemon.get_nombre())
            print("Localización:", pokemon.get_localizacion())
            print("Tipo:", pokemon.get_tipo())
            print("Evolución:", pokemon.get_evolucion())
            print("Nivel:", pokemon.get_nivel())
            if pokemon.get_cantidad() == "1":
                print("Elemento:", pokemon.get_elemento())
            elif pokemon.get_cantidad() == "2":
                print("Elemento:", pokemon.get_elemento())
                print("Elemento secundario:", pokemon.get_secundario())
            break
    if comprobar==False:
        print("Pokemon no encontrado en la pokedex.")
    print("------------------------------")      
        
def eliminar():
    nombre_pokemon = input("Ingrese el nombre del pokemon que desea eliminar: ")
    comprobar=False
    for pokemon in pokedex:
        if pokemon.get_nombre() == nombre_pokemon:
            comprobar=True
            pokedex.remove(pokemon)
            print('Pokemon eliminado')
            break
    if comprobar==False:
        print("Pokemon no encontrado en la pokedex.")
    print("------------------------------")
    
def modificar():
    nombre_pokemon = input("Ingrese el nombre del pokemon que desea modificar: ")
    comprobar=False
    for pokemon in pokedex:
        if pokemon.get_nombre() == nombre_pokemon:
            comprobar=True
            cambio=input("Introduce la característica que desea modificar: ")
            if cambio.lower()=="nombre":
                nom=input("Nombre nuevo: ")
                pokemon.set_nombre(nom)
            elif cambio.lower()=="localizacion":
                locali=input("Localización nueva: ")
                pokemon.set_nombre(locali)
            elif cambio.lower()=="tipo":
                tip=input("Tipo nuevo: ")
                pokemon.set_nombre(tip)
            elif cambio.lower()=="evolucion":
                evolu=input("Evolución nueva: ")
                pokemon.set_nombre(evolu)
            elif cambio.lower()=="nivel":
                nive=input("Nivel nuevo: ")
                pokemon.set_nombre(nive)
            elif cambio.lower()=="elemento":
                ele=input("Elemento nuevo: ")
                pokemon.set_nombre(ele)
            elif cambio.lower()=="elemento secundario":
                sele=input("Elemento secundario nuevo: ")
                pokemon.set_nombre(sele)
            break
    if comprobar==False:
        print("Pokemon no encontrado en la pokedex.")
    print("------------------------------") 
        
        
if __name__=="__main__":
    pokedex=[]
    x="o"
    while x!="6" :
         print("Si quiere añadir un pokemon pulse 1")
         print("Si quiere buscar la información de un pokemon pulse 2")
         print("Si quiere eliminar un pokemon pulse 3")
         print("Para ver todos mis pokemon pulse 4")
         print("Para modificar los datos de algún pokemon pulse 5")
         print("Para salir de la Pokedex pulse 6")
         x=input("Introduce: ")
         if x=="1":
             agregar_pokemon()
         elif x=="2":
             buscador()
         elif x=="3":
             eliminar()
         elif x=="4":
             mostrar_pokemon()
         elif x=="5":
             modificar()
             
     