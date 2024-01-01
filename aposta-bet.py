import os
import random

nomes = []
palpiteGremio = []
palpiteSeuTime = []
valores = []

def ler_arquivo():
    if not os.path.isfile("apostas.txt"):
        return

    with open("apostas.txt", "r") as arq:
        linhas = arq.readlines()

        for linha in linhas:
            partes = linha.split(";")
            nomes.append(partes[0])
            palpiteGremio.append(int(partes[1]))
            palpiteSeuTime.append(int(partes[2]))
            valores.append(float(partes[3][0:-1]))


def salva_arquivo():
    with open("apostas.txt", "w") as arq:
        for nome, palpite1, palpite2, valor in zip(nomes, palpiteGremio, palpiteSeuTime, valores):
            arq.write(f"{nome};{palpite1};{palpite2};{valor:.2f}\n")


def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado * 30)


def cadastrar_aposta():
    titulo('Cadastre sua aposta:')
    nome = input('Nome do apostador: ')
    palpite1 = input('Quantos gols do Grêmio: ')
    palpite2 = input('Quantos gols do seu time: ')
    valor = float(input('Valor da Aposta: '))
    nomes.append(nome)
    palpiteGremio.append(palpite1)
    palpiteSeuTime.append(palpite2)
    valores.append(valor)
    print('Cadastro realizado com sucesso!!')


def listar_apostas():
    titulo('Lista de Apostas:')


    for i, (nome, palpite1, palpite2, valor) in enumerate(zip(nomes, palpiteGremio, palpiteSeuTime, valores), start=1):
        print(f"{i:2}. {nome} - Palpite: {palpite1}x{palpite2} - Aposta: R${valor:.2f}")

        if palpite1 > palpite2:
            print("Apostou que o Grêmio vence!")
        elif palpite1 < palpite2:
            print("Apostou que o seu time vence!")
        else:
            print("Apostou em um empate!")

def total_apostas():
    titulo('Total de Apostas:')
    total_apostas = len(nomes)
    valor_total = sum(valores)
    print(f"Total de apostas: {total_apostas}")
    print(f"Valor total das apostas: R${valor_total:.2f}")

def total_apostado_nos_resultado():
    total_gremio = 0
    total_caxias = 0
    total_empate = 0

    for palpite_gremio, palpite_caxias, valor in zip(palpiteGremio, palpiteSeuTime, valores):
        if palpite_gremio > palpite_caxias:
            total_gremio += valor
        elif palpite_gremio < palpite_caxias:
            total_caxias += valor
        else:
            total_empate += valor
    
    print(f"Total apostado no Grêmio: R${total_gremio:.2f}")
    print(f"Total apostado no seu Time: R${total_caxias:.2f}")
    print(f"Total apostado no empate: R${total_empate:.2f}")

def resultado_partida():
    titulo('Resultado da Partida')
    opcao1 = "Grêmio"
    opcao2 = "Seu Time"
    valor_total = sum(valores)
 

    vencedores = []

    if random.randint(0, 1) == 0:
        print(f'Vencedor é o {opcao1} com a premiação de {valor_total:.2f}')

        for i, (nome, palpite1, palpite2) in enumerate(zip(nomes, palpiteGremio, palpiteSeuTime)):
            if palpite1 > palpite2:
                vencedores.append(nome)

        print(f"Nomes dos vencedores: {vencedores}")

    else:
        print(f'Vencedor é o {opcao2} com a premiação de {valor_total:.2f}')

        for i, (nome, palpite1, palpite2) in enumerate(zip(nomes, palpiteGremio, palpiteSeuTime)):
            if palpite1 < palpite2:
                vencedores.append(nome)

        print(f"Nomes dos vencedores: {vencedores}")

ler_arquivo()

while True:
    titulo('ESCOLHA UMA DAS OPÇÕES')
    print('1. -> Faça sua Aposta')
    print('2. -> Listas das Apostas')
    print('3. -> Total de apostas acumulado')
    print('4. -> Mostrar as apostas de cada time')
    print('5. -> Veja o resultado do jogo')
    print('6. -> Finalizar')
    print('-' * 20)
    selecione = int(input('Selecione a opção: '))
    if selecione == 1:
        cadastrar_aposta()
    elif selecione == 2:
        listar_apostas()
    elif selecione == 3:
        total_apostas()
    elif selecione == 4:
        total_apostado_nos_resultado()
    elif selecione == 5:
        resultado_partida()
    else:
        salva_arquivo()
        break
