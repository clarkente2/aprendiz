
nome= input('qual seu nome? ')
hora= input ('qual horas sao agora? ')
hora_f = float(hora)
try:
  
  if hora_f >= 5.0 and hora_f < 12:
    print(f"bom dia {nome}")
  elif hora_f >= 12 and hora_f < 18:
    print (f'boa tarde {nome}')
  else:
    print (f' boa noite {nome}') 
except:
  print("numero invalido digite apenas numeros no modelo '00.00'")