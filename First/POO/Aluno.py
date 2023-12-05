class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (nota1 + nota2) / 2
        self.situacao = self.verificar_situacao()

    def __str__(self):
        return f"Nome: {self.nome}\nNota 1: {self.nota1}\nNota 2: {self.nota2}\nMédia: {self.media}\nSituação: {self.situacao}"

    def verificar_situacao(self):
        if self.media<0 or self.media>20:
            return "Indefinido"
        elif self.media >= 10:
            return "Aprovado"
        else:
            return "Reprovado"
nome_aluno = "Joao"
nota1_aluno = 18.0
nota2_aluno = 19.0

aluno1 = Aluno(nome_aluno, nota1_aluno, nota2_aluno)
print(aluno1)

help("modules")