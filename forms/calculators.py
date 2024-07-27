import tkinter as tk
import math
from scipy import stats

def calcular_bayes(self):
    try:
        p_a = float(self.p_a_entry.get())
        p_b = float(self.p_b_entry.get())
        p_b_dado_a = float(self.p_b_dado_a_entry.get())
        p_a_dado_b = (p_b_dado_a * p_a) / p_b
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"La probabilidad P(A|B) es: {p_a_dado_b:.4f}")
    except Exception as e:
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"Error: {e}")

def calcular_binomial(self):
    try:
        n = int(self.n_entry.get())
        k = int(self.k_entry.get())
        p = float(self.p_entry.get())
        binomial_prob = (math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)))
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"La probabilidad binomial es: {binomial_prob:.4f}")
    except Exception as e:
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"Error: {e}")

def calcular_exponencial(self):
    try:
        lam = float(self.lam_entry.get())
        x = float(self.x_entry.get())
        exp_prob = lam * math.exp(-lam * x)
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"La probabilidad exponencial es: {exp_prob:.4f}")
    except Exception as e:
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"Error: {e}")

def calcular_poisson(self):
    try:
        lmbda = float(self.lmbda_entry.get())
        k = int(self.k_entry.get())
        poisson_prob = (lmbda ** k * math.exp(-lmbda)) / math.factorial(k)
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"La probabilidad de Poisson es: {poisson_prob:.4f}")
    except Exception as e:
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"Error: {e}")

def calcular_poisson_range(self):
    try:
        lmbda = float(self.lmbda_entry.get())
        k1 = int(self.k1_entry.get())
        k2 = int(self.k2_entry.get())
        poisson_prob = sum((lmbda ** k * math.exp(-lmbda)) / math.factorial(k) for k in range(k1, k2 + 1))
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"La probabilidad de Poisson en el rango es: {poisson_prob:.4f}")
    except Exception as e:
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"Error: {e}")

def calcular_normal(self):
    try:
        mu = float(self.mu_entry.get())
        sigma = float(self.sigma_entry.get())
        x = float(self.x_entry.get())
        normal_prob = stats.norm.cdf(x, mu, sigma)
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"La probabilidad normal es: {normal_prob:.4f}")
    except Exception as e:
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"Error: {e}")


# Funciones que calculan las probabilidades
def probabilidad_binomial(n, k, p):
    coeficiente_binomial = math.comb(n, k)
    probabilidad = coeficiente_binomial * (p**k) * ((1-p)**(n-k))
    return probabilidad

def probabilidad_exponencial(lam, x):
    return 1 - math.exp(-lam * x)

def probabilidad_poisson(lmbda, k):
    probabilidad = (math.exp(-lmbda) * lmbda**k) / math.factorial(k)
    return probabilidad

def probabilidad_normal(mu, sigma, x):
    return stats.norm.cdf(x, mu, sigma)

