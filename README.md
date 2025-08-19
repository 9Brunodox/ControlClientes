
# 📋 Sistema de Cadastro de Clientes - SENAI

Este projeto é um sistema desktop simples de **cadastro de clientes** desenvolvido com Python e Tkinter. Ele permite **inserir, listar, editar e excluir** clientes em um banco de dados SQLite de forma intuitiva e rápida.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Tkinter** (interface gráfica)
- **SQLite3** (banco de dados embutido)
- **ttk (Themed Tkinter Widgets)**

---

## 📁 Estrutura dos Arquivos

```bash
Projeto/
├── db.py                   # Acesso e manipulação do banco de dados SQLite
├── main.py                 # Arquivo principal que inicializa e conecta a interface
├── formularioClientes.py   # Formulário de cadastro/edição de clientes
├── listarClientes.py       # Listagem de clientes em tabela com Scrollbar
└── infos.db                # Arquivo do banco de dados gerado automaticamente
```

---

## ⚙️ Funcionalidades

### ✅ Cadastro de Cliente
- Campos: Nome, E-mail, Telefone, Endereço
- Validação de campos vazios e e-mail único

### ✅ Listagem de Clientes
- Tabela dinâmica com cabeçalhos e rolagem
- Dados carregados automaticamente do banco

### ✅ Edição de Cliente
- Clique duplo em uma linha da tabela para preencher o formulário
- Botão **Atualizar** habilitado para salvar alterações

### ✅ Exclusão de Cliente
- Pressione **Delete** após selecionar um cliente
- Confirmação por pop-up de exclusão

### ✅ Botão "Limpar"
- Limpa todos os campos do formulário

---

## ▶️ Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório ou baixe os arquivos.
3. Execute o arquivo `main.py`:
```bash
python main.py
```
O banco de dados será criado automaticamente como `infos.db` se ainda não existir.

---

## 🧠 Organização Interna

- A aplicação é modular: cada componente tem seu próprio arquivo.
- Os dados são acessados via funções reutilizáveis em `db.py`.
- O layout é responsivo dentro da janela principal.
- A tabela usa `ttk.Treeview` para exibir dados.

---

## 📝 Autor

Desenvolvido por **Bruno Moreira** como parte de um projeto no SENAI.

<img width="1918" height="1031" alt="image" src="https://github.com/user-attachments/assets/43f45a02-ca74-46f6-a157-37a7b6a54fdc" />

