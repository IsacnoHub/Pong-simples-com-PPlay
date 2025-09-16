from PPlay.window import*
from PPlay.gameimage import*
from PPlay.sprite import*
from random import randint

'''
Sempre que delta_time é usado isso tira a necessidade de setar fps
Random dá ao jogo mais possibilidades, mesmo um pouco mais fácil ou mais difícil

'''

Dist_da_parede = 50 #Distancia entre os pads e a parede

Ponto_player = 0
Ponto_maquina = 0

janela= Window(1600,1000) #define o tamanho da janela
janela.set_title("Pong") #coloca nome na janela

bola= Sprite("Bola.png") 
bola.set_position((janela.width/2)-(bola.width/2),(janela.height/2)-(bola.height/2))    #nome e posição
                                                                                            #dessa galera aí
barra_e= Sprite("Pad.png")                                                                      #tão definidos
barra_e.set_position(0 + Dist_da_parede, janela.height/2 - barra_e.height/2)                        #aqui <---
                                                                                                        #   <---
barra_d= Sprite("Pad.png")                                                                                  #   <---
barra_d.set_position(janela.width - barra_d.width - Dist_da_parede, janela.height/2 - barra_d.height/2)         #   <---

P_jogador = Sprite("Z.png") #Pontos começam com zero
P_maquina = Sprite("Z.png")
win = Sprite("Win.png")
lose = Sprite("Lose.png")

lista_de_pontos = ["Z.png", "U.png", "D.png", "T.png"]

P_jogador.set_position((janela.width/2)-(P_jogador.width/2)-(150),(janela.height/2)-(P_jogador.height/2)-(200)) #Posições do placar
P_maquina.set_position((janela.width/2)-(P_maquina.width/2)+(150),(janela.height/2)-(P_maquina.height/2)-(200))
win.set_position((janela.width/2)-(win.width/2),(janela.height/2)-(win.height/2)-350) #Posição de vitória
lose.set_position((janela.width/2)-(win.width/2),(janela.height/2)-(win.height/2)-350) #Posição de derrota

vel_ale_1 = 268
vel_ale_2 = 273
vel_x = 300                                 # VEL
vel_y = 300                                 # OCI
vel_barra_e = 500                           # DA
vel_barra_d = randint(vel_ale_1, vel_ale_2) # DES


encremento_vel = 23 #toda vez que toca um pad
vel_inicio = vel_x #serve pra voltar a velocidade ao normal dps de ponto

teclado = janela.get_keyboard()

estado = 0 #é pra ser o espaço para começar
vitoria_ativa = False  # NOVA VARIÁVEL PARA CONTROLAR VITÓRIA
derrota_ativa = False

while True:
    janela.set_background_color((0,0,0))

#mensagem de vitória
    if Ponto_player == 3:
        vitoria_ativa = True
        Ponto_player = 0
        Ponto_maquina = 0
        P_jogador = Sprite("Z.png") #Pontos começam com zero
        P_maquina = Sprite("Z.png")
        P_jogador.set_position((janela.width/2)-(P_jogador.width/2)-(150),(janela.height/2)-(P_jogador.height/2)-(200)) #Posições do placar
        P_maquina.set_position((janela.width/2)-(P_maquina.width/2)+(150),(janela.height/2)-(P_maquina.height/2)-(200))
        estado = 0
        vel_barra_d = randint(vel_ale_1, vel_ale_2)

#mensagem de derrota
    if Ponto_maquina == 3:
        derrota_ativa = True
        Ponto_maquina = 0
        Ponto_player = 0
        P_jogador = Sprite("Z.png") #Pontos começam com zero
        P_maquina = Sprite("Z.png")
        P_jogador.set_position((janela.width/2)-(P_jogador.width/2)-(150),(janela.height/2)-(P_jogador.height/2)-(200)) #Posições do placar
        P_maquina.set_position((janela.width/2)-(P_maquina.width/2)+(150),(janela.height/2)-(P_maquina.height/2)-(200))
        estado = 0
        vel_barra_d = randint(vel_ale_1, vel_ale_2)

#start com espaço
    if teclado.key_pressed("space"):
        vitoria_ativa = False
        derrota_ativa = False
        estado = 1
    if estado == 1:
        bola.x += vel_x * janela.delta_time()    
        bola.y += vel_y * janela.delta_time()

#colisão bola paredes laterais:
    if bola.x <=0 or bola.x + bola.width >= janela.width:
        estado = 0
        #placar
        if bola.x <= 0:
            Ponto_maquina += 1
            P_maquina = Sprite(lista_de_pontos[Ponto_maquina])
            P_maquina.set_position((janela.width/2)-(P_maquina.width/2)+(150),(janela.height/2)-(P_maquina.height/2)-(200))
        else:
            Ponto_player += 1
            P_jogador = Sprite(lista_de_pontos[Ponto_player])
            P_jogador.set_position((janela.width/2)-(P_jogador.width/2)-(150),(janela.height/2)-(P_jogador.height/2)-(200))

        if teclado.key_pressed("space"):
            vitoria_ativa = False
            derrota_ativa = False
            estado = 1
        if estado == 1:
            bola.x += vel_x * janela.delta_time()    
            bola.y += vel_y * janela.delta_time()
            
        bola.set_position((janela.width/2)-(bola.width/2),(janela.height/2)-(bola.height/2))
        barra_e.set_position(0 + Dist_da_parede, janela.height/2 - barra_e.height/2)
        barra_d.set_position(janela.width - barra_d.width - Dist_da_parede, janela.height/2 - barra_d.height/2)
        P_jogador.set_position((janela.width/2)-(P_jogador.width/2)-(150),(janela.height/2)-(P_jogador.height/2)-(200))
        P_maquina.set_position((janela.width/2)-(P_maquina.width/2)+(150),(janela.height/2)-(P_maquina.height/2)-(200))
        vel_x = vel_inicio

#colisão bola paredes base-teto:
    if bola.y <=0:
        vel_y *=-1
        bola.y += 1 #evita que fique presa no teto
    if bola.y + bola.height>= janela.height:
        vel_y *=-1
        bola.y -= 1 #evita que fique presa na base

#colisão bola x barra:
    if bola.collided(barra_e):
        vel_x*= -1
        bola.x= barra_e.x + barra_e.width

        #encrementa a velocidade
        if vel_x < 0:
            vel_x -= encremento_vel * janela.delta_time()
        else:
            vel_x += encremento_vel * janela.delta_time()

    if bola.collided(barra_d):
        vel_x*=-1
        bola.x= barra_d.x - bola.width 

        #encrementa a velocidade
        if vel_x < 0:
            vel_x -= encremento_vel * janela.delta_time()
        else:
            vel_x += encremento_vel * janela.delta_time()

#barra direita controlado por ia:
    if barra_d.y + barra_d.height/2 < bola.y + bola.height/2:
        barra_d.y += vel_barra_d * janela.delta_time()
    if barra_d.y + barra_d.height/2 > bola.y + bola.height/2:
        barra_d.y -= vel_barra_d * janela.delta_time()

#barra esquerda controlado por W, S:
    if estado == 1:  #só pra não dar pra controlar antes de começar o jogo antes de apertar espaço
        if teclado.key_pressed("UP"):
            barra_e.y -= vel_barra_e * janela.delta_time()
        if teclado.key_pressed("DOWN"):
            barra_e.y += vel_barra_e * janela.delta_time()

        if teclado.key_pressed("W"):
            barra_e.y -= vel_barra_e * janela.delta_time()
        if teclado.key_pressed("S"):
            barra_e.y += vel_barra_e * janela.delta_time()

#colisão barras:
    if barra_e.y < 0:
        barra_e.y = 0
    if barra_e.y + barra_e.height > janela.height:
        barra_e.y = janela.height - barra_e.height

    if barra_d.y < 0:
        barra_d.y = 0
    if barra_d.y + barra_d.height > janela.height:
        barra_d.y = janela.height - barra_d.height

#sair com ESC:
    if teclado.key_pressed("esc"):
        break

#desenha tudo
    bola.draw()
    barra_e.draw()
    barra_d.draw()
    P_jogador.draw()
    P_maquina.draw()
    if vitoria_ativa:
        win.draw()
    if derrota_ativa:
        lose.draw()
    janela.update()