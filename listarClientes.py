import tkinter as tk
from tkinter import ttk

class listaClientes(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Clientes Cadastrados")

        # Título da tabela
        colunas = ("id", "name", "email", "phone", "address")

        self.tree = ttk.Treeview(self, columns=colunas, show="headings", height=15)
        for col in colunas:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, anchor="w", width=150)
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Expansão do frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def carregar_dados(self, clientes):
        self.tree.delete(*self.tree.get_children())
        for cliente in clientes:
            self.tree.insert("", "end", values=(
                cliente["id"],
                cliente["name"],
                cliente["email"],
                cliente["phone"],
                cliente["address"]
            ))