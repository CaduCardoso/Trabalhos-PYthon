import tkinter as tk
from tkinter import messagebox


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        # Rótulo para a entrada da tarefa
        self.label = tk.Label(self.root, text="Digite a tarefa:")
        self.label.pack(pady=10)

        # Entrada para a tarefa
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Botão para adicionar a tarefa
        self.add_button = tk.Button(
            self.root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(pady=10)

        # Listbox para exibir as tarefas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Botão para remover a tarefa selecionada
        self.remove_button = tk.Button(
            self.root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve digitar uma tarefa.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning(
                "Aviso", "Você deve selecionar uma tarefa para remover.")

    def update_tasks_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


# Executando o programa principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
