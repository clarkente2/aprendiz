
# Calculadora simples

while True:
    sair= input('deseja prosseguir "s" ou "n": ').lower()
    if sair == 'n':
        print ('saindo...')
        break
    if sair not in ['s', 'n']:
        print('responda apenas com "s" ou "n"')
        continue

    valor1= input('digite o primeiro valor: ')
    valor2= input('digite o segundo valor: ')
    operador= input('digite um operador (+-/*): ')
    operador_permitido = '+-/*'
    if operador not in operador_permitido:
        print('digite apenas um dos operadores selecionados: +-/*')
        continue
    try:
        n1= float(valor1)
        n2= float(valor2)

    except ValueError:
        print('digite apenas numeros')
        continue

    if operador == '+':
        print(f'Resultado: {n1 + n2}')
    elif operador == '-':
        print(f'Resultado: {n1 - n2}')
    elif operador == '*':
        print(f'Resultado: {n1 * n2}')
    elif operador == '/':
        if n2 == 0:
            print(" Erro: Não é possível dividir por zero!")
        else:
            print(f'Resultado: {n1 / n2}')
    