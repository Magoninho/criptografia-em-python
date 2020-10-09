from tkinter import *

alfabeto = 'abcdefghijklmnopqrstuvwxyz '

encrypt = ''
descrypt = ''


win = Tk()


def gotolink():
    
    nova_janela = Toplevel(win)
    nova_janela.title("Sobre")
    h_sobre = Label(nova_janela, text="Sobre", font=("Arial", 16))
    nova_janela.geometry("500x200")
    h_sobre.pack()

    l_sobre = Label(nova_janela, text="Programa feito por Magoninho Gamer\nPode copiar o código a vontade, aqui a parada é open-source")
    l_sobre.pack()

def encriptar():
    global encrypt, alfabeto
    key = int(i_chave.get())
    mensagem = str(i_mensagem.get())
    
    for i in mensagem:
        # encriptada
        posicao = alfabeto.find(i)
        novaposicao = (posicao + key) % 27
        encrypt += alfabeto[novaposicao]
    final.delete('1.0', END)
    final.insert(END, encrypt)
    encrypt = ''


def decriptar():
    global descrypt, alfabeto
    key = int(i_chave.get())
    mensagem = str(i_mensagem.get())
    for j in mensagem:
        # descriptada
        posicao = alfabeto.find(j)
        novaposicao = (posicao - key) % 27
        descrypt += alfabeto[novaposicao]
    final.delete('1.0', END)
    final.insert(END, descrypt)
    descrypt = ''




win.title("CRIPTOGRAFADOR DO MAGO")
win.geometry("600x420") ## geometria da janela

bemvindo = Label(win, text="BEM-VINDO AO \nCRIPTOGRAFADOR DO MAGO", font=("Arial", 16)) ## Header

bemvindo.grid(row=0, column=1)

link1 = Label(win, text="Sobre", fg="blue", cursor="hand2")
link1.bind("<Button-1>", lambda e: gotolink())
link1.grid(row=1, column=1)
## Input ##

l_chave = Label(win, text="Chave")
l_chave.grid(row=2,column=0, padx= 10, pady=10)

i_chave = Entry(win, width=45)
i_chave.grid(row=2, column=1)

l_mensagem = Label(win, text="Mensagem")
l_mensagem.grid(row=3,column=0, padx= 10, pady=10)

i_mensagem = Entry(win, width=45)
i_mensagem.grid(row=3, column=1)


# vxcjpbbxoutst
### CRIPTOGRAFAR / DESCRIPPTOGRAFAR ###

btn_encript = Button(win, text="   Criptografar   ", command=encriptar)
btn_decript = Button(win, text="Descriptografar", command=decriptar)

btn_encript.grid(row=4, column=1)
btn_decript.grid(row=5, column=1)



### Mensagem final ###
l_final = Label(win, text="Mensagem final:").grid(row=6, column=1)
final = Text(win, height=10, width=50)
final.grid(row=7, column=1)


win.mainloop()
