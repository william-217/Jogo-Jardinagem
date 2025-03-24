from plantas.planta import Planta
import random

class Batata(Planta):
    def __init__(self):
        super().__init__("Batata", 12)
        self.estado_crescimento = ["semente", "rebento", "madura", "pronto-recolher"]
        self.fertilizar = True

    def crescer(self):
        if self.fertilizar == True:
            if self.check_status < len(self.estado_crescimento)-1:
                if self.check_status < len(self.estado_crescimento)-2:
                    self.check_status = 2
                else:
                    self.check_status = 1
            if self.check_status == len(self.estado_crescimento)-1:
                self.pronto_recolher = True

    