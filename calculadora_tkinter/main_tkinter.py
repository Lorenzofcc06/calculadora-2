import tkinter as tk

def clique(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, atual + botao)

def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def limpar():
    entrada.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora Tkinter")
root.geometry("350x500")
root.resizable(False, False)

for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

entrada = tk.Entry(root, font=("Arial", 22), justify="right", bd=10, relief="ridge")
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", ipadx=8, ipady=8)

botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (txt, linha, coluna) in botoes:
    if txt == "=":
        btn = tk.Button(root, text=txt, font=("Arial", 20), bg="lightblue", command=calcular)
    else:
        btn = tk.Button(root, text=txt, font=("Arial", 20), command=lambda t=txt: clique(t))
    
    btn.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

btn_limpar = tk.Button(root, text="C", font=("Arial", 20), bg="red", command=limpar)
btn_limpar.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

root.mainloop()
