#o programa automaticamente define a funcao, o salario e onde o funcionario trabalho pelo factory

class FuncMecanico:

	def __init__(self):

		self.dados = {
                     "Funcao": "Consertar",
                     "Salario": "5000",
                     "Posto":"Area 2"
                     }

	def converterFunc(self, msg):
		return self.dados.get(msg, msg)

class FuncAtendente:

	def __init__(self):

		self.dados = {
                     "Funcao": "Atender",
                     "Salario": "4000",
                     "Posto":"Area 1"
                     }

	def converterFunc(self, msg):
		return self.dados.get(msg, msg)

class FuncIndefinido:

	def converterFunc(self, msg):
		return msg

def Factory(funcionario ="Indefinido"):

	funcionarios = {
		"Mecanico": FuncMecanico,
		"Atendente": FuncAtendente,
		"Indefinido": FuncIndefinido,
	}

	return funcionarios[funcionario]()

if __name__ == "__main__":

	m = Factory("Mecanico")
	a = Factory("Atendente")
	i = Factory("Indefinido")

	message = ["Funcao", "Salario", "Posto"]

	for msg in message:
		print(m.converterFunc(msg))
		print(a.converterFunc(msg))
		print(i.converterFunc(msg))
