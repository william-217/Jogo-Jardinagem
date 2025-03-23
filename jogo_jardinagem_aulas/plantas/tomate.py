from plantas.planta import Planta

class Tomate(Planta):
    def __init__(self):
        super().__init__("Tomate", 10)
        self.estado_crescimento = ["semente", "rebento", "madura", "flor", "fruta", "pronto-recolher"]