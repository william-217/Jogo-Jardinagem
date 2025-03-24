from plantas.planta import Planta
import random

class Batata(Planta):
    def __init__(self):
        super().__init__("Batata", 12)
        self.estado_crescimento = ["semente", "rebento", "madura", "flor", "fruto" "pronto-recolher"]

    def fertilizar(self):
        self.fertilizado == True

    def crescer(self):
        if self.__estado_atual < len(self.estado_crescimento)-1 and self.fertilizado == True:
            self.__estado_atual += 2
        if self.__estado_atual == len(self.estado_crescimento)-1:
            self.pronto_recolher = True