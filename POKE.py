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
    def get_nombre(nom):
        return self.__nombre
    def set_locaizacion(self,locali):
        self.__localizacion=locali
    def get_locaizacion(locali):
        return self.__localizacion
    def set_tipo(self,tip):
        self.__tipo=tip
    def get_tipo(tip):
        return self.__tipo
    def set_evolucion(self,evolu):
        self.__evolucion=evolu
    def get_evolucion(evolu):
        return self.__evolucion
    def set_nivel(self,nive):
        self.__nivel=nive
    def get_nivel(nive):
        return self.__nivel
    def set_cantidad(self,cant):
        self.__cantidad=cant
    def get_cantidad(cant):
        return self.__cantidad
class Elementop(Pokemon):
    def __init__(self,ele,nom,locali,tip,evolu,nive,cant):
        super().__init__(nom,locali,tip,evolu,nive,cant)
        self.__elemento=ele
    def set_elemento(self,ele):
        self.__elemento=ele
    def get_elemento(ele):
        return self.__elemento
class Elementos(Elementop):
     def __init__(self,sele,ele,nom,locali,tip,evolu,nive,cant):
        super().__init__(ele,nom,locali,tip,evolu,nive,cant)
        self.__secundario=sele
     def set_secundario(self,sele):
        self.__secundario=sele
     def get_secundario(sele):
        return self.__secundario
def anadir():
    nom=input("Nombre: ")
    locali=input("Localización de captura: ")
    tip=input("Tipo: ")
    evolu=input("Nivel de evoución: ")
    nive=input("Nivel: ")
    elemento=input("¿Tiene un elemento específico? ¿si o no?")
    if elemento.lower()=="si" or elemento.lower()=="sí":
        ele=input("Elemento principal: ")
        secu=input("¿Tiene más de un elemento específico? ¿si o no? ")
        if secu.lower()=="si" or secu.lower()=="sí":
            sele=input("Elemento secundario: ")
            cant="2"
            mipoke=Elementos(sele,ele,nom,locali,tip,evolu,nive,cant)
        else:
            cant="1"
            mipoke=Elementop(ele,nom,locali,tip,evolu,nive,cant)
    else:
        cant="0"
        mipoke=Pokemon(nom,locali,tip,evolu,nive,cant)
    pokedex.append(mipoke)
def info():
    busca=input("Qué pokemon busca? ")
    if busca in pokedex:
        if pokedex[busca].get_cantidad()=="1":
            print (pokedex[busca].get_elemento)
        elif pokedex[busca].get_cantidad()=="2":
            print(pokedex[busca].get_elemento)
            print(pokedex[busca].get_secundario)
    print(pokedex[busca].get_nombre())
    print(pokedex[busca].get_localizacion())
    print(pokedex[busca].get_tipo())
    print(pokedex[busca].get_evolucion())
    print(pokedex[busca].get_nivel())
if __name__=="__main__":
    pokedex=[]
    respuesta="poke"
    x="o"
    while x!="7" :
         print("Si quiere añadir un pokemon pulse 1")
         print("Si quiere buscar la información de un pokemon pulse 2")
         print("Si quiere eliminar un pokemon pulse 3")
         print("Si quiere ver todos los pokemons de un elemento(s) pulse 4")
         print("Para buscar los 6 pokemon de más nivel para combatir pulse 5")
         print("Para ver todos mis pokemon pulse 6")
         print("Para salir de la Pokedex pulse 7")
         x=input("Introduce: ")
         if x=="1":
             anadir()
         elif x=="2":
             info()
         elif x=="3":
             anadir()
         elif x=="4":
             anadir()
         elif x=="5":
             anadir()
         elif x=="6":
             anadir()
     
     