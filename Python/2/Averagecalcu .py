cali1=int(input('calificacion1:'))
cali2=int(input('calificacion2:'))
cali3=int(input('calificacion3:'))

promedio=(cali1+cali2+cali3)/3
print("promedio",promedio)

if (promedio<6):
  print('reprobado')
  
if (promedio>=6):
  print('aprobado')

if ((promedio>=9)and (promedio<11)):
  print('ganaste un premio')
