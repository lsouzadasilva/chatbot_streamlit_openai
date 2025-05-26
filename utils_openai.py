import openai


# API OPENAI ================================================
def retorna_resposta_modelo(mensagens,
                            openai_key,
                            modelo='gpt-4-turbo',
                            temperatura=0,
                            stream=False):

    # Definindo a chave da API diretamente
    openai.api_key = openai_key

    response = openai.ChatCompletion.create(
        model=modelo,
        messages=mensagens,
        temperature=temperatura,
        stream=stream
    )

    return response
