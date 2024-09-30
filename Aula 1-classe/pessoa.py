class Pessoa:
    #atributos
    nome = "Fulano"
    peso = 71
    escolaridade = "Ensino Médio"

    #métodos
    def falar(self, texto):
        print(f"Tenho algo para dizer: {texto}")


 #CRIANDO OS OBJETOS
pessoal = Pessoa()
print(pessoal.nome)     
pessoal.falar("Boa tarde, hoje é segunda-feira") 