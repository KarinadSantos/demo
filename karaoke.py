import time
import turtle

turtle.addshape('Moana.gif')


titulo = 'Saber quem sou'
autor = 'Moana'
letra = '''\
Aqui sempre, sempre à beira da água
Desde quando eu me lembro
Não consigo explicar
Tento não causar nenhuma mágoa
Mas sempre volto pra água
Mas não posso evitar

Tento obedecer, não olhar pra trás
Sigo meu dever, não questiono mais
Mas pra onde vou, quando vejo, estou onde eu sempre quis

O horizonte me pede pra ir tão longe
Será que eu vou?
Ninguém tentou
Se as ondas se abrirem pra mim de verdade
Com o vento eu vou
Se eu for, não sei ao certo quão longe eu vou

Eu sou moradora dessa ilha
Todos vivem bem na ilha
Tudo tem o seu lugar
Sei que cada cidadão da ilha
Tem função nessa ilha
Talvez seja melhor tentar

Posso liderar o meu povo então
E desempenhar essa tal missão
Mas não sei calar o meu coração
Por que sou assim?

Essa luz que do mar bate em mim me invade
Será que eu vou?
Ninguém tentou
E parece que a luz chama por mim e já sabe
Que um dia eu vou
Vou atravessar para além do mar

O horizonte me pede pra ir tão longe
Será que eu vou?
Ninguém tentou
Se as ondas abrirem pra mim de verdade
Um dia eu vou
Saber quem sou '''

texto = letra.split("\n")

Moana = turtle.Pen()
Moana.shape('Moana.gif')

pincel = turtle.Pen()
pincel.goto(300,300)
pincel.hideturtle()

for linha in texto:
    pincel.write(linha, align='center')
    time.sleep(1.0)
    pincel.undo()

turtle.done()    