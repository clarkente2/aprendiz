import os

lista = []

while True:
    print('\n ESCOLHA UMA DAS OPÇÕES ABAIXO')
    piloto = input('\n [l]istar [a]dicionar [r]etirar [s]air\n ').lower()

    if piloto == 's':
        break

    if piloto not in 'lar' or len(piloto) != 1:
        print('Opção inválida. Tente novamente!')
        continue

    if piloto == 'a':
        os.system('cls')
        while True:
            
            item = input('Digite o item (ou [v] para voltar): ')
        
            if item.lower() == 'v':
                break
            if item in lista:
                print('Esse item ja esta na lista')
                continue
            if not item.isalpha():
                print('Erro: Digite apenas palavras.')
                continue
            
            lista.append(item)
            print(f'{item} adicionado com sucesso!')

    elif piloto == 'l':
        os.system('cls')
        if not lista:
            print('\n Sua lista está vazia.')
            continue
        
        print('SUA LISTA:')
        for indice, nome in enumerate(lista):
            print(f'{indice} - {nome}')

    elif piloto == 'r':
        os.system('cls')
        if not lista:
            print('\n Nada para retirar.')
            continue
            
        while True:
            for i, n in enumerate(lista):
                print(f'{i}: {n}')
                
            indice_str = input('\n Digite o número do item a ser apagado (ou [v] para retornar): ')
            
            if indice_str.lower() == 'v':
                break
            
            try:
                indice = int(indice_str)
                removido = lista.pop(indice)
                print(f'Item "{removido}" removido com sucesso!')
                break 
            except (ValueError, IndexError):
                print('Erro: Digite um número válido da lista.')