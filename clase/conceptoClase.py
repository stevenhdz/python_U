""" 
def suma(a,b):
  c = a+b """
  

class Persona:
    #metodo o funcion constructor: inicializa las variables o atributos globales a la clase
    def __init__(self, nombre, identificacion, telefono, edad, peso, sexo, estatura):
        self.nombre = nombre
        self.identificacion = identificacion
        self.telefono = telefono
        self.edad = edad
        self.peso = peso
        self.sexo = sexo
        self.estatura = estatura
        
    def imc(self):
      return self.peso/(self.estatura**2) 

    def __eq__(self, persona):
      if self.edad == persona.edad and self.peso == persona.peso and self.estatura == persona.estatura:
        return True
      return False

    def __str__(self):
      h = self.peso/self.estatura**2
      texto = f"""
      Clase Persona
        Nombre: {self.nombre}  
        ID: {self.identificacion}
        Teléfono: {self.telefono}
        Edad: {self.edad}
        Sexo: {self.sexo}
        Peso: {self.peso}
        Estatura: {self.estatura}
        IMC: {round(h, 2)}
      """
      return texto

        