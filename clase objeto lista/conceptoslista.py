from stack import *

def basico():
    #TODO coleccion de datos
    frutas = ['Manzana','Pera','Banana','UvA','Lulo','Guayaba','Mango','Nispero']
    print(f"Todas las frutas: {frutas}")

    fOrdenadas = sorted(frutas)
    print(f"Ordenas: {fOrdenadas}") 

    frutas.sort()
    print(f"Todas las frutas ordenadas: {frutas}")

    frutas.reverse()
    print(f"Todas las frutas ordenadas invertida: {frutas}")

    print(f"primero fruta: {frutas[0]}")
    print(f"ultimo fruta: {frutas[-1]}")
    print(f"para obtener los n ultimos: {frutas[-2:]}")
    print(f"para obtener los n primeros: {frutas[:2]}")


def main():
    #TODO: PILAS/STACK
    pila = Pila()
    pila.apilar('Manzana')
    pila.apilar('Pera')
    pila.apilar('Lulo')


    print(pila)
    
    print(pila, f" sale: {pila.desapilar()}")
    print(pila, f" sale: {pila.desapilar()}")
    print(pila, f" sale: {pila.desapilar()}") #TODO este ultimo ya salio entraria al error except
    


    #TODO: COLA/QUEUE

if __name__ == '__main__':
  main()