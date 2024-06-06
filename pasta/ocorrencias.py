import random
ocorrencias = []  # Lista para armazenar as ocorrências por causa do diocinário da lista

def registrarOcorrencia(ocorrencias): #fazer uma lista no main para a ocorrencias
    '''
    Essa função serve para o usuário digitar o local e a descrição da ocorrencia assim a empresa ter os dados do lugares que a empresa SeaCure não tem.

    Parâmetros (ocorrencias)

    Retornará a lista da ocorrencias.
    '''
    nome = input('Digite o seu nome: ')
    local = input('Digite o local da ocorrência que será feita: ')
    descricao = input('digite a ocorrência com detalhes: ')
    ocorrencia = {"nome": nome,  #lista com dicionário
                "local": local, 
                "descricao": descricao}
    ocorrencias.append(ocorrencia)
    print('Ocorrência feita com sucesso, você também consegue ver o status dela')
    return ocorrencias

def consultaOcorrencia(ocorrencias):
    '''
    Essa função serve para o usuário receber os dados da lista "ocorrências" e imprimir elas na tela.
    Parâmetros (ocorrencias)

    Retornará
    '''
    if len(ocorrencias) == 0:
        print('Não há nehuma ocorrência registrada')
    else:
        for ocorrencia in ocorrencias:
            status = random.choice(["Enviado", "Em andamento", "Não entregue ainda"])
            print('Ocorrência:')
            print(f'Nome: {ocorrencia["nome"]}')
            print(f'Local: {ocorrencia["local"]}')
            print(f'Descrição: {ocorrencia["descricao"]}')
            print(f'Status: {status}')
            print('------- / -------- / -------- / ------- / ------- /')

def main():

    while True:
        print('\n--- Menu ---')
        print('1. Registrar Ocorrência')
        print('2. Consultar Ocorrências')
        print('3. Sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            ocorrencias = registrarOcorrencia(ocorrencias)
        elif escolha == '2':
            consultaOcorrencia(ocorrencias)
        elif escolha == '3':
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida. Por favor, escolha novamente.')

main()