import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")

        self.tasks = []

        # Interface Gráfica
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, relief="flat", background="#007BFF", foreground="white")
        self.style.configure("TLabel", padding=6, font=('Arial', 11), foreground="black")

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=('Arial', 12))
        self.task_listbox.pack(pady=10)

        self.add_button = ttk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(pady=5)

        self.edit_button = ttk.Button(root, text="Editar Tarefa", command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.delete_button = ttk.Button(root, text="Excluir Tarefa", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.save_button = ttk.Button(root, text="Salvar Tarefas", command=self.save_tasks)
        self.save_button.pack(pady=10)

        # Carregar tarefas salvas
        self.load_tasks()

    def add_task(self):
        task_name = simpledialog.askstring("Adicionar Tarefa", "Digite o nome da tarefa:")
        if task_name:
            self.tasks.append(task_name)
            self.update_task_list()

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            current_task = self.tasks[selected_index]
            new_task_name = simpledialog.askstring("Editar Tarefa", "Digite o novo nome da tarefa:",
                                                   initialvalue=current_task)
            if new_task_name:
                self.tasks[selected_index] = new_task_name
                self.update_task_list()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.tasks[selected_index]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("Salvo", "Tarefas salvas com sucesso!")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_task_list()
        except FileNotFoundError:
            pass  # Se o arquivo não existir, não há tarefas para carregar


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.geometry("400x400")
    root.resizable(False, False)
    root.mainloop()
