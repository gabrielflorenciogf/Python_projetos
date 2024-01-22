import psutil
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt  # Adiciona esta linha

class SystemMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de Atividade de Sistema")

        self.create_widgets()

    def create_widgets(self):
        self.cpu_label = ttk.Label(self.root, text="Uso de CPU:")
        self.cpu_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.cpu_progress = ttk.Progressbar(self.root, length=300, mode='determinate')
        self.cpu_progress.grid(row=0, column=1, padx=10, pady=10)

        self.memory_label = ttk.Label(self.root, text="Uso de Memória:")
        self.memory_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.memory_progress = ttk.Progressbar(self.root, length=300, mode='determinate')
        self.memory_progress.grid(row=1, column=1, padx=10, pady=10)

        self.processes_label = ttk.Label(self.root, text="Número de Processos:")
        self.processes_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.processes_value = ttk.Label(self.root, text="")
        self.processes_value.grid(row=2, column=1, padx=10, pady=10)

        self.fig, self.ax = self.create_cpu_plot()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

        self.update_system_info()

    def create_cpu_plot(self):
        fig, ax = plt.subplots(figsize=(4, 2), dpi=100)
        ax.set_title("Uso de CPU ao Longo do Tempo")
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Uso de CPU (%)")
        return fig, ax

    def update_system_info(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        num_processes = len(psutil.pids())

        # Atualiza barras de progresso e rótulos
        self.cpu_progress["value"] = cpu_percent
        self.memory_progress["value"] = memory_percent
        self.cpu_label.config(text=f"Uso de CPU: {cpu_percent:.2f}%")
        self.memory_label.config(text=f"Uso de Memória: {memory_percent:.2f}%")
        self.processes_value.config(text=f"{num_processes}")

        # Adiciona ponto ao gráfico
        self.ax.scatter(self.ax.get_xlim()[1], cpu_percent, color='blue')
        self.ax.set_xlim(left=max(0, self.ax.get_xlim()[1] - 60), right=self.ax.get_xlim()[1])
        
        self.root.after(1000, self.update_system_info)  # Atualiza a cada segundo

def main():
    root = tk.Tk()
    app = SystemMonitor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
