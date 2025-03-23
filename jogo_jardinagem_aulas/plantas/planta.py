class Planta:
    def __init__(self, nome, rendimento_colheita):
        self.nome = nome
        self.estado_crescimento = ["semente", "rebento", "madura", "flor", "fruta", "pronto-recolher"]
        self.__estado_atual = 0
        self.nome_estado_crescimento = self.estado_crescimento[0]
        self.__pronto_recolher = False

    def crescer(self):
        self.__estado_atual += 1

        if self.estado_atual == len(self.estado_crescimento) -1:
            self.__pronto_recolher = True

    def recolher(self):
        pass

    def obter_nome_estado_actual(self):
        return self.estado_crescimento[self.__estado_atual]
    
    @property
    def pronto_recolher(self):
        return self.__pronto_recolher
    
    @property
    def check_status(self):
        return self.__estado_atual