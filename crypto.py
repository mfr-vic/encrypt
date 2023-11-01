import os
import base64
from tkinter import *
from tkinter import messagebox


def descriptografar():
    senha = cod.get()

    if senha == "1234":
        tela_2 = Toplevel(tela)
        tela_2.title("descriptografar")
        tela_2.geometry("400x200")
        tela_2.configure(bg = "#494d7e")

        mensagem = texto_1.get(1.0, END)
        mensagem_decodificada = mensagem.encode("ascii")
        base64_bytes = base64.b64decode(mensagem_decodificada)
        descriptografar = base64_bytes.decode("ascii")


        Label(tela_2, text = "descriptografar", font = "arial", fg = "white", bg = "#494d7e").place(x = 10, y = 0)
        texto_2 = Text(tela_2, font = "Robote 10", bg = "white", relief = GROOVE, wrap = WORD, bd = 0)
        texto_2.place(x = 10, y = 40, width = 380, height = 150)

        texto_2.insert(END, descriptografar)

    elif senha == "":
        messagebox.showerror("encriptografar", "Coloque a senha.")
    
    elif senha != "1234":
        messagebox.showerror("descriptografar", "Senha incorreta.")


def encriptografar():
    senha = cod.get()

    if senha == "1234":
        tela_1 = Toplevel(tela)
        tela_1.title("encriptografar")
        tela_1.geometry("400x200")
        tela_1.configure(bg = "#272744")

        mensagem = texto_1.get(1.0, END)
        mensagem_codificada = mensagem.encode("ascii")
        base64_bytes = base64.b64encode(mensagem_codificada)
        encriptografar = base64_bytes.decode("ascii")


        Label(tela_1, text = "encriptografar", font = "arial", fg = "white", bg = "#272744").place(x = 10, y = 0)
        texto_2 = Text(tela_1, font = "Robote 10", bg = "white", relief = GROOVE, wrap = WORD, bd = 0)
        texto_2.place(x = 10, y = 40, width = 380, height = 150)

        texto_2.insert(END, encriptografar)

    elif senha == "":
        messagebox.showerror("encriptografar", "Digite a senha.")
    
    elif senha != "1234":
        messagebox.showerror("encriptografar", "Senha inválida.")


def tela_principal():

    global tela
    global cod
    global texto_1


    tela = Tk()
    tela.geometry("375x398")

    imagem_icone = PhotoImage(file = "icone.png")
    tela.iconphoto(False, imagem_icone)
    tela.title("Encriptando.")


    def reset():
        cod.set("")
        texto_1.delete(1.0, END)

    Label(text = "Adicione o texto a ser (des)criptografado:", fg = "black", font = ("calbri", 12)).place(x = 10, y = 10)
    texto_1 = Text(font = "Robote 20", bg = "white", relief = GROOVE, wrap = WORD, bd = 0)
    texto_1.place(x = 10, y = 50, width = 355, height = 100)

    Label(text = "Digite a senha para prosseguir:", fg = "black", font = ("calbri", 12)).place(x = 10, y = 170)

    cod = StringVar()
    Entry(textvariable = cod, width = 19, bd = 0, font = ("arial", 25), show = "*").place(x = 10, y = 200)


    Button(text = "Criptografar", height = "2", width = 23, bg = "#272744", fg = "white", bd = 0, command = encriptografar).place(x = 10, y = 250)
    Button(text = "Descriptografar", height = "2", width = 23, bg = "#494d7e", fg = "white", bd = 0, command = descriptografar).place(x = 200, y = 250)
    Button(text = "Resetar", height = "2", width = 50, bg = "#8b6d9c", fg = "white", bd = 0, command = reset).place(x = 10, y = 300)


    tela.mainloop()

tela_principal()