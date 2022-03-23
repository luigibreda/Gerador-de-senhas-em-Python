import tkinter as tk  # usado para interface gráfica
from functools import partial
import random # biblioteca que gera valores randomicos 
import pyperclip # biblioteca usada para "copiar" as coisas

def gerador_de_senhas(v_tamanho_senha):


    # Define os caracteres permitidos para serem usados nas senhas
    caracteres_disponiveis = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    # Variaveis temporarias
    senha=""
    # Faz um loop e gera as senhas com a quantidade de caracteres informada e de forma randomica
    for i in range(int(v_tamanho_senha)):
        tmp_senha="".join(random.choices(caracteres_disponiveis))
        senha=senha+tmp_senha
     
    roda_funcao=funcao_copiar(senha)

    LabelGabZika = tk.Label(root, text="Desenvolvido pela estudante Gabriela \nTHANK YOU BABY").grid(row=50, column=0)
    return senha


def funcao_copiar(senha):
    botao_copiar = tk.Button(root, text="Copiar").grid(row=9, column=0)
    pyperclip.copy(senha) # Funcao para salvar o resultado no clipboard 

def gerar_senha(LabelResultado, v_tamanho_senha):  
    v_tamanho_senha = (v_tamanho_senha.get())  
    resultado = gerador_de_senhas(v_tamanho_senha) 
    LabelResultado.config(text="Senha: \n%s" % resultado)  
    return
   
root = tk.Tk()  # Importa o construtor da GUI
root.geometry('450x300')  # Dimesoes da GUI
root.title('Gerador de senhas') # Titulo
 
v_tamanho_senha = tk.StringVar() # Variavel do tamanho da senha

LabelTamanhoSenha = tk.Label(root, text="Qual o tamanho da senha?").grid(row=2, column=0)
InputTamanhoSenha = tk.Entry(root, textvariable=v_tamanho_senha).grid(row=2, column=1)  

LabelResultado = tk.Label(root)  # Label que mostrará o resultado
LabelResultado.grid(row=8, column=0) # Posição do resultado da senha
  
gerar_senha = partial(gerar_senha, LabelResultado, v_tamanho_senha)  # Funcao chamada ao clicar no botão
v_botao_gerarsenhas = tk.Button(root, text="Gerar senhas", command=gerar_senha).grid(row=2, column=3) # Botão gerar senhas
root.mainloop()  # Inicia a GUI
