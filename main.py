import pygame
from classe_viloes_hahaha import Viloes
from classse_jogador import Jogador

pygame.init()

cores = {
    "VERMELHO" : (255,0,0),
    "VERDE DE PASTO" : (70,255,70),
    "PRETO"  : (0,0,0),
    "BRANCO" : (255,255,255)
}

clock = pygame.time.Clock()
#cria a janela do jogo
tela = pygame.display.set_mode((1700,900))
fundo = pygame.image.load("src/img/rua2.png")
fundo = pygame.transform.scale(fundo,(1700,900))
inicial = pygame.image.load("src/img/tela_inicial.png")
inicial = pygame.transform.scale(inicial,(1700,900))
perdeu = pygame.image.load("src/img/tela_game_over.png")
perdeu = pygame.transform.scale(perdeu,(1700,900))
#alterar o nome do jogo

pygame.display.set_caption("Joguinho do Mr. Godoy Master Aurudo 6️⃣7️⃣")
morte = 0

#criando inimigos
lista_inimigos = [Viloes("src/img/bin.png"),
                  Viloes("src/img/vilao.png"),
                  Viloes("src/img/vilao2.png"),
                  Viloes("src/img/vilao3.png")]

#criando davizinho

davizinho = Jogador()
fonte_texto = pygame.font.SysFont("Arial",28,True)
status_jogo = "INICIO"
while True:
    #Pego todos os eventos que aconteceram na janela
    lista_de_eventos = pygame.event.get()
    #Percorro os eventos para encontrar aquele que eu quiser
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT: #Se um dos eventos for ter clicado no X eu encerro o programa
            pygame.quit()
            exit()

    

    tecla_pressionada = pygame.key.get_pressed()   
    #PINTANDO A TELA NOVAMENTE

    if status_jogo == "INICIO":
        tela.blit(inicial,(0,0))
        if tecla_pressionada[pygame.K_RETURN] or tecla_pressionada[pygame.K_KP_ENTER]:
            status_jogo = "JOGANDO"

    if status_jogo =="JOGANDO":

        #exibindo tela da rua
        tela.blit(fundo,(0,0))

        textos_mortes = fonte_texto.render(f'Mortes: {morte}', False,(255,255,255))
        tela.blit(textos_mortes,(10, 5))
        #exibir davizinho
        davizinho.andar(tecla_pressionada)
        davizinho.exibir(tela)
        for  inimigo in lista_inimigos:
            inimigo.andar()
            inimigo.exibir(tela)
            #testando colisão  entre inimigos malvado e davi britozex
            if inimigo.mascara.overlap(davizinho.mascara,(davizinho.davi_x - inimigo.pos_x_inimigo , davizinho.davi_y - inimigo.pos_y_inimigo )):
                davizinho.voltar()
                morte += 1
                davizinho.gritar()
            if morte == 10 :
                status_jogo = "PERDEU"
    if status_jogo == "PERDEU":
        tela.blit(perdeu,(0,0))
    if tecla_pressionada[pygame.K_RETURN] or tecla_pressionada[pygame.K_KP_ENTER]:
            status_jogo = "JOGANDO"
        #INSERINDO IMAGENS DOS INIMIGOS

        
        

            
            
        #ATUALIZA A TELA
    pygame.display.update()

    clock.tick(80)
