def quiz():
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
    acertos = 0
    erros = 0

    for q in perguntas:
        print(q["pergunta"])
        for alternativa in q["alternativas"]:
            print(alternativa)
        resposta = int(input("Escolha a alternativa correta (1, 2 ou 3): "))
        if resposta == q["resposta"]:
            acertos += 1
            print("Resposta correta!\n")
        else:
            erros += 1
            print("Resposta incorreta.\n")

    print(f"Você acertou {acertos} e errou {erros} de um total de {len(perguntas)} questões.\n")

def main():
    print("Bem-vindo ao Quiz sobre questões marinhas!")
    print("Responda às perguntas e veja quantos pontos você consegue!")

    perguntas = quiz()
    pontoQuiz(perguntas)

#main
main()