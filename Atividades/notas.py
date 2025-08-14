notas = [10, 5 , 6 , 8]

media = 0
for nota in notas:
    media += nota
media /=4

if media >= 6:
    print(f'Sua média é {media} e você está: Aprovado!')

else :
    print(f'Sua média é {media} e você está de : Sub!')

