import tkinter as tk
import random

# Criar a janela principal
janela = tk.Tk()
janela.title("Botão Fujão")
janela.geometry("1000x700")  # Tamanho da janela

# Adicionar a frase no fundo
frase = tk.Label(janela, text="Duvido conseguir clicar", font=("Arial", 20), fg="gray")
frase.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza a frase

# Função para mover o botão para uma posição aleatória
def mover_botao(event):
    # Gerar novas coordenadas aleatórias dentro da janela
    novo_x = random.randint(0, 800)  # Limite para não sair da janela
    novo_y = random.randint(0, 600)
    botao.place(x=novo_x, y=novo_y)

# Função para quando o botão for clicado (só por diversão)
def clicou():
    botao.config(text="Você é rápido!")  # Mensagem caso consiga clicar

# Criar o botão
botao = tk.Button(janela, text="Clique em mim", command=clicou)
botao.place(x=800, y=500)  # Posição inicial

# Vincular o movimento do mouse ao evento de aproximação
janela.bind("<Motion>", mover_botao)  # O botão foge quando o mouse se move

# Iniciar o loop da janela
janela.mainloop()