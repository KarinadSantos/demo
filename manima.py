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

    gato = Pen('gato_.gif')
    gato.up()

    turtle.done()

# Chama a funÃ§Ã£o principal
principal()
