palavra_secreta= 'biscoito'
tentativa = 0
letra_correta = ''
import os
while True:
    
    digite_palavra= input('digite uma letra: ')
    tentativa += 1
    if len(digite_palavra) > 1:
        print('digite apenas uma letra')
        continue

    if digite_palavra in palavra_secreta:
      letra_correta += digite_palavra
      tentativa -= 1


    palavra_formada = ''
    for letra_secreta in palavra_secreta:
       if letra_secreta in letra_correta:
         palavra_formada += letra_secreta
       else:
        palavra_formada += '*'
    print('palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
       os.system('cls')
       print('PARABENS!!!! VOCE GANHOU!!!')
       print('a palavra era:', palavra_secreta)
       print(f'total de erros:{tentativa}x')
       tentativa = 0
       letra_correta = ''
       break
