import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# Dicionário com produtos, códigos e preços
produtos = {
    1: {"produto": "Açúcar", "preco": 4.09},
    2: {"produto": "Arroz", "preco": 5.47},
    3: {"produto": "Feijão", "preco": 9.56},
    4: {"produto": "Carne", "preco": 40.0},
}

# Dicionário para armazenar as seleções do usuário
selecoes = {}

def calcular_total(quilo, valor):
    return quilo * valor

def mostrar_carrinho():
    carrinho_text.delete(1.0, tk.END)  # Limpa o texto anterior

    carrinho_text.insert(tk.END, "Mercadinho Econômico\n\n")
    carrinho_text.insert(tk.END, "============================ Carrinho de Compras ============================\n\n")

    if not selecoes:
        carrinho_text.insert(tk.END, "Seu carrinho está vazio.")
    else:
        for codigo, quilo in selecoes.items():
            produto_info = produtos[codigo]
            total_produto = calcular_total(quilo, produto_info["preco"])

            carrinho_text.insert(tk.END, f"Produto: {produto_info['produto']}\n")
            carrinho_text.insert(tk.END, f"Quilo: {quilo}\n")
            carrinho_text.insert(tk.END, f"Total: R$ {total_produto:.2f}\n\n")

    carrinho_text.insert(tk.END, f"Valor total da compra: R$ {calcular_total_compra():.2f}\n")
    carrinho_text.insert(tk.END, "=============================================================================")

def calcular_total_compra():
    total = 0.0
    for codigo, quilo in selecoes.items():
        produto_info = produtos[codigo]
        total += calcular_total(quilo, produto_info["preco"])
    return total

def adicionar_produto():
    produto_selecionado = produto_combobox.get()
    quilo = quilo_entry.get()

    if not produto_selecionado:
        messagebox.showerror("Erro", "Selecione um produto válido.")
        return

    codigo_escolhido = None
    for codigo, info in produtos.items():
        if info["produto"] == produto_selecionado:
            codigo_escolhido = codigo
            break

    if not quilo.isdigit():
        messagebox.showerror("Erro", "Digite uma quantidade válida.")
        return

    quilo = int(quilo)

    if codigo_escolhido in selecoes:
        selecoes[codigo_escolhido] += quilo
    else:
        selecoes[codigo_escolhido] = quilo

    mostrar_carrinho()
    quilo_entry.delete(0, tk.END)

def finalizar_compra():
    mostrar_carrinho()
    messagebox.showinfo("Compra Finalizada", "Compra finalizada, obrigado e volte sempre!")

def cadastrar_produto():
    novo_produto = simpledialog.askstring("Cadastro de Produto", "Nome do novo produto:")
    if novo_produto:
        novo_preco = simpledialog.askfloat("Cadastro de Produto", f"Preço do {novo_produto}:")
        if novo_preco is not None:
            novo_codigo = max(produtos.keys()) + 1
            produtos[novo_codigo] = {"produto": novo_produto, "preco": novo_preco}
            atualizar_combobox()

def atualizar_combobox():
    produtos_disponiveis = [info["produto"] for info in produtos.values()]
    produto_combobox["values"] = produtos_disponiveis

# Criar a janela principal
root = tk.Tk()
root.title("Mercadinho Econômico")

# Criar rótulos e caixas de entrada
produto_label = tk.Label(root, text="Produto:")
produto_label.pack()

produto_combobox = ttk.Combobox(root, values=[], state="readonly")
produto_combobox.pack()

quilo_label = tk.Label(root, text="Quantidade (Kg):")
quilo_label.pack()

quilo_entry = tk.Entry(root)
quilo_entry.pack()

# Botões
adicionar_button = tk.Button(root, text="Adicionar ao Carrinho", command=adicionar_produto)
adicionar_button.pack()

finalizar_button = tk.Button(root, text="Finalizar Compra", command=finalizar_compra)
finalizar_button.pack()

cadastrar_produto_button = tk.Button(root, text="Cadastrar Produto", command=cadastrar_produto)
cadastrar_produto_button.pack()

# Texto do carrinho
carrinho_text = tk.Text(root, height=20, width=50)
carrinho_text.pack()

# Atualizar o menu suspenso (combobox) com os produtos disponíveis
atualizar_combobox()

# Iniciar a interface gráfica
root.mainloop()

