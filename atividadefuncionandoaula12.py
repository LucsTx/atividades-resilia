#ATIVIDADE FUNCIONANDO.
#FUNÇAO
def previsaoRodagem (qtdLitros,mediaLitro):
    kmsDisponiveis = qtdLitros * mediaLitro
    return print('Voce ainda pode rodar ', str(kmsDisponiveis), 'quilometros!' )
#_______________________________________________________________________________
#VARIÁVEIS
qtdLitros = float(input('Quantos litros voce abasteceu? \n'))
mediaLitro = float(input('Quantos quilometros seu veiculo faz com 1 litro? \n'))

previsaoRodagem (qtdLitros,mediaLitro)
    