import tkinter as tk
from tkinter import messagebox
import pyodbc


def connect_db():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=;'
        'DATABASE=;'
        'UID=;'
        'PWD=;'
    )

# Função para registrar usuário no banco de dados
def register_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    # Verifica se o usuário já existe
    cursor.execute("SELECT * FROM users WHERE username = ?", username)
    if cursor.fetchone():
        messagebox.showerror("Erro", "Nome de usuário já existe.")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")

    conn.close()

# Função para autenticar usuário
def login_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    # Verifica o nome de usuário e senha
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()

    conn.close()

    if result:
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        show_welcome_screen(username)
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")

# Função para exibir uma tela de boas-vindas após login
def show_welcome_screen(username):
    welcome_screen = tk.Toplevel()
    welcome_screen.title("Bem-vindo")
    welcome_screen.configure(bg="#e1f5fe")

    tk.Label(welcome_screen, text=f"Bem-vindo, {username}!", font=("Arial", 16), bg="#e1f5fe", fg="#0277bd").pack(pady=20)
    tk.Button(welcome_screen, text="OK", command=welcome_screen.destroy, font=("Arial", 12), bg="#0277bd", fg="white").pack(pady=10)

# Funções para abrir as janelas de registro e login
def register_screen():
    reg_screen = tk.Toplevel()
    reg_screen.title("Registro")
    reg_screen.configure(bg="#e3f2fd")

    tk.Label(reg_screen, text="Nome de Usuário", font=("Arial", 12), bg="#e3f2fd").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(reg_screen, text="Senha", font=("Arial", 12), bg="#e3f2fd").grid(row=1, column=0, padx=10, pady=10)

    username_entry = tk.Entry(reg_screen, font=("Arial", 12))
    password_entry = tk.Entry(reg_screen, show='*', font=("Arial", 12))
    username_entry.grid(row=0, column=1, padx=10, pady=10)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(reg_screen, text="Registrar", command=lambda: register_user(username_entry.get(), password_entry.get()), font=("Arial", 12), bg="#0277bd", fg="white").grid(row=2, column=1, pady=10)

def login_screen():
    login_screen = tk.Toplevel()
    login_screen.title("Login")
    login_screen.configure(bg="#e3f2fd")

    tk.Label(login_screen, text="Nome de Usuário", font=("Arial", 12), bg="#e3f2fd").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(login_screen, text="Senha", font=("Arial", 12), bg="#e3f2fd").grid(row=1, column=0, padx=10, pady=10)

    username_entry = tk.Entry(login_screen, font=("Arial", 12))
    password_entry = tk.Entry(login_screen, show='*', font=("Arial", 12))
    username_entry.grid(row=0, column=1, padx=10, pady=10)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(login_screen, text="Login", command=lambda: login_user(username_entry.get(), password_entry.get()), font=("Arial", 12), bg="#0277bd", fg="white").grid(row=2, column=1, pady=10)

# Tela principal com opções de registro e login
def main_screen():
    root = tk.Tk()
    root.title("Sistema de Login")
    root.geometry("300x200")
    root.configure(bg="#bbdefb")

    tk.Label(root, text="Bem-vindo ao Sistema", font=("Arial", 16), bg="#bbdefb", fg="#0d47a1").pack(pady=20)
    tk.Button(root, text="Registrar", command=register_screen, font=("Arial", 12), bg="#0288d1", fg="white").pack(pady=10)
    tk.Button(root, text="Login", command=login_screen, font=("Arial", 12), bg="#0288d1", fg="white").pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_screen()
