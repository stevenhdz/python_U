
class Stack:
    def __init__(self):
        self.collection = []    

    def push(self, data):
        self.collection.append(data)
    
    def pop(self):
        try:
            return self.collection.pop()
        except:
            print('Error in pop')

    def __str__(self):
        text = 'List \n'
        i = 0
        if len(self.collection) > 0:
            for item in self.collection:
                text += f"[{i}]: {item} \n"
                i+=1
            return text
        else:
            return "This list is empty"  

class Pila:
    def __init__(self):            
        self.conjunto = []

    def apilar(self, data):
        self.conjunto.append(data)

    def desapilar(self):
        try:
            return self.conjunto.pop()
        except:
            print('Error en desapilar')

    def __str__(self):
        texto = 'Lista \n'
        i = 0
        if len(self.conjunto) > 0:
            for item in self.conjunto:
                texto += f"[{i}]: {item} \n"
                i+=1
            return texto
        else:
            return "La lista esta vacia"    