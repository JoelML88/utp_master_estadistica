import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR
import utils.util_window as u_window
import utils.util_images as u_image
from tkinter import messagebox

from forms.calculators import (
    calcular_bayes, calcular_binomial, calcular_exponencial,
    calcular_poisson, calcular_poisson_range, calcular_normal
)

"""
from plotting import (
    plot_bayes, plot_binomial, plot_exponencial,
    plot_poisson, plot_poisson_range, plot_normal
)
"""

class main_window(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.logo = u_image.read_image("./images/logo.png",(560,136))
        self.perfil = u_image.read_image("./images/Perfil.png",(100,100))
        self.config_window()
        self.panels()
        self.controles_barra_superior()
        self.controles_menulateral()
        self.controles_body()
        
        
        
    def config_window(self):
        self.title("Python GUI")
        self.iconbitmap("./images/logo.ico")
        w,h=1024,600
        self.geometry("%dx%d+0+0" % (w, h))
        u_window.centrar_ventana(self, w, h)
        
    def panels(self):
        self.barra_superior = tk.Frame(
            self, bg =  COLOR_BARRA_SUPERIOR,height=50) #50 characters
        self.barra_superior.pack(side=tk.TOP,fill='both')
        
        self.menu_lateral = tk.Frame(
            self, bg = COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side = tk.LEFT, fill='both', expand=False)
        
        self.cuerpo_principal = tk.Frame(
            self, bg = COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side = tk.RIGHT, fill='both', expand=True)
        
        
    def controles_barra_superior(self):
        
        font_awesome = font.Font(family='FontAwesome', size=12)
        
        self.labelTitulo = tk.Label(self.barra_superior, text="Estadística")
        self.labelTitulo.config(fg='#fff', font=("Roboto",15), bg=COLOR_BARRA_SUPERIOR,pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)
        
        #Botón del menú lateral
        self.btn_lateral = tk.Button(self.barra_superior,font=font_awesome,text="\uf023",
                                     command = self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.btn_lateral.pack(side=tk.LEFT)
        
        #Etiqueta de info
        self.labelTitulo = tk.Label(
            self.barra_superior, text="Joel Méndez León ")
        self.labelTitulo.config(fg="#fff", font=(
            "Robot",10), bg=COLOR_BARRA_SUPERIOR,padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)

        self.labelTitulo = tk.Label(
            self.barra_superior, text=" Rosalba Bolaños Ortega")
        self.labelTitulo.config(fg="#fff", font=(
            "Robot",10), bg=COLOR_BARRA_SUPERIOR,padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
        
        
    def controles_menulateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
        
        #Etiqueta de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)
        
        #Buttons
        self.btn_dash_board = tk.Button(self.menu_lateral)
        self.btn_profile = tk.Button(self.menu_lateral)
        self.btn_picture = tk.Button(self.menu_lateral)
        self.btn_info = tk.Button(self.menu_lateral)
        self.btn_settings = tk.Button(self.menu_lateral)
        
        buttons_info=[
            ("Bayes", "\uf053", self.btn_dash_board, lambda: mostrar_bayes(self)),
            ("Binomial", "\uf107", self.btn_profile, lambda: mostrar_binomial(self)),
            ("Exponencial", "\uf03e", self.btn_picture, lambda: mostrar_exponencial(self)),
            ("Poisson", "\uf129", self.btn_info, lambda: mostrar_poisson(self)),
            ("Poisson Range", "\uf013", self.btn_settings, lambda: mostrar_poisson_range(self)),
            ("Normal", "\uf013", self.btn_settings, lambda: mostrar_normal(self))
        ]
        
        #, command=mostrar_bayes

        for text, icon, btn, pantalla in buttons_info:
            self.configurar_btns_menu(btn, text, icon, font_awesome, ancho_menu, alto_menu, pantalla)
    
    def controles_body(self):
        label = tk.Label(self.cuerpo_principal,image = self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0,y=0, relwidth=1,relheight=1)
        
            
    def configurar_btns_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, pantalla):
        button.config(text=f"{icon} {text}", anchor="w", font=font_awesome, bd=0, command=pantalla, bg=COLOR_MENU_LATERAL, fg = "white", width = ancho_menu, height = alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)
        
    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
        
    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR,fg='white')
        
    def on_leave(self, event, button): 
        button.config(bg=COLOR_MENU_LATERAL,fg='white')
        
    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side = tk.LEFT, fill='y')


    # Funciones para mostrar las ventanas de cada método
def mostrar_bayes(self):
    limpiar_frame(self.cuerpo_principal)
    
    messagebox.showerror("Cargando Bayes", "Bayes")

    tk.Label(self.cuerpo_principal, text="Calculadora de Bayes").pack(pady=10)
    
    tk.Label(self.cuerpo_principal, text="P(A)").pack()
    global p_a_entry
    p_a_entry = tk.Entry(self.cuerpo_principal)
    p_a_entry.pack()

    tk.Label(self.cuerpo_principal, text="P(B)").pack()
    global p_b_entry
    p_b_entry = tk.Entry(self.cuerpo_principal)
    p_b_entry.pack()

    tk.Label(self.cuerpo_principal, text="P(B|A)").pack()
    global p_b_dado_a_entry
    p_b_dado_a_entry = tk.Entry(self.cuerpo_principal)
    p_b_dado_a_entry.pack()

    tk.Button(self.cuerpo_principal, text="Calcular", command=calcular_bayes).pack(pady=20)


def mostrar_binomial(self):
    limpiar_frame(self.cuerpo_principal)
    tk.Label(self.cuerpo_principal, text="Calculadora Binomial").pack(pady=10)
    
    tk.Label(self.cuerpo_principal, text="Número de ensayos (n)").pack()
    global n_entry
    n_entry = tk.Entry(self.cuerpo_principal)
    n_entry.pack()

    tk.Label(self.cuerpo_principal, text="Número de éxitos (k)").pack()
    global k_entry
    k_entry = tk.Entry(self.cuerpo_principal)
    k_entry.pack()

    tk.Label(self.cuerpo_principal, text="Probabilidad de éxito (p)").pack()
    global p_entry
    p_entry = tk.Entry(self.cuerpo_principal)
    p_entry.pack()

    tk.Button(self.cuerpo_principal, text="Calcular", command=calcular_binomial).pack(pady=20)

def mostrar_exponencial(self):
    limpiar_frame(self.cuerpo_principal)
    tk.Label(self.cuerpo_principal, text="Calculadora Exponencial").pack(pady=10)
    
    tk.Label(self.cuerpo_principal, text="Tasa de eventos (λ)").pack()
    global lam_entry
    lam_entry = tk.Entry(self.cuerpo_principal)
    lam_entry.pack()

    tk.Label(self.cuerpo_principal, text="Valor de x").pack()
    global x_entry
    x_entry = tk.Entry(self.cuerpo_principal)
    x_entry.pack()

    tk.Button(self.cuerpo_principal, text="Calcular", command=calcular_exponencial).pack(pady=20)

def mostrar_poisson(self):
    limpiar_frame(self.cuerpo_principal)
    tk.Label(self.cuerpo_principal, text="Calculadora Poisson").pack(pady=10)
    
    tk.Label(self.cuerpo_principal, text="Número promedio de eventos (λ)").pack()
    global lmbda_entry
    lmbda_entry = tk.Entry(self.cuerpo_principal)
    lmbda_entry.pack()

    tk.Label(self.cuerpo_principal, text="Número de eventos (k)").pack()
    global k_entry
    k_entry = tk.Entry(self.cuerpo_principal)
    k_entry.pack()

    tk.Button(self.cuerpo_principal, text="Calcular", command=calcular_poisson).pack(pady=20)

# Función para mostrar la ventana de Poisson
def mostrar_poisson_range(self):
    limpiar_frame(self.cuerpo_principal)
    tk.Label(self.cuerpo_principal, text="Calculadora Poisson").pack(pady=10)
    
    tk.Label(self.cuerpo_principal, text="Número promedio de eventos (λ)").pack()
    global lmbda_entry
    lmbda_entry = tk.Entry(self.cuerpo_principal)
    lmbda_entry.pack()

    tk.Label(self.cuerpo_principal, text="Valor de k1 (inferior)").pack()
    global k1_entry
    k1_entry = tk.Entry(self.cuerpo_principal)
    k1_entry.pack()

    tk.Label(self.cuerpo_principal, text="Valor de k2 (superior)").pack()
    global k2_entry
    k2_entry = tk.Entry(self.cuerpo_principal)
    k2_entry.pack()

    tk.Button(self.cuerpo_principal, text="Calcular", command=calcular_poisson_range).pack(pady=20)

def mostrar_normal(self):
    limpiar_frame(self.cuerpo_principal)
    tk.Label(self.cuerpo_principal, text="Calculadora Normal").pack(pady=10)
    
    tk.Label(self.cuerpo_principal, text="Media (μ)").pack()
    global mu_entry
    mu_entry = tk.Entry(self.cuerpo_principal)
    mu_entry.pack()

    tk.Label(self.cuerpo_principal, text="Desviación estándar (σ)").pack()
    global sigma_entry
    sigma_entry = tk.Entry(self.cuerpo_principal)
    sigma_entry.pack()

    tk.Label(self.cuerpo_principal, text="Valor de x").pack()
    global x_entry
    x_entry = tk.Entry(self.cuerpo_principal)
    x_entry.pack()

    tk.Button(self.cuerpo_principal, text="Calcular", command=calcular_normal).pack(pady=20)


# Función para limpiar el frame
def limpiar_frame(cuerpo_principal):
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()




"""
# Funciones de cálculo
def calcular_bayes():
    try:
        p_a = float(p_a_entry.get())
        p_b = float(p_b_entry.get())
        p_b_dado_a = float(p_b_dado_a_entry.get())
        p_a_dado_b = (p_b_dado_a * p_a) / p_b
        messagebox.showinfo("Resultado de Bayes", f"La probabilidad P(A|B) es: {p_a_dado_b:.6f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def calcular_binomial():
    try:
        n = int(n_entry.get())
        k = int(k_entry.get())
        p = float(p_entry.get())
        resultado = probabilidad_binomial(n, k, p)
        messagebox.showinfo("Resultado Binomial", f"La probabilidad binomial es: {resultado:.6f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def calcular_exponencial():
    try:
        lam = float(lam_entry.get())
        x = float(x_entry.get())
        resultado = probabilidad_exponencial(lam, x)
        messagebox.showinfo("Resultado Exponencial", f"La probabilidad exponencial es: {resultado:.6f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def calcular_poisson():
    try:
        lmbda = float(lmbda_entry.get())
        k = int(k_entry.get())
        resultado = probabilidad_poisson(lmbda, k)
        messagebox.showinfo("Resultado Poisson", f"La probabilidad de Poisson es: {resultado:.6f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Funciones de cálculo
def calcular_poisson_range():
    try:
        lmbda = float(lmbda_entry.get())
        k1 = int(k1_entry.get())
        k2 = int(k2_entry.get())
        
        # Calcular la probabilidad para el rango de k1 a k2
        probabilidad_acumulada = 0
        resultado_texto = ""
        for k in range(k1, k2 + 1):
            probabilidad = probabilidad_poisson(lmbda, k)
            probabilidad_acumulada += probabilidad
            resultado_texto += f"P(K = {k}) = {probabilidad:.6f}\n"

        resultado_texto += f"\nProbabilidad total en el rango [{k1}, {k2}] = {probabilidad_acumulada:.6f}"
        messagebox.showinfo("Resultado de Poisson", resultado_texto)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def calcular_normal():
    try:
        mu = float(mu_entry.get())
        sigma = float(sigma_entry.get())
        x = float(x_entry.get())
        resultado = probabilidad_normal(mu, sigma, x)
        messagebox.showinfo("Resultado Normal", f"La probabilidad normal es: {resultado:.6f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")


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
"""