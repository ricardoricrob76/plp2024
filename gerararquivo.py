# Vamos importar a biblioteca para gerar o arquivo .txt
def gerar_frases_atendimento(num_frases):
    # Lista básica de frases de atendimento
    frases = [
        "Olá, como posso ajudá-lo hoje?",
        "Obrigado por entrar em contato. Em que posso ajudar?",
        "Estamos aqui para ajudar! Qual é o seu problema?",
        "Como posso auxiliá-lo com sua solicitação?",
        "Se precisar de assistência, estamos à disposição.",
        "Por favor, forneça mais detalhes sobre o seu problema.",
        "Estamos trabalhando para resolver a sua solicitação.",
        "Desculpe pelo transtorno, vamos resolver isso o mais rápido possível.",
        "Agradecemos seu contato e estamos analisando a sua solicitação.",
        "Qualquer dúvida, não hesite em nos chamar.",
        "Estamos aqui para garantir que você tenha a melhor experiência possível.",
        "Pode me informar mais detalhes para que eu possa ajudar?",
        "Estamos verificando a sua solicitação e em breve entraremos em contato.",
        "Obrigado por seu feedback, é muito importante para nós.",
        "Estamos empenhados em resolver o seu problema o mais rápido possível.",
        "Sua paciência é muito apreciada enquanto trabalhamos na solução.",
        "Por favor, informe o número do seu pedido para que possamos verificar.",
        "Vamos analisar o seu caso e retornaremos em breve.",
        "Se precisar de mais informações, estamos à disposição.",
        "Estamos aqui para ajudar com qualquer questão que você tenha.",
        # Adicione mais frases conforme necessário
    ]

    # Expandindo a lista até ter o número desejado de frases
    while len(frases) < num_frases:
        frases.extend(frases)  # Duplicar frases
        frases = frases[:num_frases]  # Truncate to the desired length

    return frases

def salvar_em_arquivo(frases, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        for frase in frases:
            file.write(frase + '\n')

def main():
    num_frases = 1000  # Número de frases desejadas
    nome_arquivo = 'frases_atendimento.txt'
    
    frases = gerar_frases_atendimento(num_frases)
    salvar_em_arquivo(frases, nome_arquivo)
    print(f"Arquivo '{nome_arquivo}' gerado com {num_frases} frases de atendimento.")

if __name__ == "__main__":
    main()
