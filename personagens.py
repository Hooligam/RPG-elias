#Classe base para os personagens do jogo

class Personagem:
    def __init__(self, nome, vida, ataque, nivel=1, xp=0):
        self.nome = nome
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.xp = xp
        self.ouro = 0

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 5
        self.ataque += 2
        return print(f'{self.nome} subiu para o nível {self.nivel}')
    
    def ganhar_xp(self, xp):
        self.xp += xp
        if self.xp >= 100:
            self.subir_nivel()
            self.xp = 0
        return print(f'{self.nome} ganhou {xp} de xp')
    
    def ganhar_ouro(self, ouro):
        self.ouro += ouro
        return print(f'{self.nome} ganhou {ouro} de ouro')
    
    def ataque(self, inimigo):
        inimigo.vida -= self.ataque
        return print(f'{self.nome} atacou {inimigo.nome} e causou {self.ataque} de dano')
    
    def vivo(self):
        if self.vida > 0:
            return print(f"{self.nome} esta vivo com {self.vida} de vida")
        else:
            return print(f"{self.nome} esta morto") 

    def status(self):
        return print(f'{self.nome}\nNível: {self.nivel}\nVida: {self.vida}\nAtaque: {self.ataque}\nXP: {self.xp}\nOuro: {self.ouro}')


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 65, 70)
    
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 80, 55)

class Assassino(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 60, 75)

class Sacerdote(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 90, 40)