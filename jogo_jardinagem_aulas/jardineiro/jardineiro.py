import random
from .helper import Helper
from plantas.alface import Alface
from plantas.cenoura import Cenoura
from plantas.tomate import Tomate

class Jardineiro:
    """Representa um jardineiro que pode plantar, regar e recolher plantas."""

    def __init__(self, nome):
        self.nome = nome
        self.plantas_plantadas = []
        self.inventario = {}
        self.points = 0
        self.plantas_disponiveis = {"tomate": Tomate, "alface": Alface, "cenoura": Cenoura}

    def plantar(self):
        planta_selecionada = Helper().seleccionar_item(self.inventario)
        self.inventario[planta_selecionada] -= 1
        self.plantas_plantadas.append(self.plantas_disponiveis[planta_selecionada]())
        print(f"Plantaste uma semente de {planta_selecionada}!")
        if self.inventario[planta_selecionada] == 0:
            del self.inventario[planta_selecionada]
        # Testes
        print(self.plantas_plantadas)
        print(self.inventario)

    def regar(self):
        for planta in self.plantas_plantadas:
            planta.crescer()
    
    def recolher(self):
        planta_seleccionada = Helper().seleccionar_item(self.plantas_plantadas)
        # completar

    def inventario(self):
        print(f"O teu inventário é: {self.inventario}") 

    def procurar(self):
        newSeed = random.choice(list(self.plantas_disponiveis.keys()))
        print(f"Encontraste uma semente de {newSeed}!")
        if newSeed in self.inventario:
            self.inventario[newSeed] += 1
        else:
            self.inventario[newSeed] = 1