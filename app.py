import modelos

print("Nosso App!")

conf = {
    "versao": 1.0,
    "cor":"Azul"
}

print(conf)

print("\nCarros disponíveis:")
for carro in modelos.listar_carros():
    print(f"{carro['marca']} {carro['modelo']} - Ano: {carro['ano']} - Preço: R${carro['preco']:.2f}")
