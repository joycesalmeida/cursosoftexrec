import enum

class Candidato(enum.Enum):
    Candidato_X = 889
    Candidato_Y = 847
    Candidato_Z = 515
    branco = 0

votar = True
votosX = 0
votosY = 0
votosZ = 0
votosBrancos = 0
votosNulo = 0

votar = True
while votar:

    #codigo para votar
    #pedir voto
    #verificar se o voto e valido
    #computar voto

    votoInvalido = True
    voto = -1
    while votoInvalido:
        try:
            voto_str = int(input("Informe seu voto: "))
            votoInvalido = False
        except:
            print("Informe um valor válido.")

    # aqui já temos um voto válido

    if Candidato.Candidato_X.value == voto:
        votosX =+ 1
    elif Candidato.Candidato_Y.value == voto:
        votosY += 1
    elif Candidato.Candidato_Z.value == voto:
        votosZ += 1
    elif Candidato.Branco.value == voto:
        votosBrancos += 1
    else:
        votosNulo += 1

    opcao = init(input("Deseja continuar votando? (1-SIM, 2-NÂO): "))
    if opcao == 1:
        votar = True
    if opcao == 2:
        votar = False

print("Votos para o(a) candidato(a) {}: {}".format(Candidato.Candidato_X.name, votosX))
print("Votos para o(a) candidato(a) {}: {}".format(Candidato.Candidato_Y.name, votosY))
print("Votos para o(a) candidato(a) {}: {}".format(Candidato.Candidato_Z.name, votosZ))
print("Votos nulos: {}".format(votosNulos))
print("Votos Brancos: {}".format(votosBrancos))
