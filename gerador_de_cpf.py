import random
while True:
    nove= ''
    for i in range(9):
        nove += str(random.randint(0, 9))
    contador= 10
    resultado = 0
    for digit in nove:
        resultado += (int(digit) * contador )
        contador -= 1
    digit1= ((resultado * 10) % 11)
    digit1 = digit1 if digit1 <= 9 else 0

    dez = nove + str(digit1)
    contador1= 11
    resultado2 = 0
    for digit2 in dez:
        resultado2 += (int(digit2) * contador1 )
        contador1 -= 1
    digit02= ((resultado2 * 10) % 11)
    digit02 = digit02 if digit02 <= 9 else 0

    cpf_valido= (f'{nove}{digit1}{digit02}')
    print(f'CPF GERADO: [{cpf_valido}]')
    break
    