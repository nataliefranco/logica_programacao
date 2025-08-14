print('Sistema de notas')

opcao = ''
media = 0
notas = []


while opcao.lower() != 'sair':
    opcao = input('Digite uma nota ou sair para calcular a media: ')
    if opcao.lower() != 'sair':
        notas.append(int(opcao))

for notaDaVez in notas:
    media += notaDaVez

media /= len(notas)

if media >= 6:
    print(f'Sua média é {media} e você está: Aprovado!')

else :
    print(f'Sua média é {media} e você está de : Sub!')

