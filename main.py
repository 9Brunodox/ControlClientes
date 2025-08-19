from tkinter import messagebox
import db
import tkinter as tk
from tkinter import ttk
from listarClientes import listaClientes
from formularioClientes import FormularioCliente

def carregar_clientes(lista, termo=None):
    clientes = db.listar_clientes(termo)
    lista.carregar_dados(clientes)

def salvar_cliente(dados, formulario, lista):
    try:
        db.inserir_cliente(dados["name"], dados["email"], dados["phone"], dados["address"])
        messagebox.showinfo("Sucesso", "Cliente cadastrado!")
        formulario.limpar()
        carregar_clientes(lista)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {str(e)}")

def atualizar_cliente(dados, formulario, lista):
    try:
        db.atualizar_cliente(
            int(dados["id"]),
            dados["name"],
            dados["email"],
            dados["phone"],
            dados["address"]
        )
        messagebox.showinfo("Atualizado", "Dados atrualizados com sucesso")
        formulario.limpar()
        carregar_clientes(lista)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar: {str(e)}")

def editar_cliente(formulario, lista):
    id_ = lista.get_selected_id()
    if id_ is None:
        messagebox.showwarning("Seleção", "Selecione um cliente para editar.")
        return
    cliente = db.obter_cliente(id_)
    if cliente:
        formulario.preencher(cliente)

def excluir_cliente(formulario, lista):
    id_ = lista.get.selected_id()
    if id_ is None:
        messagebox.showwarning("Seleção", "Selecione um cliente para excluir.")
        return
    if messagebox.askyesno("Excluir", "Tem certeza que deseja excluir este cliente?"):
        db.excluir_cliente(id_)
        formulario.limpar()
        carregar_clientes(lista)

def main():
    db.init_db()

    root = tk.Tk()
    root.title = ("SENAI - Cadastro de Clientes")
    root.geometry("900x500")

    # Criando o layout principal: 2 colunas
    root.columnconfigure(0, weight=1 )
    root.columnconfigure(1, weight=2 )
    root.rowconfigure(0, weight=1 )

    # Formulário (lado esquerdo)
    formulario = FormularioCliente(
        root,
        on_salvar=lambda dados: salvar_cliente(dados, formulario, lista),
        on_atualizar=lambda dados: atualizar_cliente(dados, formulario, lista)
    )
    formulario.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)



    # Lista de clientes (lado direito)
    lista = listaClientes(root)
    lista.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

    # Ações da lista: duplo clique para editar, delete para excluir
    lista.tree.bind("<Double-1>", lambda e: editar_cliente(formulario, lista))
    lista.tree.bind("<Delete>", lambda e: excluir_cliente(formulario, lista))

    carregar_clientes(lista)

    # Executa a janela
    root.mainloop()

if __name__ == "__main__":
    main()