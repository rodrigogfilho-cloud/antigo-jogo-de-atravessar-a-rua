import pygame
from classe_viloes_hahaha import Viloes
from classse_jogador import Jogador
pygame.init()

cores = {
    "VERMELHO" : (255,0,0),
    "VERDE DE PASTO" : (70,255,70),
    "PRETO"  : (0,0,0)
}

clock = pygame.time.Clock()
#cria a janela do jogo
tela = pygame.display.set_mode((1700,900))
fundo = pygame.image.load("src/img/rua.png")
fundo = pygame.transform.scale(fundo,(1700,900))

#alterar o nome do jogo
pygame.display.set_caption("Joguinho do Mr. Godoy Master Aurudo 6️⃣7️⃣")

####################################################################
#criando inimigo
lista_inimigos = [Viloes("src/img/bin.png"),
                  Viloes("src/img/vilao.png"),
                  Viloes("src/img/vilao2.png"),
                  Viloes("src/img/vilao3.png")]
player = ("src/img/DAVI-BRITO.png")

while True:
    #Pego todos os eventos que aconteceram na janela
    lista_de_eventos = pygame.event.get()
    #Percorro os eventos para encontrar aquele que eu quiser
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT: #Se um dos eventos for ter clicado no X eu encerro o programa
            pygame.quit()
            exit()

        
    #PINTANDO A TELA NOVAMENTE
    
    tela.blit(fundo,(0,0))
    #INSERINDO IMAGENS DOS INDIVIDUOS
    


    for  inimigo in lista_inimigos:
        inimigo.andar()
        inimigo.exibir(tela)
    
        ###MOVIMENTAÇÃO DO DAVIZINHO CALABRESO###
        
    for jogador in player:
        jogador.andar_player()
        jogador.exibir_player(tela)
    

    #ATUALIZA A TELA
    pygame.display.update()

    clock.tick(80)
