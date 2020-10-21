# fila de prioridades

import heapq

class FilaDePrioridade:

	def __init__(self):
		self._fila = []
		self._indice = 0

	def inserir(self, item, prioridade):
		heapq.heappush(self._fila, (-prioridade, self._indice, item))
		self._indice += 1

	def remover(self):
		return heapq.heappop(self._fila)[-1]


class Pessoa:
	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome


fila = FilaDePrioridade()
fila.inserir(Pessoa('Maria'), 20)
fila.inserir(Pessoa('Pedro'), 16)
fila.inserir(Pessoa('Felipe'), 23)
fila.inserir(Pessoa('Carol'), 23)

print(fila.remover())