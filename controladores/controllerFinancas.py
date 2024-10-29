from controladores.controllerProfessor import ControladorProfessor
from telas.tela_financas import TelaFinancas
from entidades.financas import Financas

class ControllerFinancas:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_professor = ControladorProfessor(controlador_sistema)
        self.__tela_financas = TelaFinancas()
        self.__ent_financas = Financas
        pass

    def faturamento_escola(self):
        valor = self.__ent_financas.faturamento_escola()
        self.__tela_financas.ver_faturamento(valor)
    
    def despesa_escola(self):
        valor = self.__ent_financas.despesa_escola()
        self.__tela_financas.ver_despesa(valor)
    
    def lucro_escola(self):
        valor = self.__ent_financas.lucro_escola()
        self.__tela_financas.ver_lucro(valor)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
        
    def abre_tela(self):
        lista_opcoes = {1: self.faturamento_escola, 2: self.despesa_escola, 3: self.lucro_escola, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_financas.tela_opcoes()]()