import random

def gerar_frases_api():
    return [
        "Como posso auxiliá-lo com o teste da API da DATAPREV hoje?",
        "Você encontrou algum problema ao integrar com a API da DATAPREV?",
        "Estamos aqui para ajudar com a documentação da API da DATAPREV.",
        "Podemos revisar a resposta da API da DATAPREV para identificar qualquer falha.",
        "Precisa de suporte para configurar testes automatizados para a API da DATAPREV?",
        "Vamos verificar os logs da API da DATAPREV para solucionar o problema.",
        "Você já tentou testar a API da DATAPREV com diferentes cenários de entrada?",
        "Estamos analisando a performance da API da DATAPREV com base nos resultados dos testes.",
        "A API da DATAPREV está respondendo conforme o esperado em seu ambiente de teste?",
        "Podemos ajudá-lo a simular diferentes cargas na API da DATAPREV para avaliação.",
        "Vamos preparar um relatório detalhado dos testes realizados na API da DATAPREV.",
        "Você encontrou algum erro específico ao utilizar a API da DATAPREV?",
        "Estamos realizando um teste de carga na API da DATAPREV para verificar a capacidade.",
        "Precisamos verificar a configuração do servidor da API da DATAPREV.",
        "Pode nos fornecer mais detalhes sobre o erro encontrado na API da DATAPREV?",
        "Estamos trabalhando para resolver qualquer problema relacionado à API da DATAPREV.",
        "Você já considerou automatizar os testes da API da DATAPREV para maior eficiência?",
        "Estamos ajustando as configurações da API da DATAPREV para melhorar a performance.",
        "Vamos revisar os parâmetros utilizados nos testes da API da DATAPREV.",
        "Estamos disponíveis para resolver qualquer questão sobre a API da DATAPREV.",
        # Mais frases podem ser adicionadas conforme necessário
    ]

def gerar_frases_desempenho_web():
    return [
        "Como está o desempenho da aplicação web da DATAPREV atualmente?",
        "Você precisa de ajuda para otimizar a performance da aplicação web da DATAPREV?",
        "Estamos analisando os tempos de resposta da aplicação web da DATAPREV.",
        "A aplicação web da DATAPREV está enfrentando lentidão em algum cenário específico?",
        "Vamos identificar e resolver quaisquer gargalos na aplicação web da DATAPREV.",
        "Você já realizou um teste de estresse na aplicação web da DATAPREV?",
        "Estamos revisando a configuração do servidor da aplicação web da DATAPREV para melhorar o desempenho.",
        "Pode fornecer mais detalhes sobre o ambiente em que a aplicação web da DATAPREV está rodando?",
        "Estamos avaliando o impacto das alterações recentes no desempenho da aplicação web da DATAPREV.",
        "Você está monitorando o desempenho da aplicação web da DATAPREV em tempo real?",
        "Estamos ajustando a configuração do banco de dados para melhorar o desempenho da aplicação web da DATAPREV.",
        "Você já otimizou o código da aplicação web da DATAPREV para um melhor desempenho?",
        "Vamos realizar uma análise comparativa de desempenho para a aplicação web da DATAPREV.",
        "Você encontrou algum problema específico de desempenho na aplicação web da DATAPREV?",
        "Estamos preparando um relatório detalhado sobre o desempenho da aplicação web da DATAPREV.",
        "Podemos ajudar a configurar ferramentas de monitoramento para a aplicação web da DATAPREV.",
        "Você já considerou ajustar a arquitetura da aplicação web da DATAPREV para melhorar o desempenho?",
        "Estamos analisando os logs para entender a causa da lentidão na aplicação web da DATAPREV.",
        "Você precisa de ajuda para identificar problemas de escalabilidade na aplicação web da DATAPREV?",
        "Estamos disponíveis para discutir estratégias para otimizar o desempenho da aplicação web da DATAPREV.",
        # Mais frases podem ser adicionadas conforme necessário
    ]

def gerar_frases_desempenho_mobile():
    return [
        "Como está o desempenho do aplicativo mobile da DATAPREV?",
        "Você está enfrentando problemas de lentidão no aplicativo mobile da DATAPREV?",
        "Estamos analisando a performance do aplicativo mobile da DATAPREV.",
        "Você já realizou um teste de estresse no aplicativo mobile da DATAPREV?",
        "Podemos revisar a configuração do servidor para melhorar o desempenho do aplicativo mobile da DATAPREV.",
        "Estamos avaliando o impacto das recentes atualizações no desempenho do aplicativo mobile da DATAPREV.",
        "Você já monitorou o desempenho do aplicativo mobile da DATAPREV em diferentes dispositivos?",
        "Estamos ajustando a configuração do banco de dados para otimizar o desempenho do aplicativo mobile da DATAPREV.",
        "Pode nos fornecer mais detalhes sobre os problemas de desempenho que você encontrou no aplicativo mobile da DATAPREV?",
        "Vamos realizar uma análise de desempenho do aplicativo mobile da DATAPREV e preparar um relatório.",
        "Você já otimizou o código do aplicativo mobile da DATAPREV para melhorar a performance?",
        "Estamos disponíveis para discutir estratégias para melhorar o desempenho do aplicativo mobile da DATAPREV.",
        "Você está utilizando ferramentas de monitoramento para avaliar o desempenho do aplicativo mobile da DATAPREV?",
        "Estamos aqui para ajudar a resolver qualquer problema de desempenho no aplicativo mobile da DATAPREV.",
        "Vamos analisar os logs do aplicativo mobile da DATAPREV para identificar possíveis gargalos.",
        "Você encontrou alguma instabilidade no aplicativo mobile da DATAPREV?",
        "Estamos realizando um teste de carga para avaliar a capacidade do aplicativo mobile da DATAPREV.",
        "Você já tentou otimizar o backend para melhorar o desempenho do aplicativo mobile da DATAPREV?",
        "Estamos revisando as práticas de desenvolvimento para garantir o melhor desempenho para o aplicativo mobile da DATAPREV.",
        "Podemos ajudar a ajustar as configurações do aplicativo mobile da DATAPREV para melhorar o desempenho.",
        # Mais frases podem ser adicionadas conforme necessário
    ]

def gerar_frases_aleatorias():
    frases_api = gerar_frases_api()
    frases_web = gerar_frases_desempenho_web()
    frases_mobile = gerar_frases_desempenho_mobile()
    
    todas_as_frases = frases_api + frases_web + frases_mobile
    
    # Garantir que a lista tenha pelo menos 1000 frases
    while len(todas_as_frases) < 1000:
        todas_as_frases.extend(todas_as_frases)
        todas_as_frases = todas_as_frases[:1000]  # Limitar a 1000 frases
    
    frases_aleatorias = [random.choice(todas_as_frases) for _ in range(1000)]
    
    return frases_aleatorias

def salvar_em_arquivo(frases, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        for frase in frases:
            file.write(frase + '\n')

def main():
    nome_arquivo = 'frases_treinamento_dataprev.txt'
    frases = gerar_frases_aleatorias()
    salvar_em_arquivo(frases, nome_arquivo)
    print(f"Arquivo '{nome_arquivo}' gerado com 1000 frases de treinamento.")

if __name__ == "__main__":
    main()
