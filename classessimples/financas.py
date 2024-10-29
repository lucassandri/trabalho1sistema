from controlador_aluno import ControladorAlunos
from controllerProfessor import ControladorProfessor
from controllerFuncionario import ControladorFuncionarios
from entidades.sistema import *

class Financas:
    def faturamento_escola():
        faturamento = 0
        for aluno in Sistema.lista_alunos:
            faturamento += aluno.mensalidade
        return faturamento
    
    def despesa_escola(self):
        despesa = 0
        for professor in self.__controlador_professor.professores:
            despesa += professor.salario
        for funcionario in Sistema.lista_funcionarios:
            despesa += funcionario.salario
        return despesa

    
    def lucro_escola(self):
        lucro = self.faturamento_escola() - self.despesa_escola()
        return lucro