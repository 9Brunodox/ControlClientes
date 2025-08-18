import db
import tkinter as tk
from tkinter import ttk

def main():
    db.init_db()

    root = tk.Tk()
    root.title = ("SENAI - Cadastro de Clientes")
    root.geometry("900x500")

    # Criando o layout principal: 2 colunas
    root.columnconfigure(0, weight=1 )
    root.columnconfigure(1, weight=2 )
    root.rowconfigure(0, weight=1 )

    # Frame da esquerda (formulário futuro)
    form_frame = ttk.Frame(root, padding=10, relief="ridge")
    form_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Frame da direita (lista de clientes futura)
    lista_frame = ttk.Frame(root, padding=10, relief="ridge")
    lista_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    # Executa a janela

    root.mainloop()

if __name__ == "__main__":
    main()