"""
voce deve criar uma classe que vai possuir dois atributos compostos opr outras duas classes
1)Motor
2)Direção
 o Motor terá a responsabilidade de controlar a velocidade
 ele oferece os seguintes atributos
 1)atributo de dados velocidade
 2)método acelerar, que deverá incrementar a velocidade em uma unidade
 3)método frear que deverá decrementar a vloccidade em duas unidades

 a direção terá a responsabilidade de controlar a direção. ela oferece os seguintes atributos
 1)valor de direção com valores possiveis: Norte,Sul,Leste,Oeste
 2)método a girar_a_direita
 3)método girar_a_esquerda
   N
O    L
   S
     exemplo:
     >>> #testando motor
     >>>motor=Motor()
     >>>motor.velocidade
     0
     >>>motor.acelerar()
     >>>motor.velocidade
     1
     >>>motor.acelerar()
     >>>motor.velocidade
     2
     >>>motor.acelerar()
     >>>motor.velocidade
     3
     >>>motor.frear()
     >>>motor.velocidade
     1
     >>>motor.acelerar()
     >>>motor.velocidade
     0
     >>>#tesatando direção
     >>>direção=Direção()
     >>>direção.valor
     'Norte'
     >>>direção.girar_a_direita()
     >>>direção.valor
      'Leste'
     >>>direção.girar_a_direita()
     >>>direção.valor
     'Sul'
     >>>direção.girar_a_direita()
     >>>direção.valor
     'oste'
     >>>direção.girar_a_direita()
     >>>direção.valor
     'Norte'
     >>>direção.girar_a_esquerda()
     >>>direção.valor
     'Oeste'
     >>>direção.girar_a_esquerda()
     >>>direção.valor
     'Sul'
     >>>direção.girar_a_esquerda()
     >>>direção.valor
     'Leste'
     >>>direção.girar_a_esquerda()
     >>>direção.valor
     'Norte'
     >>>carro=Carro(direção,motor)
     >>>carro.calcular.velocidade()
     0
     >>>carro.acelerar()
     >>>carro.calcular.velocidade()
     1
     >>>carro.acelerar()
     >>>carro.calcular.velocidade()
     2
     >>>carro.frear()
     >>>carro.calcular.velocidade()
     0
     >>>carro.calcular_direção()
     'Norte'
     >>>carro.girar_a_direita()
     >>>carro.calcular_direção()
     'Leste'
     >>>carro.girar_a_esquerda()
     >>>carro.calcular_direção()
     'Norte'
     >>>carro.girar_a_esquerda()
     >>>carro.calcular_direção()
     'Oeste'
"""
class Carro:
    def __init__(self,direção,motor):
        self.direção=direção
        self.motor=motor
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()
    def calcular_direcao(self):
        return self.direcao.valor
    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'

class Direcao:
    rotacao_a_direita={NORTE: LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    rotacao_a_esquerda = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}
    def __init__(self):
        self.valor=NORTE

    def girar_a_direita(self):
        self.valor=self.rotacao_a_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda[self.valor]




class Motor:
    def __init__(self):
        self.velocidade=0
    def acelerar(self):
        self.velocidade+=1
    def frear(self):
        self.velocidade-=2
        self.velocidade=max(0, self.velocidade)