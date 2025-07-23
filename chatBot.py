import os
import re
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    #if comando in ('olá', 'boa tarde', 'bom dia'):
    #    return 'Olá tudo bem!'
    #if comando == 'como estás':
    #    return 'Estou bem, obrigado!'
    #if comando == 'como te chamas?':
    #    return 'O meu nome é: Bot :)'
    #if comando == 'tempo':
    #    return 'Está um dia de sol!'
    #if comando in ('bye', 'adeus', 'tchau'):
    #    return 'Gostei de falar contigo! Até breve...'
    #if 'horas' in comando:
    #    return f'São: {datetime.now():%H:%M} horas'
    #if 'data' in comando:
    #    return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    #return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
         ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
         'como estás': 'Estou bem, obrigado!', 'como te chamas?': 'O meu nome é Joaquim',
         ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...', 'obrigado': 'De nada! Estou aqui para ajudar. '
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta
        
    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'
    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'
    
    if 'soma' in comando or '+' in comando:
    
        encontra = re.search(r'(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)', comando)

        if encontra:
            
            num1 = float(encontra.group(1))
            num2 = float(encontra.group(2))
            resultado = num1 + num2
            return f'O resultado de {num1} + {num2} é: {resultado}'
        else:
            
            return 'Claro! Diz-me os números que queres somar (exemplo: 9 + 4)'

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta = obter_resposta(user_input)
        print(f'Bot: {resposta}')
        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')

def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()