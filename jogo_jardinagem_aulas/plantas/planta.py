class Planta:
    def __init__(self, nome, rendimento_colheita):
        self.nome = nome
        self.rendimento = rendimento_colheita
        self.estado_crescimento = ["semente", "rebento", "madura", "flor", "fruta", "pronto-recolher"]
        self.__estado_atual = 0
        self.nome_estado_crescimento = self.estado_crescimento[0]
        self.__pronto_recolher = False
        self.__fertilizado = False

    def crescer(self):
        if self.__estado_atual < len(self.estado_crescimento)-1:
            self.__estado_atual += 1
        if self.__estado_atual == len(self.estado_crescimento)-1:
            self.__pronto_recolher = True

    def recolher(self):
        if self.__pronto_recolher == True:
            self.__estado_atual = 0
            return self.rendimento

    def obter_nome_estado_actual(self):
        return self.estado_crescimento[self.__estado_atual]
    
    @property
    def fertilizar(self):
        return self.__fertilizado
    
    @fertilizar.setter
    def fertilizar(self, x):
        self.__fertilizado = x
    
    @property
    def pronto_recolher(self):
        return self.__pronto_recolher
    
    @pronto_recolher.setter
    def pronto_recolher(self, x):
        self.__pronto_recolher = x
    
    @property
    def check_status(self):
        return self.__estado_atual
    
    @check_status.setter
    def check_status(self, x):
        self.__estado_atual += x