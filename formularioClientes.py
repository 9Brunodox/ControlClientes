import tkinter as tk
from tkinter import ttk

class FormularioCliente(ttk.LabelFrame):
    def __init__(self, master, on_salvar, on_atualizar, on_excluir):
        super().__init__(master, text="Cadastro de Cliente")
        self.on_salvar = on_salvar
        self.on_atualizar = on_atualizar
        self.on_excluir = on_excluir

        self.id_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.telefone_var = tk.StringVar()
        self.endereco_var = tk.StringVar()

        # Campos
        ttk.Label(self, text="Nome").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(self, textvariable=self.nome_var).grid(row=0, column=1, sticky="ew", padx=5)

        ttk.Label(self, text="E-mail").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(self, textvariable=self.email_var).grid(row=1, column=1, sticky="ew", padx=5)

        ttk.Label(self, text="Telefone").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(self, textvariable=self.telefone_var).grid(row=2, column=1, sticky="ew", padx=5)

        ttk.Label(self, text="Endereço").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(self, textvariable=self.endereco_var).grid(row=3, column=1, sticky="ew", padx=5)


        # Botões
        botoes = ttk.Frame(self)
        botoes.grid(row=4, column=0, columnspan=2, sticky="e", padx=5, pady=10)

        self.btn_salvar = ttk.Button(botoes, text="Salvar", command=self._salvar)
        self.btn_salvar.grid(row=0, column=0, padx=5)

        self.btn_atualizar = ttk.Button(botoes, text="Atualizar", command=self._atualizar, state="disabled")
        self.btn_atualizar.grid(row=0, column=1, padx=5)

        self.btn_atualizar = ttk.Button(botoes, text="Atualizar", command=self._atualizar, state="disabled")
        self.btn_atualizar.grid(row=0, column=1, padx=5)

        self.btn_limpar = ttk.Button(botoes, text="Limpar", command=self.limpar)
        self.btn_limpar.grid(row=0, column=2, padx=5)

        self.btn_excluir = ttk.Button(botoes, text="Excluir", command=self._excluir, state="disabled")
        self.btn_excluir.grid(row=0, column=3, padx=5)


        self.columnconfigure(1, weight=1)

    def limpar(self):
        self.id_var.set("")
        self.nome_var.set("")
        self.email_var.set("")
        self.telefone_var.set("")
        self.endereco_var.set("")
        self._ativar_salvar()

    def preencher(self, cliente):
        self.id_var.set(cliente["id"])
        self.nome_var.set(cliente["name"])
        self.email_var.set(cliente["email"])
        self.telefone_var.set(cliente["phone"])
        self.endereco_var.set(cliente["address"])
        self._ativar_atualizar()

    def _salvar(self):
        dados = self._obter_dados()
        self.on_salvar(dados)

    def _atualizar(self):
        dados = self._obter_dados()
        self.on_atualizar(dados)

    def _obter_dados(self):
        return {
            "id": self.id_var.get(),
            "name": self.nome_var.get().strip(),
            "email": self.email_var.get().strip(),
            "phone": self.telefone_var.get().strip(),
            "address": self.endereco_var.get().strip()
        }

    def _ativar_salvar(self):
        self.btn_salvar.config(state="normal")
        self.btn_atualizar.config(state="disabled")
        self.btn_excluir.config(state="disabled")


    def _ativar_atualizar(self):
        self.btn_salvar.config(state="disabled")
        self.btn_atualizar.config(state="normal")
        self.btn_excluir.config(state="normal")


    def _excluir(self):
        dados = self._obter_dados()
        if dados["id"]:
            self.on_excluir(dados)

