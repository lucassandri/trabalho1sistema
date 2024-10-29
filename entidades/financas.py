from controladores.controlador_aluno import ControladorAlunos
from controladores.controllerProfessor import ControladorProfessor
from controladores.controllerFuncionario import ControladorFuncionarios
from entidades.sistema import *

class Financas:

    def __init__(self):
        self.__controlador_professor = ControladorProfessor()
        self.__lista_alunos = ControladorAlunos.
        self.__lista_funcionarios = ControladorFuncionarios.
        self.__lista_professores = ControladorProfessor.


    def faturamento_escola():
        faturamento = 0
        for aluno in Sistema.lista_alunos:
            faturamento += aluno.mensalidade
        return float(faturamento)
    
    def despesa_escola(self):
        despesa = 0
        for professor in self.__controlador_professor.professores:
            despesa += professor.salario
        for funcionario in Sistema.lista_funcionarios:
            despesa += funcionario.salario
        return float(despesa)

    
    def lucro_escola(self):
        lucro = self.faturamento_escola() - self.despesa_escola()
        return float(lucro)