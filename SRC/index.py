# Desafio do Herói
nome_do_heroi = 'André Moura'
rank = ''
soul_stone = True

def subtracao(wins=0, loss=0):
    return wins - loss

resultado = subtracao(1250, 1050)

#  if-elif-else
if resultado <= 10:
    rank = 'Ferro'
elif resultado >= 11 and resultado <= 20:
    rank = 'Bronze'
elif resultado >= 21 and resultado <= 50:
    rank = 'Prata'
elif resultado >= 51 and resultado <= 80:
    rank = 'Ouro'
elif resultado >= 81 and resultado <= 90:
    rank = 'Diamante'
elif resultado >= 91 and resultado <= 100:
    rank = 'Lendário'
elif resultado >= 101:
    rank = 'Imortal'

print(f"Olá {nome_do_heroi}, seu saldo de vitórias é {resultado} e seu nível é {rank}")

if rank == 'Ferro':
    print('Consiga mais vitórias para liberar novos modos.')
elif rank == 'Prata':
    print('Você liberou o modo PvP em grupo')
elif rank == 'Diamante':
    print('O modo masmorra está liberado!')
elif rank == 'Imortal':
    print('Parabéns por estar entre os melhores!')
    print('A partir deste nível, em posse da SoulStone 💎 você pode viajar entre os mundos')
    print('')
    
    if soul_stone:
        print('Pedra localizada?: 👍')
        print('')
        print('Você tem uma SoulStone 💎, vá desbravar os mundos e espalhe seu legado!')
    else:
        print('Pedra localizada?: 👎')
        print('')
        print('Você ainda não tem uma SoulStone, vá ao vale perdido em busca da sua e cuidado com os perigos!')
