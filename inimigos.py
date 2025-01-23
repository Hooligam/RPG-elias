from personagens import Personagem

class inimigos:
    def __init__(self, nome, vida, dano, drop_xp):
        self.nome = nome   
        self.vida = vida
        self.dano = dano
        self.drop_xp = drop_xp

    def status(self):
        return print(f'{self.nome}\n {self.vida}\n {self.dano}\n Caso abatido esse monstro dropa {self.drop_xp} de XP.')

    def vivo(self):
        if self.vida > 0:
            return print(f"{self.nome} esta vivo com {self.vida} de vida")
        else:
            return print(f"{self.nome} esta morto")

# com erro, precisa ser implementado
    def ataque(self):
        dano = self.dano 
        Personagem.vida -= dano

class Dragao(inimigos):
    def __init__(self):
        super().__init__( "Dragao", 2000, 40, 100)

class Goblin(inimigos):
    def __init__(self):
        super().__init__( "Goblin", 40, 15, 25)

class Esqueleto(inimigos):
    def __init__(self):
        super().__init__( "Esqueleto", 30, 10, 20)
