import os
import turtle
from turtle import Pen , Screen
from pathlib import Path

LARG= 800
ALT= 600

def carrega_imagens(categoria: str):
    caminho = Path(__file__)
    caminho_imagens = caminho.parent / categoria
    img_animais = caminho_imagens.glob('*.gif')
    pwd = os.getcwd()
    os.chdir(caminho_imagens)

    for img in img_animais:
        turtle.addshape(img.name)

    os.chdir(pwd)

def principal():
    carrega_imagens('animais')

    tela = Screen()
    tela.setup(LARG,ALT)
    tela.title('Manima: Animações que me animam')

    gato = Pen('gato_.gif', False)
    gato.up()
    gato.goto(-LARG//2, -ALT//2)
    gato.showturtle()
    X_INI = -LARG//2
    X_FIM = LARG//2
    Y_FIXO = 10-ALT//2
    for x in range(X_INI, X_FIM, 5)
     gato.goto(x, Y_FIXO)


    turtle.done()

# Chama a funÃ§Ã£o principal
principal()
