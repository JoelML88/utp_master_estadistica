import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
from scipy import stats
from tkinter import messagebox

def plot_bayes(self):
    # Obtener datos de entrada
    try:
        p_a = float(self.p_a_entry.get())
        p_b = float(self.p_b_entry.get())
        p_b_dado_a = float(self.p_b_dado_a_entry.get())

        # Cálculo de Bayes
        p_a_dado_b = (p_b_dado_a * p_a) / p_b

        # Crear la figura y los ejes
        fig, ax = plt.subplots()
        ax.bar(['P(A)', 'P(B)', 'P(B|A)', 'P(A|B)'], [p_a, p_b, p_b_dado_a, p_a_dado_b])
        ax.set_ylabel('Probabilidades')
        ax.set_title('Teorema de Bayes')

        # Mostrar el gráfico
        _show_plot(self, fig)

    except Exception as e:
        self.resultado_text.insert(tk.END, f"Error: {e}\n")

def plot_binomial(self):
    try:
        n = int(self.n_entry.get())
        k = int(self.k_entry.get())
        p = float(self.p_entry.get())

        x = np.arange(0, n+1)
        pmf = stats.binom.pmf(x, n, p)

        fig, ax = plt.subplots()
        ax.bar(x, pmf)
        ax.set_xlabel('Número de éxitos')
        ax.set_ylabel('Probabilidad')
        ax.set_title('Distribución Binomial')

        _show_plot(self, fig)
        
    except Exception as e:
        self.resultado_text.insert(tk.END, f"Error: {e}\n")

def plot_exponencial(self):
    try:
        lam = float(self.lam_entry.get())
        x = float(self.x_entry.get())

        x_vals = np.linspace(0, x, 100)
        cdf = stats.expon.cdf(x_vals, scale=1/lam)

        fig, ax = plt.subplots()
        ax.plot(x_vals, cdf)
        ax.set_xlabel('x')
        ax.set_ylabel('F(x)')
        ax.set_title('Distribución Exponencial')

        _show_plot(self, fig)

    except Exception as e:
        self.resultado_text.insert(tk.END, f"Error: {e}\n")

def plot_poisson(self):
    try:
        lmbda = float(self.lmbda_entry.get())
        k = int(self.k_entry.get())

        x = np.arange(0, k+10)
        pmf = stats.poisson.pmf(x, lmbda)

        fig, ax = plt.subplots()
        ax.bar(x, pmf)
        ax.set_xlabel('Número de eventos')
        ax.set_ylabel('Probabilidad')
        ax.set_title('Distribución de Poisson')

        _show_plot(self, fig)

    except Exception as e:
        self.resultado_text.insert(tk.END, f"Error: {e}\n")

def plot_poisson_range(self):
    try:
        lmbda = float(self.lmbda_entry.get())
        k1 = int(self.k1_entry.get())
        k2 = int(self.k2_entry.get())

        x = np.arange(k1, k2+1)
        pmf = stats.poisson.pmf(x, lmbda)

        fig, ax = plt.subplots()
        ax.bar(x, pmf)
        ax.set_xlabel('Número de eventos')
        ax.set_ylabel('Probabilidad')
        ax.setTitle('Distribución de Poisson (Rango)')

        _show_plot(self, fig)

    except Exception as e:
        self.resultado_text.insert(tk.END, f"Error: {e}\n")

def plot_normal(self):
    try:
        mu = float(self.mu_entry.get())
        sigma = float(self.sigma_entry.get())
        x = float(self.x_entry.get())

        x_vals = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        cdf = stats.norm.cdf(x_vals, mu, sigma)

        fig, ax = plt.subplots()
        ax.plot(x_vals, cdf)
        ax.set_xlabel('x')
        ax.set_ylabel('F(x)')
        ax.set_title('Distribución Normal')

        _show_plot(self, fig)

    except Exception as e:
        self.resultado_text.insert(tk.END, f"Error: {e}\n")

def _show_plot(self, fig):
    top = tk.Toplevel(self)
    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    close_button = tk.Button(top, text="Cerrar", command=lambda: _close_plot(top, fig))
    close_button.pack()

    # Asocia la destrucción de la ventana secundaria con la liberación de la figura
    top.protocol("WM_DELETE_WINDOW", lambda: _close_plot(top, fig))

def _close_plot(top, fig):
    top.destroy()
    plt.close(fig)
