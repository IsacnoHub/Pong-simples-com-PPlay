from PPlay.window import*
from PPlay.gameimage import*
from PPlay.sprite import*
from random import randint

'''
Sempre que delta_time é usado isso tira a necessidade de setar fps
Random dá ao jogo mais possibilidades, mesmo um pouco mais fácil ou mais difícil

'''

Dist_da_parede = 50 #Distancia entre os pads e a parede

janela= Window(2000,800) #define o tamanho da janela
janela.set_title("Pong") #coloca nome na janela

bola= Sprite("Bola.png") 
bola.set_position((janela.width/2)-(bola.width/2),(janela.height/2)-(bola.height/2))    #nome e posição
                                                                                            #dessa galera aí
barra_e= Sprite("Pad.png")                                                                      #tão definidos
barra_e.set_position(0 + Dist_da_parede, janela.height/2 - barra_e.height/2)                        #aqui <---
                                                                                                        #   <---
barra_d= Sprite("Pad.png")                                                                                  #   <---
barra_d.set_position(janela.width - barra_d.width - Dist_da_parede, janela.height/2 - barra_d.height/2)         #   <---

lista_de_pontos = ['0', '1', '2', '3']

Ponto_player = 0
Ponto_maquina = 0
pts = 0

#Variaveis do texto na tela
size = 20
size_event = 30
size_placar = 50
size_pts = 15
text = "Espaço para jogar | ESC para sair"  
text_win = "WINNER"   
text_lose = "GAME OVER"    
text_placar_widht = len('0') * size_placar
text_width = len(text) * (size // 2)
text_width_win = len(text_win) * (size_event / 2)
text_width_lose = len(text_lose) * (size_event / 2)
distan = janela.height*5/6
distan_placar = janela.height*1/4
distan_event = janela.height*1/8
dist_meio = 100
branco = (255, 255, 255)
vermelho = (255, 0, 0)

teclado = janela.get_keyboard()

vel_ale_1 = 265
vel_ale_2 = 272
vel_x = 300                                 # VEL
vel_y = 300                                 # OCI
vel_barra_e = 500                           # DA
vel_barra_d = randint(vel_ale_1, vel_ale_2) # DES

encremento_vel = 23 #toda vez que toca um pad
vel_inicio = vel_x #serve pra voltar a velocidade ao normal dps de ponto

estado = 0 #é pra ser o espaço para começar
vitoria_ativa = False  # NOVA VARIÁVEL PARA CONTROLAR VITÓRIA
derrota_ativa = False

while True: 
      
    janela.set_background_color((0,0,0))
    text_placar_d = lista_de_pontos[Ponto_maquina]
    text_placar_e = lista_de_pontos[Ponto_player]

#mensagem de vitória
    if Ponto_player == 3:
        vitoria_ativa = True
        Ponto_player = 0
        Ponto_maquina = 0
        P_maquina = janela.draw_text(text_placar_d, (janela.width/2 - text_placar_widht/2 + dist_meio), (distan_placar), size_placar, (branco), "Calibri")
        P_jogador = janela.draw_text(text_placar_e, (janela.width/2 - text_placar_widht/2 - dist_meio), (distan_placar), size_placar, (branco), "Calibri")
        janela.draw_text(text_win, (janela.width/2 - text_width_win/2), (distan_event), size_event, (branco), "Calibri")
        estado = 0
        vel_barra_d = randint(vel_ale_1, vel_ale_2)

#mensagem de derrota
    if Ponto_maquina == 3:
        derrota_ativa = True
        Ponto_maquina = 0
        Ponto_player = 0
        P_maquina = janela.draw_text(text_placar_d, (janela.width/2 - text_placar_widht/2 + dist_meio), (distan_placar), size_placar, (branco), "Calibri")
        P_jogador = janela.draw_text(text_placar_e, (janela.width/2 - text_placar_widht/2 - dist_meio), (distan_placar), size_placar, (branco), "Calibri")
        janela.draw_text(text_lose, (janela.width/2 - text_width_lose/2), (distan_event), size_event, (branco), "Calibri")
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

#texto na tela
    if estado == 0:
        janela.draw_text(text, (janela.width/2 - text_width/2), (distan), size, (255,255,255), "Calibri")
    


#colisão bola paredes laterais:
    if bola.x <=0 or bola.x + bola.width >= janela.width:
        estado = 0
        #placar
        if bola.x <= 0:
            Ponto_maquina += 1
            pts = 0
            P_maquina = janela.draw_text(text_placar_d, (janela.width/2 - text_placar_widht/2 + dist_meio), (distan_placar), size_placar, (branco), "Calibri")

        else:
            Ponto_player += 1
            pts = 0
            P_jogador = janela.draw_text(text_placar_e, (janela.width/2 - text_placar_widht/2 - dist_meio), (distan_placar), size_placar, (branco), "Calibri")

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
        pts += 1

        #encrementa a velocidade
        if vel_x < 0:
            vel_x -= encremento_vel
        else:
            vel_x += encremento_vel

    if bola.collided(barra_d):
        vel_x*=-1
        bola.x= barra_d.x - bola.width 

        #encrementa a velocidade
        if vel_x < 0:
            vel_x -= encremento_vel
        else:
            vel_x += encremento_vel 

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
    janela.draw_text(text_placar_d, (janela.width/2 - text_placar_widht/2 + dist_meio), (distan_placar), size_placar, (branco), "Calibri")
    janela.draw_text(text_placar_e, (janela.width/2 - text_placar_widht/2 - dist_meio), (distan_placar), size_placar, (branco), "Calibri")
    janela.draw_text(str(pts), 0, 0, size_pts, (branco), "Calibri")
    janela.draw_text(str(abs(vel_x)), 0, size_pts, size_pts, (branco), "Calibri")
    bola.draw()
    barra_e.draw()
    barra_d.draw()
    if vitoria_ativa:
        janela.draw_text(text_win, (janela.width/2 - text_width_win/2), (distan_event), size_event, (branco), "Calibri", True)#True é pra negrito
    if derrota_ativa:
        janela.draw_text(text_lose, (janela.width/2 - text_width_lose/2), (distan_event), size_event, (vermelho), "Calibri", True)
    janela.update()