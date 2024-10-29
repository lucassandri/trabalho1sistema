class TelaFinancas():
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- ALUNOS ----------")
    print("Escolha a opcao")
    print("1 - Ver Faturamento da Instituição")
    print("2 - Ver Despesa da Instituição")
    print("3 - Ver Lucro da Instituição")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    from controladores.controllerFinancas import ControllerFinancas
    return opcao
  
  def ver_faturamento(self, valor):
    from controladores.controllerFinancas import ControllerFinancas
    print("-------- Faturamento da Instituição ----------")
    print(f"O Faturamento da instituição é de R$: {valor}")

  def ver_despesa(self, valor):
    from controladores.controllerFinancas import ControllerFinancas
    print("-------- Despesa da instituição ----------")
    print(f"A Despesa da instituição é de R$: {valor}")


  def ver_lucro(self, valor):
    from controladores.controllerFinancas import ControllerFinancas
    print("-------- Lucro da Instituição ----------")
    print(f"O Lucro da instituição é de R$: {valor}")


  def mostra_mensagem(self, msg):
    print(msg)