import random
from .helper import Helper
from plantas.planta import Planta
from plantas.alface import Alface
from plantas.cenoura import Cenoura
from plantas.tomate import Tomate
from plantas.batata import Batata

class Jardineiro:
    """Representa um jardineiro que pode plantar, regar e recolher plantas."""

    def __init__(self, nome):
        self.nome = nome
        self.plantas_plantadas = []
        self.inventario = {}
        self.points = 0
        self.plantas_disponiveis = {"tomate": Tomate, "alface": Alface, "cenoura": Cenoura, "batata": Batata}

    def plantar(self):
        planta_selecionada = Helper().seleccionar_item(self.inventario)
        self.inventario[planta_selecionada] -= 1
        self.plantas_plantadas.append(self.plantas_disponiveis[planta_selecionada]())
        print(f"Plantaste um rebento de {planta_selecionada}!")
        if self.inventario[planta_selecionada] == 0:
            del self.inventario[planta_selecionada]

    def regar(self):
        for planta in self.plantas_plantadas:
            planta.crescer()
            print(planta.check_status)
            print(planta.pronto_recolher)
    
    def recolher(self):
        planta_selecionada = Helper().seleccionar_item(self.plantas_plantadas)
        for planta_selecionada in self.plantas_plantadas:
            if planta_selecionada.pronto_recolher:
                pontuacao = planta_selecionada.recolher()
                self.plantas_plantadas.remove(planta_selecionada)

                if planta_selecionada in self.inventario:
                    self.inventario[planta_selecionada] += 1
                else:
                    self.inventario[planta_selecionada] = 1

                print(f"Recolheste um/a {planta_selecionada}!")
                self.points += pontuacao

    def inv(self):
        print(f"O teu inventário é: {self.inventario}")

    def pont(self):
        print(f"A tua pontuação é: {self.points}!")

    def procurar(self):
        newSeed = random.choice(list(self.plantas_disponiveis.keys()))
        print(f"Encontraste um rebento de {newSeed}!")
        if newSeed in self.inventario:
            self.inventario[newSeed] += 1
        else:
            self.inventario[newSeed] = 1