class Carro:
	def __init__(self, id, marca, modelo, ano, preco):
		self.id = id
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.preco = preco

	def para_dict(self):
		return {
			"id": self.id,
			"marca": self.marca,
			"modelo": self.modelo,
			"ano": self.ano,
			"preco": self.preco,
		}


carros = [
	Carro(1, "Toyota", "Corolla", 2023, 145000.00),
	Carro(2, "Honda", "Civic", 2022, 138000.00),
	Carro(3, "Volkswagen", "T-Cross", 2024, 152000.00),
]

def listar_carros() -> list[dict]:
	"""Devolve todos os carros para serem usados pelo app.py."""
	return [carro.para_dict() for carro in carros]
