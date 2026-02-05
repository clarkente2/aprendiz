 
while True:
    pega= input('qual cpf deseja validar: ') .replace('.', '').replace('-', '').replace(' ', '')
    if not pega.isdigit() or len(pega) !=11:
        print('DIGITE OS 11 NUMEROS DO CPF')
        continue
    if pega == pega[0] * 11:
        print('nao repita o mesmo numero diversas vezes')
        continue
    nove = pega[0:9]
    contador= 10
    resultado = 0
    for digit in nove:
        resultado += (int(digit) * contador )
        contador -= 1
    digit1= ((resultado * 10) % 11)
    digit1 = digit1 if digit1 <= 9 else 0

    dez = pega[0:10]
    contador1= 11
    resultado2 = 0
    for digit2 in dez:
        resultado2 += (int(digit2) * contador1 )
        contador1 -= 1
    digit02= ((resultado2 * 10) % 11)
    digit02 = digit02 if digit02 <= 9 else 0

    cpf_valido= (f'{nove}{digit1}{digit02}')
    
    if pega == cpf_valido:
        print(f'cpf [{pega}] e valido')
        break
    else:
        print(f'cpf [{pega}] e invalido')
        