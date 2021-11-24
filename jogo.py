from graphics import *
import random

#Janela Inicial
win = GraphWin("Tela Inicial", 800, 600)
win.setBackground(color_rgb(0, 200, 255))

#play
txt= Text(Point(400, 300), "PLAY")
txt.setTextColor(color_rgb(230, 240, 240))
txt.setSize(30)
txt.draw(win)

#pra salvar
txt1=Text(Point(400, 400), """Depois de colocar seu nome
Clique 2 vezes no PLAY para começar
""")
txt1.setTextColor("black")
txt1.setSize(10)
txt1.draw(win)

#nome do jogador
textEntry=Entry(Point(400, 350), 14)
textEntry.draw(win)
win.getMouse()
text= textEntry.getText()
top3=[]
top3.append(text)
win.getMouse()

txt.undraw()
txt1.undraw()
textEntry.undraw()

#parte do jogo

LinhaSuperior= Line(Point (0, 40),Point(800, 40))
LinhaSuperior.setWidth(10)
LinhaSuperior.setFill(color_rgb(230, 240, 240))
LinhaSuperior.draw(win)

linhaInferior = Line(Point(0, 550), Point(800, 550))
linhaInferior.setWidth(3)
linhaInferior.setFill(color_rgb(230, 240, 240))
linhaInferior.draw(win)

#Bola
col = 390
lin = 80
raio = 15
circulo=Circle(Point(col, lin), raio)
circulo.setFill(color_rgb(10, 10, 100))
circulo.draw(win)

#pontos
pts= 0
pontos=Text(Point(400,575), f"{text}:" + str(pts))
pontos.setSize(14)
pontos.draw(win)

#dificuldade
nivel=1
dificuldade=Text(Point(400, 20), "NÍVEL " + str(nivel))
dificuldade.setSize(14)
dificuldade.draw(win)

#corações
poly1= Polygon(Point(40,575), Point(81,575), Point(60,595))
poly1.setFill(color="red")
poly1.setOutline(color="red")
poly1.draw(win)

cor = Circle(Point(53, 570), 14)
cor.setFill(color="red")
cor.setOutline(color="red")
cor.draw(win)

cor1 = Circle(Point(68, 570), 14)
cor1.setFill(color="red")
cor1.setOutline(color="red")
cor1.draw(win)

poly2= Polygon(Point(98,578), Point(134,578), Point(115,595))
poly2.setFill(color="red")
poly2.setOutline(color="red")
poly2.draw(win)

cor2 = Circle(Point(108, 570), 14)
cor2.setFill(color="red")
cor2.setOutline(color="red")
cor2.draw(win)

cor3 = Circle(Point(123, 570), 14)
cor3.setFill(color="red")
cor3.setOutline(color="red")
cor3.draw(win)

poly3= Polygon(Point(150,575), Point(190,575), Point(170,595))
poly3.setFill(color="red")
poly3.setOutline(color="red")
poly3.draw(win)

cor4 = Circle(Point(163, 570), 14)
cor4.setFill(color="red")
cor4.setOutline(color="red")
cor4.draw(win)

cor5 = Circle(Point(178, 570), 14)
cor5.setFill(color="red")
cor5.setOutline(color="red")
cor5.draw(win)

#Nuvem
Raio=20
x, y = 350, 530
x1, y1 = 370,520
x2, y2 = 400, 520
x3, y3 = 430, 520
x4, y4 = 450, 530
x5, y5 = 370, 545
x6, y6 = 400, 545
x7, y7 = 430, 545

cir=Circle(Point(x,y), Raio)
cir.setFill(color='white')
cir.setOutline(color="white")
cir.draw(win)

cir1=Circle(Point(x1,y1), Raio)
cir1.setFill(color='white')
cir1.setOutline(color="white")
cir1.draw(win)

cir2=Circle(Point(x2,y2), Raio)
cir2.setFill(color='white')
cir2.setOutline(color="white")
cir2.draw(win)

cir3=Circle(Point(x3,y3),Raio)
cir3.setFill(color='white')
cir3.setOutline(color="white")
cir3.draw(win)

cir4=Circle(Point(x4,y4), Raio)
cir4.setOutline(color="white")
cir4.setFill(color='white')
cir4.draw(win)

cir5=Circle(Point(x5,y5), Raio)
cir5.setFill(color='white')
cir5.setOutline(color="white")
cir5.draw(win)

cir6=Circle(Point(x6,y6), Raio)
cir6.setFill(color='white')
cir6.setOutline(color="white")
cir6.draw(win)

cir7=Circle(Point(x7,y7), Raio)
cir7.setFill(color='white')
cir7.setOutline(color="white")
cir7.draw(win)


velocidade=5
bateu = True
continuar = True
vida=0

while continuar:

  if bateu:
      passo = random.randrange(1, 10)
      if random.random() < 0.5:
          passo = -passo
      bateu = False

  if (col + raio + passo) > 800:
      passo = -passo

  if (col - raio + passo) < 0:
      passo = -passo

  if lin < 65:
      velocidade = -velocidade

  if lin == 520 and col > x and col < x4:
      velocidade = -velocidade
      pontos.undraw()
      pts += 1
      pontos = Text(Point(400, 575), f"{text}:" + str(pts))
      pontos.setSize(14)
      pontos.draw(win)
      if pts==5:
        velocidade-= 5
        dificuldade.undraw()
        nivel+=1
        dificuldade = Text(Point(400, 20), "NÍVEL " + str(nivel) )
        dificuldade.setSize(14)
        dificuldade.draw(win)
      if pts==10:
          velocidade -= 10
          dificuldade.undraw()
          nivel += 1
          dificuldade = Text(Point(400, 20), "NÍVEL " + str(nivel) )
          dificuldade.setSize(14)
          dificuldade.draw(win)

  if lin>600:
      vida+=1
      if vida<3:
          circulo.undraw()
          col = 390
          lin = 80
          raio = 15
          circulo = Circle(Point(col, lin), raio)
          circulo.setFill(color_rgb(10, 10, 100))
          circulo.draw(win)
      if vida==1:
          poly3.undraw()
          cor5.undraw()
          cor4.undraw()
      if vida==2:
          poly2.undraw()
          cor3.undraw()
          cor2.undraw()
      if vida==3:
          poly1.undraw()
          cor1.undraw()
          cor.undraw()
          pontos.undraw()
          txt = Text(Point(400, 300), "VOCE PERDEU")
          txt.setTextColor(color="white")
          txt.setSize(30)
          txt.draw(win)
          pontos = Text(Point(400, 350), f"{text}:" + str(pts))
          pontos.setSize(14)
          pontos.draw(win)
          win.getMouse()
          break

  # Nova posição do círculo
  circulo.undraw()
  col += passo
  lin += velocidade
  circulo = Circle(Point(col, lin), 15)
  circulo.setFill(color_rgb(10, 10, 100))
  circulo.draw(win)

  #dificuldade



  # Movimento horizontal da barra pelas setas direita/esquerda
  tecla = win.checkKey()

  # Sair do joguinho
  if tecla == "Escape":
      continuar = False
      continue

  if tecla == "Right":
      if x < 680:
          x+=20
      cir.undraw()
      cir=Circle(Point(x,y), 20)
      cir.setFill(color='white')
      cir.setOutline(color="white")
      cir.draw(win)
      if x1 < 700:
          x1+=20
      cir1.undraw()
      cir1=Circle(Point(x1,y1), 20)
      cir1.setFill(color='white')
      cir1.setOutline(color="white")
      cir1.draw(win)
      if x2 < 740:
          x2+=20
      cir2.undraw()
      cir2=Circle(Point(x2,y2),20)
      cir2.setFill(color='white')
      cir2.setOutline(color="white")
      cir2.draw(win)
      if x3 < 760:
          x3+=20
      cir3.undraw()
      cir3=Circle(Point(x3,y3),20)
      cir3.setFill(color='white')
      cir3.setOutline(color="white")
      cir3.draw(win)
      if x4 < 780:
          x4+=20
      cir4.undraw()
      cir4=Circle(Point(x4,y4),20)
      cir4.setFill(color='white')
      cir4.setOutline(color="white")
      cir4.draw(win)
      if x5 < 700:
          x5+=20
      cir5.undraw()
      cir5=Circle(Point(x5,y5),20)
      cir5.setFill(color='white')
      cir5.setOutline(color="white")
      cir5.draw(win)
      if x6 < 740:
          x6+=20
      cir6.undraw()
      cir6=Circle(Point(x6,y6),20)
      cir6.setFill(color='white')
      cir6.setOutline(color="white")
      cir6.draw(win)
      if x7 < 760:
          x7+=20
      cir7.undraw()
      cir7=Circle(Point(x7,y7),20)
      cir7.setFill(color='white')
      cir7.setOutline(color="white")
      cir7.draw(win)


  if tecla == "Left":
      if x > 10:
          x+=-20
      cir.undraw()
      cir = Circle(Point(x, y), 20)
      cir.setFill(color='white')
      cir.setOutline(color="white")
      cir.draw(win)

      if x1 > 40:
          x1+=-20
      cir1.undraw()
      cir1 = Circle(Point(x1, y1), 20)
      cir1.setFill(color='white')
      cir1.setOutline(color="white")
      cir1.draw(win)

      if x2 > 60:
          x2+=-20
      cir2.undraw()
      cir2 = Circle(Point(x2, y2), 20)
      cir2.setFill(color='white')
      cir2.setOutline(color="white")
      cir2.draw(win)

      if x3 > 100:
          x3+=-20
      cir3.undraw()
      cir3 = Circle(Point(x3, y3), 20)
      cir3.setFill(color='white')
      cir3.setOutline(color="white")
      cir3.draw(win)

      if x4 > 120:
          x4+=-20
      cir4.undraw()
      cir4 = Circle(Point(x4, y4), 20)
      cir4.setFill(color='white')
      cir4.setOutline(color="white")
      cir4.draw(win)

      if x5 > 40:
          x5+=-20
      cir5.undraw()
      cir5 = Circle(Point(x5, y5), 20)
      cir5.setFill(color='white')
      cir5.setOutline(color="white")
      cir5.draw(win)

      if x6 > 60:
          x6+=-20
      cir6.undraw()
      cir6 = Circle(Point(x6, y6), 20)
      cir6.setFill(color='white')
      cir6.setOutline(color="white")
      cir6.draw(win)

      if x7 > 100:
          x7+=-20
      cir7.undraw()
      cir7 = Circle(Point(x7, y7), 20)
      cir7.setFill(color='white')
      cir7.setOutline(color="white")
      cir7.draw(win)
  # Esperar o ser humano reagir
  time.sleep(.07)


win.close()
