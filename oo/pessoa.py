class Pessoa:
    olhos=2
    def __init__(self,*filhos, nome=None,idade=35):
        self.idade=idade
        self.nome=nome
        self.filhos=list(filhos)



    def cumprimentar(self):
        return f'ola {id(self)}'




if __name__ == '__main__':
    renzo = Pessoa(nome='renzo')
    luciano=Pessoa(renzo, nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
     print(filho.nome)
    luciano.sobrenome='tarcisio'
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)

    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)