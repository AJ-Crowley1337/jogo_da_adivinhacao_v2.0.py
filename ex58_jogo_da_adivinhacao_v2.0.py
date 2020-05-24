from random import randint
cores = {'lim':'\033[m', 'p':'\033[30;47m','vrl':'\033[1;31m', 'vrl2':'\033[1;31;47m', 'am':'\033[33m', 'am2':'\033[1;33m', 'az':'\033[1;34m', 'li':'\033[1;35m', 'li2':'\033[1;35m', 'azc':'\033[36m', 'b':'\033[4;37m', 'pb':'\033[7:37m'}
print(f'{cores["vrl2"]}=~{cores["lim"]}' * 21)
print(f'{cores["p"]}{"v2.0": <42}{cores["lim"]}')
print(f'{cores["vrl2"]}{"JOGO DA ADIVINHAÇÃO": ^42}{cores["lim"]}')
print(f'{cores["vrl2"]} {cores["lim"]}' * 42)
print(f'{cores["vrl2"]}=~{cores["lim"]}' * 21)
print(f'{"by: pequeno gafanhoto": >42}')
computador = randint(9, 10)
print(f'''{cores["am2"]}Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Sera que você consegue adivinhar qual foi?{cores["lim"]}
{cores["li"]}Digite -1 para desistir.{cores["lim"]}''')
acertou = False
palpites = 0
while not acertou:
    player = int(input(f'{cores["am2"]}Qual é seu palpite?{cores["lim"]} '))
    palpites += 1
    if player == computador:
        acertou = True
    elif player == -1:
        break
    else:
        if player < computador:
            print(f'{cores["li"]}Mais... Tente novamente.{cores["lim"]}')        
        elif player > computador:
            print(f'{cores["li"]}Menos... Tente novamente{cores["lim"]}')
print(f'{cores["vrl"]}=~{cores["lim"]}' * 21)
if player == -1:
    print(f'{cores["vrl"]}Você desistiu!{cores["lim"]}')
else:
    if palpites == 1:
        print(f'{cores["am2"]}Conseguiu acertar com {palpites} tentativa.Parabéns!\nVocê e muito bom nisso!{cores["am2"]}')
    elif palpites == 2:   
        print(f'{cores["am2"]}Acertou com {palpites} tentativas. Parabéns!{cores["am2"]}')
    else:
        print(f'{cores["am2"]}Você levou {palpites} tentativas mas acertou.{cores["lim"]}')
print(f'{cores["vrl"]}=~{cores["lim"]}' * 21)
