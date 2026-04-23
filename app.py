import tkinter as tk
from tkinter import messagebox, ttk

def salvar_dados():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    tel = entry_tel.get()
    nasc = entry_nasc.get()

    # Validações de tamanho
    
    if not nome:
        messagebox.showerror("Erro", "O nome é obrigatorio.")
    elif len(cpf) < 11 or len (cpf) > 11 or not cpf.isdigit():
        messagebox.showerror("Erro", "CPF deve conter exatamente 11 números.")
    elif len(tel) < 10 or len(tel) > 11 or not tel.isdigit():
        messagebox.showerror("Erro", "Erro! número do telefone não existe.")
    elif len(nasc) < 8 or len (nasc) > 8 or not nasc.isdigit():
        messagebox.showerror("Erro", "Data de Nascimento deve ter 8 números.")
    else:
        # Adiciona na tabela (Treeview)
        tree.insert("", tk.END, values=(nome, cpf, tel, nasc))
        limpar_campos()
        messagebox.showinfo("Sucesso", "Dados armazenados com sucesso!")

def deletar_item():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Aviso", "Selecione um registro para apagar.")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_tel.delete(0, tk.END)
    entry_nasc.delete(0, tk.END)

# Configuração da Janela Principal
root = tk.Tk()
root.title("Gerenciador de Cadastros")
root.geometry("600x450")

# Layout de Entrada
frame_inputs = tk.Frame(root, pady=10)
frame_inputs.pack()

labels = ["Nome:", "CPF :", "Telefone :", "Data de Nascimento:"]
entries = []

for i, text in enumerate(labels):
    tk.Label(frame_inputs, text=text).grid(row=i, column=0, sticky="w", padx=5, pady=2)
    entry = tk.Entry(frame_inputs, width=30)
    entry.grid(row=i, column=1, padx=5, pady=2)
    entries.append(entry)

entry_nome, entry_cpf, entry_tel, entry_nasc = entries

# Botões
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

btn_salvar = tk.Button(frame_botoes, text="Salvar", command=salvar_dados, bg="green", fg="white", width=10)
btn_salvar.pack(side=tk.LEFT, padx=5)

btn_deletar = tk.Button(frame_botoes, text="Apagar Selecionado", command=deletar_item, bg="red", fg="white")
btn_deletar.pack(side=tk.LEFT, padx=5)

# Tabela (Visualização dos dados)
columns = ("nome", "cpf", "tel", "nasc")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
tree.heading("nome", text="Nome")
tree.heading("cpf", text="CPF")
tree.heading("tel", text="Telefone")
tree.heading("nasc", text="Nascimento")

# Ajuste de largura das colunas
for col in columns:
    tree.column(col, width=120)

tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
