import random

def mostrar_menu():
    '''
    Essa função serve para o usuário escolher a opção quer quiser assim será redirecionado para ela.

    Parâmetros ()

    Retornará a escolha feita pelo o usuário.
    '''
    escolha = 0
    while escolha < 1 or escolha > 5:
        print("Bem-vindo ao SeaCure!!!")
        print("Escolha uma das opções abaixo:")
        print("1 - Registrar uma ocorrência")
        print("2 - Consultar ocorrências registradas")
        print("3 - Ver informações educativas e curiosidades")
        print("4 - Quiz sobre as curiosidades, para saber se você entendeu bem as informações")
        print("5 - Sair")
        escolha = int(input('Digite um opção desejada: '))
        if (escolha < 1 or escolha > 5):
            print('Opção inválida')
        else:
            return escolha
        
def registrarOcorrencia(ocorrencias): #fazer uma lista no main para a ocorrencias #da para fazer com json e pick #estamos usando o parâmetro pq queremos passar a
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

def escolhaInformacoes():
    '''
    Essa função serve para o usuário escolher a opção para assim depois saber a curiosidade.

    Parâmetros ()

    Retornará a opcao feita pelo o usuário.
    '''
    opcao = -1
    while opcao < 1 or opcao > 5:
        print('1 - Corais')
        print('2 - Peixes em extinção')
        print('3 - Pesca sustentável')
        print('4 - Clima e Oceano')
        print('5 - Redução do lixo ')
        opcao = int(input('Digite uma opção: '))
        if opcao < 1 or opcao > 5:
            print('Opção inválida. Tente novamente')
            print('------- / --------- / --------- / ---------- /')
    return opcao

def informacao(opcao):
    '''
    Essa função serve para receber a opcao e retornar a escolha dele. 
    (Foi utilizado lista ao invés do print, por causa se quiser mudar alguma coisa é mais fácil de manipular)

    Parâmetros (opcao)

    Retornará a cursiosidade escolhida pelo o usuário.
    '''
    curiosidades = [
        '''
        O branqueamento dos corais, que afeta 54 países, é um problema sério que ameaça a pesca, o turismo e o clima. Esses recifes,
        vitais para a biodiversidade marinha, são impactados por diversos fatores, incluindo o aumento da temperatura da água. É crucial
        tomar medidas como reduzir a poluição e combater as mudanças climáticas para protegê-los. A preservação dos recifes de corais é 
        essencial para a saúde do planeta.''',

        '''
        A vida marinha enfrenta um futuro sombrio devido à sobrepesca, poluição, mudanças climáticas e destruição do habitat. Essas 
        ameaças dizimam populações, sufocam oceanos com plástico, danificam ecossistemas e devastam habitats costeiros. Para proteger 
        nossos oceanos e garantir a saúde do planeta, medidas urgentes como áreas marinhas protegidas, pesca regulamentada e redução 
        do plástico descartável são cruciais.''', 

        '''
        A sobrepesca devasta populações de peixes, desequilibra ecossistemas marinhos, prejudica comunidades costeiras e compromete 
        a segurança alimentar. Combater essa crise exige gestão pesqueira sustentável e conscientização sobre a preservação dos oceanos.''',

        '''
        Oceano e clima se influenciam: calor é absorvido e liberado, impactando temperatura e vento. Correntes transportam calor e 
        umidade, afetando chuva e temperatura em diversas regiões. Mudanças nos oceanos, como aquecimento e acidificação, impactam 
        significativamente o clima global. Os oceanos regulam o CO2 na atmosfera, sendo cruciais na mitigação das mudanças climáticas. 
        Compreender essa relação é essencial para agir contra as mudanças climáticas e proteger a saúde dos oceanos e do planeta.''', 
                    
        '''
        O lixo plástico nos oceanos, especialmente os microplásticos, representa uma grave ameaça aos ecossistemas marinhos. 
        Milhões de toneladas de plástico são descartadas nos oceanos anualmente, causando danos à vida marinha e aos habitats. Os 
        microplásticos, em particular, são ingeridos por organismos marinhos, causando problemas de saúde e morte.'''
    ]
    
    return curiosidades[opcao - 1]

def quiz():
    '''
    Essa função serve para armazenar as perguntas, alternativas e resposta da lista de dicionário 

    Parâmetros ()

    Retornará a lista perguntas
    '''
    
    perguntas = [
            {
                "pergunta": 'Qual é um dos principais problemas que os recifes de corais enfrentam atualmente?',
                "alternativas": ['1 - Aumento do nível do mar', '2 - Branqueamento dos corais', '3 - Poluição por petróleo'],
                "resposta": 2
            },
            {
                "pergunta": 'Qual é uma medida crucial para proteger os recifes de corais?',
                "alternativas": ['1 - Aumentar a pesca', '2 - Reduzir a quantidade de barcos turísticos', '3 - Combater as mudanças climáticas'],
                "resposta": 3
            },
            {
                "pergunta": 'Quais são algumas das principais ameaças enfrentadas pela vida marinha?',
                "alternativas": ['1 - Sobrepesca, poluição e mudanças climáticas', '2 - Tsunamis e furacões', '3 - Desmatamento e mineração'],
                "resposta": 1
            },
            {
                "pergunta": 'O que sufoca os oceanos e prejudica a vida marinha?',
                "alternativas": ['1 - Plástico', '2 - Poeira do deserto', '3 - Excesso de algas'],
                "resposta": 1
            },
            {
                "pergunta": 'O que é necessário para combater a crise da sobrepesca?',
                "alternativas": ['1 - Reduzir a proteção de áreas marinhas', '2 - Aumentar a captura de peixes', '3 - Gestão pesqueira sustentável e conscientização'],
                "resposta": 3
            },
            {
                "pergunta": 'O que a sobrepesca causa às populações de peixes?',
                "alternativas": ['1 - Aumenta sua diversidade', '2 - Devasta as populações', '3 - Estimula seu crescimento'],
                "resposta": 2
            },
            {
                "pergunta": 'Como as correntes oceânicas afetam as condições climáticas em diferentes regiões?',
                "alternativas": ['1 - Transportam calor e umidade, afetando chuva e temperatura', '2 - Tornam o clima mais estável', '3 - Elas não têm impacto no clima'],
                "resposta": 1
            },
            {
                "pergunta": 'Por que é importante compreender a relação entre o oceano e o clima?',
                "alternativas": ['1 - Para aumentar o turismo nas praias', '2 - Para proteger a biodiversidade marinha', '3 - Para agir contra as mudanças climáticas e proteger a saúde dos oceanos e do planeta'],
                "resposta": 3
            },
            {
                "pergunta": 'Qual é uma das principais ameaças aos ecossistemas marinhos?',
                "alternativas": ['1 - Aumento da temperatura da água', '2 - Lixo plástico nos oceanos', '3 - Desmatamento das florestas tropicais'],
                "resposta": 2
            },
            {
                "pergunta": 'O que acontece com milhões de toneladas de plástico descartadas nos oceanos anualmente?',
                "alternativas": ['1 - São facilmente decompostas pelo oceano', '2 - Causam danos à vida marinha e aos habitats', '3 - São recicladas e reutilizadas'],
                "resposta": 2
            }
        ]
    return perguntas

def pontoQuiz(perguntas):
    '''
    Essa função serve para responder as váriavel perguntas e contar quantos pontos tem

    Parâmetros (perguntas)

    '''
    acertos = 0
    erros = 0

    for q in perguntas:
        print(q["pergunta"])
        for alternativa in q["alternativas"]:
            print(alternativa)
        resposta = int(input("Escolha a alternativa correta (1, 2 ou 3): "))
        if resposta == q["resposta"]:
            acertos += 1
            print("\nResposta correta!")
        else:
            erros += 1
            print("\nResposta incorreta.")

    print(f"\nVocê acertou {acertos} e errou {erros} de um total de {len(perguntas)} questões.")

def controladora(escolha, ocorrencias):
    if escolha == 1:
        ocorrencias = registrarOcorrencia()
        print('------------- / ----------------- / ---------------- / -------')
    elif escolha == 2:
        consultaOcorrencia(ocorrencias)
        print('------------- / ----------------- / ---------------- / -------')

    elif escolha == 3:
        while True:
            opcao = escolhaInformacoes()
            curiosidade = informacao(opcao)
            print(curiosidade)
            print('------------- / ----------------- / ---------------- / -------')
            pergunta = input('Deseja saber mais alguma coisa? (s/n): ').lower()
            if pergunta != 's':
                print("Obrigado por usar a SeaCure!")
                break
            else:
                continue
        print('------------- / ----------------- / ---------------- / -------')

    elif escolha == 4:
        print("Bem-vindo ao Quiz sobre questões marinhas!")
        print("Vamos testar o seu conhecimento e ver quanto acertos e erros você conseguem.")

        perguntas = quiz()
        pontoQuiz(perguntas)
        print('------------- / ----------------- / ---------------- / -------')

    elif escolha == 5:
        print('Muito obrigador por usar o SeaCure')
        print('------------- / ----------------- / ---------------- / -------')
    else:
        ('Você escolheu alguma opção errado')


ocorrencias = []  # Inicialize a lista de ocorrências
#main
while True:
    
    escolha = mostrar_menu()
    controladora(escolha, ocorrencias)


