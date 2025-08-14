# Instruções:
# Fiz as duas atividade a aula em um só documento, então eu comentei um exemplo. Para verificar, basta comentar o código que não gostaria de visualizar e descomentar o outro.

#--------------

#Exercício de If | Else

# nota = int(input('Digite sua nota: '))

# if nota >= 7:
    # print('Parabéns, você está aprovado!')

# elif nota < 5:
    # print('Que triste, você está reprovado!')

# else :
    # print('Você está de recuperação')

# print('Acabou o programa!')

#--------------

#Exercício de Match | Case

print('Olá, eu sou a sua assistente, Natalie. O que você quer fazer hoje?')

comando = input('Digite um comando: ')

match comando:
    case 'oi' | 'olá':
        print('Oi, como vai você?')
    case 'tchau' | 'sair' | 'fim' | 'exit':
        print('Tchau, foi bom conversar com você!')
    case 'piada':
        print('Sabe qual o padroeiro das pessoas que trabalham com TI? O São Login')
    case 'clima' | 'previsão do tempo':
        print('Tá muuuuuuuuito quente!! Deve ter passado de 40°C! 🥵')
    case _:
        print('Desculpe, não entendi o comando.')