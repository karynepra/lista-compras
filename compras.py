import json
import os
import time

compras = {}

def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade

def remover_item(compras, item):
    if item in compras:
        del compras[item]

def visualizar_compras(compras):
    for item, quantidade in compras.items():
        print(f'{item}: {quantidade}')
    print()
    print('Pressione enter para continuar')
    input()

def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(compras, arquivo)

def carregar_compras(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)

def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1 Adicionar item')
        print('2 Remover item')
        print('3 Visualizar lista')
        print('4 Salvar e sair')
        print('5 Sair sem salvar')
        
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            item = input('Digite o nome do item: ')
            print('1 Quantidade de itens: ')
            print('2 Peso do item: ')
            escolha = input('Escolha opção de quantidade ou peso: ')

            if escolha == '1':
                quantidade = int(input('Digite a quantidade do item: '))
            elif escolha == '2':
                quantidade = float(input('Digite o peso desejado do item: '))
            adicionar_item(compras, item, quantidade)
        elif escolha == '2':
            item = input('Digite o nome do item: ')
            remover_item(compras, item)
        elif escolha == '3':
            visualizar_compras(compras)
        elif escolha == '4':
            if nome_arquivo is None:
                nome_arquivo = input('Digite o nome do arquivo para salvar: ')
            if not nome_arquivo.endswith('.json'):
                nome_arquivo += '.json'
            salvar_compras(compras, nome_arquivo)
            break
        elif escolha == '5':
            break
        else:
            print('Opção inválida!')
            time.sleep(1)

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1 Criar uma nova lista de compras')
        print('2 Carregar uma lista de existente')
        print('3 Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            compras = {}
            gerenciar_compras(compras)
        elif escolha == '2': 
            print('Listas disponíveis: ')
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith('.json')]
            if not arquivos:
                print('Nenhum arquivo encontrado')
                time.sleep(2)
                continue
            for i, arquivo in enumerate(arquivos, 1):
                print(f'{i} {arquivo}')
                
            escolha = int(input('Escolha uma lista para carregar (0 se nenhuma): '))

            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print('Opção inválida')
                time.sleep(1)
                continue
            compras = carregar_compras(arquivos[escolha - 1])
            gerenciar_compras(compras, arquivos[escolha - 1])

        elif escolha == '3':
            break
        else:
            print('Opção inválida!')
            time.sleep(1)

if __name__ == '__main__':
    main()