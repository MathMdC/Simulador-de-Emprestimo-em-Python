#Simulador de Cadastro e Análise de Crédito

'''
O objetivo é criar um programa que "cadastre" (não é integrado a nenhum banco de dados) e análise o perfil
para julgar se é possível realizar um empréstimo com base nos dados fornecidos pelo usuário.
'''

#Declaração de variáveis

import sys
nome = input(f'Olá, qual é o seu nome?\n').strip()
idade = int(input(f'Que nome bonito {nome}! E qual é a sua idade?\n'))

if idade < 18:
    print(f'Desculpe {nome}, mas como você é de menor é necessário abrir a conta com um responsável.')
    sys.exit()
else:
    print(f'---Castros LTDA---\nBem vindo {nome}!')

print(f'Para começar precisamos de mais alguns de seus dados...\n')
profissao = input(f'Gostariamos de começar conhecendo mais sobre você {nome}, qual é a sua profissão?\n').strip()
salario_bruto = float(input(f'Qual é o seu salário bruto?\n'))

#HOME do programa
print(f'---Castros LTDA---\nO que você deseja:\n1. Alterar dados\n2. Consultar Empréstimo')
selecao = int(input(':'))

match selecao:
    #Página de alteração de dados
    case 1 :
        print(f'---Castros LTDA---\nQual dado deseja alterar {nome}?\n'
         f'1. Nome {nome}\n2. Profissão {profissao}\n3. Salário Bruto R${salario_bruto}\n')
        selecao_dados = int(input())
        match selecao_dados:
            case 1:
                nome = input(f'---Castros LTDA---\nSeu nome atual é {nome}, digite o seu novo nome:\n').strip()
            case 2:
                profissao = input(f'---Castros LTDA---\n'
                                  f'Sua profissão atual está como {profissao}, digite a sua nova profissão:\n').strip()
            case 3:
                salario_bruto = float(input(f'---Castros LTDA---\n'
                                          f'Seu salário atual é de {salario_bruto}, digite o seu novo salário:\n'))
    #Página de empréstimos
    case 2:
        print(f'---Castros LTDA---\nBem vindo {nome} a Consulta de Empréstimo!\n')
        valor_emprestimo = int(input(f'Qual é o valor desejado para empréstimo?\n'))
        parcela = valor_emprestimo / 12

        if parcela <= float(0.3 * salario_bruto):
            print(f'Que maravilha {nome} seu empréstimo foi APROVADO!\n'
                  f'Você pagará 12 x R$ {parcela:.2f} (Em caso de atraso será cobrado 5% de juros.)')
        else:
            print(f'Infelizmente {nome} o valor desejado foi REPROVADO pois está acima do seu limite.')







