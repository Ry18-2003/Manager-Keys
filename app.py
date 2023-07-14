# Janela do aplicativo

from customtkinter import * # Se der erro roda isso no cmd: pip install customtkinter


def tamanho_janela(janela, x, y):
    janela.geometry(f"{x}x{y}")

def aparencia(janela, modo):
    janela._set_appearance_mode(modo)

def frame(janela, tamanho_x = int, tamanho_y = int, local_x = int, local_y = int, color = str):
    frame = CTkFrame(janela, width=tamanho_x, height=tamanho_y, fg_color=color, corner_radius=0).place(x=local_x,y=local_y)

    return(frame)


janela = CTk() # Criando a janela
janela.title("MK - 1")

tamanho_janela(janela, x=1400, y=850)
aparencia(janela, "")

frame1 = frame(janela, local_x=0, local_y=0, tamanho_x=200, tamanho_y=850, color="black")

#janela._set_appearance_mode("dark")


janela.mainloop() # Mantendo a janela aberta